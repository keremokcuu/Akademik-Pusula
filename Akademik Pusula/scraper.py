"""
scraper.py - Örnek Veri Yükleme ve Scraping Modülü
"""

import sys
from datetime import date, timedelta
from typing import List, Dict, Any
from database import DatabaseManager

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class ScraperModule:
    """Fırsat verilerini toplayan ve veritabanına aktaran modül."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def generate_mock_data(self) -> List[Dict[str, Any]]:
        today = date.today()

        mock_opportunities = [
            {
                "title": "TEKNOFEST 2026 Yapay Zeka Yarışması",
                "category": "Yarışma",
                "organization": "T3 Vakfı & Sanayi ve Teknoloji Bakanlığı",
                "description": "Doğal dil işleme ve bilgisayarlı görü projeleri yarışması. Takım başvuruları açık.",
                "requirements": "Python, PyTorch, Git, Yapay Zeka, Takım Çalışması",
                "min_grade_level": 1,
                "location": "İstanbul / Çevrim içi",
                "deadline": (today + timedelta(days=12)).isoformat(),
                "link": "https://teknofest.org/tr/competitions/",
                "tags": "Python, Yapay Zeka, PyTorch, Lise, Lisans"
            },
            {
                "title": "TÜBİTAK 2247-C STAR Stajyer Araştırmacı Burs Programı",
                "category": "Akademik",
                "organization": "TÜBİTAK BİDEB",
                "description": "Lisans öğrencilerine Ar-Ge projelerinde araştırmacı burs desteği.",
                "requirements": "Python, Veri Analizi, SQL, Araştırma, 2. sınıf ve üzeri",
                "min_grade_level": 2,
                "location": "Ankara / Üniversiteler",
                "deadline": (today + timedelta(days=2)).isoformat(),  # ACİL
                "link": "https://tubitak.gov.tr/tr/burslar/lisans/burs-programlari",
                "tags": "Python, SQL, Veri Analizi, Lisans, Ar-Ge"
            },
            {
                "title": "Baykar Yaz Gençlik Staj Programı (Aday Mühendislik)",
                "category": "Staj",
                "organization": "Baykar Teknoloji",
                "description": "Milli Teknoloji Hamlesi kapsamında Otonom Sistemler ve Yazılım birimlerinde staj.",
                "requirements": "C++, Python, Linux, OOP, Veri Yapıları",
                "min_grade_level": 2,
                "location": "İstanbul (Özdemir Bayraktar Milli Teknoloji Merkezi)",
                "deadline": (today + timedelta(days=18)).isoformat(),
                "link": "https://kariyer.baykartech.com/",
                "tags": "Python, C++, Linux, Staj, Lisans"
            },
            {
                "title": "Akbank Gençlik Akademisi Veri Analitiği Bursu",
                "category": "Burs",
                "organization": "Akbank & Kodluyoruz",
                "description": "Veri analitiği eğitimi içeren burs ve mentörlük programı.",
                "requirements": "SQL, Python, Excel, PowerBI, Problem Çözme",
                "min_grade_level": 1,
                "location": "Çevrim içi",
                "deadline": (today + timedelta(days=5)).isoformat(),  # YAKLAŞIYOR
                "link": "https://kodluyoruz.org/bootcamp",
                "tags": "SQL, Python, Burs, Veri Analitiği, Lise, Lisans"
            },
            {
                "title": "Havelsan Siber Güvenlik Uzmanlık Kampı",
                "category": "Staj",
                "organization": "HAVELSAN",
                "description": "Ağ güvenliği, sızma testleri ve zararlı yazılım analizi eğitimi.",
                "requirements": "Linux, Ağ Temelleri, Python, Siber Güvenlik, Bash",
                "min_grade_level": 2,
                "location": "Ankara",
                "deadline": (today + timedelta(days=25)).isoformat(),
                "link": "https://www.havelsan.com.tr/kariyer",
                "tags": "Linux, Siber Güvenlik, Python, Staj"
            },
            {
                "title": "Google Developer Student Clubs (GDSC) Proje Destek Çağrısı",
                "category": "Akademik",
                "organization": "Google for Developers",
                "description": "Açık kaynak yazılım projelerine mentörlük ve cloud kredisi desteği.",
                "requirements": "Web Geliştirme, JavaScript, React, Firebase, Git",
                "min_grade_level": 1,
                "location": "Çevrim içi",
                "deadline": (today + timedelta(days=1)).isoformat(),  # ÇOK ACİL
                "link": "https://developers.google.com/community/gdsc",
                "tags": "JavaScript, React, Open Source, Lise, Lisans"
            }
        ]
        return mock_opportunities

    def seed_database(self) -> int:
        self.db.clear_opportunities()
        mock_data = self.generate_mock_data()
        
        count = 0
        for opp in mock_data:
            self.db.add_opportunity(
                title=opp["title"],
                category=opp["category"],
                organization=opp["organization"],
                description=opp["description"],
                requirements=opp["requirements"],
                min_grade_level=opp["min_grade_level"],
                location=opp["location"],
                deadline=opp["deadline"],
                link=opp["link"],
                tags=opp.get("tags", "")
            )
            count += 1
            
        return count


if __name__ == "__main__":
    db = DatabaseManager()
    scraper = ScraperModule(db)
    inserted = scraper.seed_database()
    print(f" {inserted} adet örnek veritabanına yüklendi.")
