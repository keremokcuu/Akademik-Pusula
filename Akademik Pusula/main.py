"""
main.py - FırsatPusulası CLI Menüsü ve Ana Akış Kontrolü (MVP)
"""

import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from database import DatabaseManager
from scraper import ScraperModule
from matcher import ProfileMatcher, OpportunityMatcher
from notifier import OpportunityNotifier, NotificationManager

def print_header():
    print("=" * 65)
    print(" 🧭  F İ R S A T  P U S U L A S I  (v1.2 MVP)  🧭")
    print("     Staj, Burs, TEKNOFEST ve Akademik Çağrı Takip Platformu")
    print("=" * 65)

def run_cli():
    print_header()
    db = DatabaseManager()
    scraper = ScraperModule(db)
    matcher = ProfileMatcher(db)
    notifier = OpportunityNotifier(db)

    # Veritabanı boşsa varsayılan verileri yükle
    if len(db.get_all_opportunities_dict()) == 0:
        print("ℹ️ Veritabanı boş. Örnek test verileri yükleniyor...")
        scraper.seed_database()

    all_opps = db.get_all_opportunities_dict()
    print(f"\n [BILGI] Sistemde toplam {len(all_opps)} fırsat kayıtlı.")
    
    urgents = notifier.get_urgent_opportunities(days_left=7)
    if urgents:
        print(f" 🚨 [UYARI] Son 7 gün içinde başvuru süresi dolacak {len(urgents)} acil fırsat var!\n")
        for u in urgents:
            print(f"   - ⚠️ {u.title} ({u.category}) -> Son Gün: {u.deadline}")

    print("\n💡 İpucu: Web arayüzünü başlatmak için şu komutu çalıştırabilirsiniz:")
    print("   streamlit run app.py\n")

if __name__ == "__main__":
    run_cli()
