"""
database.py - FırsatPusulası SQLite Veritabanı Yönetim Modülü
"""

import sqlite3
import os
import sys
from typing import List, Dict, Any, Optional, Tuple

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DB_FILE = "firsat_pusulasi.db"

class DatabaseManager:
    """SQLite veritabanı bağlantı ve tablo yönetim sınıfı."""
    
    def __init__(self, db_path: str = DB_FILE):
        self.db_path = db_path
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        """Veritabanı bağlantısı döndürür."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        """Veritabanı tablolarını (opportunities ve user_profiles) oluşturur."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Fırsatlar Tablosu
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS opportunities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    organization TEXT DEFAULT 'Genel',
                    description TEXT DEFAULT '',
                    requirements TEXT DEFAULT '',
                    min_grade_level INTEGER DEFAULT 1,
                    location TEXT DEFAULT 'Türkiye',
                    deadline DATE NOT NULL,
                    link TEXT DEFAULT '#',
                    tags TEXT DEFAULT '',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Kullanıcı Profili Tablosu
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    grade_level INTEGER DEFAULT 2,
                    skills TEXT,
                    interested_categories TEXT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def add_opportunity(self, title: str, category: str, deadline: str, 
                        link: str = "#", tags: str = "", organization: str = "Genel",
                        description: str = "", requirements: str = "", 
                        min_grade_level: int = 1, location: str = "Türkiye") -> int:
        """Yeni bir fırsat kaydı ekler."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO opportunities 
                (title, category, organization, description, requirements, min_grade_level, location, deadline, link, tags)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (title, category, organization, description, requirements, min_grade_level, location, deadline, link, tags))
            conn.commit()
            return cursor.lastrowid

    def get_all_opportunities(self, raw_tuples: bool = True) -> List[Any]:
        """
        Tüm fırsatları son başvuru tarihine göre sıralı getirir.
        raw_tuples=True: Streamlit pd.DataFrame(..., columns=["ID", "Başlık", "Kategori", "Son Tarih", "Link", "Etiketler"]) uyumlu.
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, category, deadline, link, tags, organization, description, requirements, min_grade_level, location FROM opportunities ORDER BY deadline ASC")
            rows = cursor.fetchall()
            
            if raw_tuples:
                # App.py 6 kolonlu pd.DataFrame beklentisini karşılamak için 6'lı tuple döndürür
                return [(r["id"], r["title"], r["category"], r["deadline"], r["link"], r["tags"]) for r in rows]
            else:
                return [dict(r) for r in rows]

    def get_all_opportunities_dict(self) -> List[Dict[str, Any]]:
        """Tüm fırsatları dictionary formatında döndürür."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM opportunities ORDER BY deadline ASC")
            return [dict(r) for r in cursor.fetchall()]

    def get_opportunities_by_category(self, category: str, raw_tuples: bool = True) -> List[Any]:
        """Belirli bir kategorideki fırsatları getirir."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, category, deadline, link, tags, organization, description, requirements, min_grade_level, location FROM opportunities WHERE category = ? ORDER BY deadline ASC", (category,))
            rows = cursor.fetchall()
            
            if raw_tuples:
                return [(r["id"], r["title"], r["category"], r["deadline"], r["link"], r["tags"]) for r in rows]
            else:
                return [dict(r) for r in rows]

    def clear_opportunities(self) -> None:
        """Fırsatlar tablosunu temizler."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM opportunities")
            conn.commit()

    def save_user_profile(self, name: str, grade_level: int, skills: str, interested_categories: str) -> None:
        """Kullanıcı profilini kaydeder veya günceller."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_profiles")
            cursor.execute('''
                INSERT INTO user_profiles (name, grade_level, skills, interested_categories)
                VALUES (?, ?, ?, ?)
            ''', (name, grade_level, skills, interested_categories))
            conn.commit()

    def get_user_profile(self) -> Optional[Dict[str, Any]]:
        """Kayıtlı kullanıcı profilini döndürür."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_profiles ORDER BY id DESC LIMIT 1")
            row = cursor.fetchone()
            return dict(row) if row else None


if __name__ == "__main__":
    db = DatabaseManager()
    print(" Veritabanı başlatıldı:", db.db_path)
