"""
notifier.py - Son Başvuru Tarihi Uyarı Modülü
"""

import sys
from datetime import datetime, date
from typing import List, Dict, Any, Tuple
from database import DatabaseManager

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class UrgentTuple(tuple):
    """
    Streamlit app.py 'for title, cat, deadline in urgent_items' döngüsü ile
    %100 geriye dönük uyumlu ve aynı zamanda zengin nitelikler içeren özel tuple sınıfı.
    """
    def __new__(cls, title: str, category: str, deadline: str, 
                organization: str = "", link: str = "#", remaining_days: int = 0):
        obj = super().__new__(cls, (title, category, deadline))
        obj.title = title
        obj.category = category
        obj.deadline = deadline
        obj.organization = organization
        obj.link = link
        obj.remaining_days = remaining_days
        return obj


class OpportunityNotifier:
    """Son başvuru tarihlerini denetleyen ve aciliyet durumuna göre uyarı üreten modül."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def calculate_remaining_days(self, deadline_str: str) -> int:
        """Tarihe kalan gün sayısını hesaplar."""
        try:
            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
            today = date.today()
            return (deadline_date - today).days
        except (ValueError, TypeError):
            return 999

    def get_urgent_opportunities(self, days_left: int = 7) -> List[UrgentTuple]:
        """
        Son başvuru tarihine belirtilen gün sayısından az kalan acil fırsatları getirir.
        Döndürür: List[UrgentTuple(title, category, deadline)]
        """
        all_opps = self.db.get_all_opportunities_dict()
        urgent_list = []

        for opp in all_opps:
            rem_days = self.calculate_remaining_days(opp.get("deadline", ""))
            if 0 <= rem_days <= days_left:
                urgent_item = UrgentTuple(
                    title=opp["title"],
                    category=opp["category"],
                    deadline=opp["deadline"],
                    organization=opp.get("organization", "Genel"),
                    link=opp.get("link", "#"),
                    remaining_days=rem_days
                )
                urgent_list.append(urgent_item)

        urgent_list.sort(key=lambda x: x.remaining_days)
        return urgent_list


# CLI Uyumlu Takma İsim
NotificationManager = OpportunityNotifier

if __name__ == "__main__":
    db = DatabaseManager()
    notifier = OpportunityNotifier(db)
    urgents = notifier.get_urgent_opportunities(7)
    print(f" Acil fırsat sayısı: {len(urgents)}")
    for title, cat, deadline in urgents:
        print(f" ⚠️ {title} ({cat}) - Son gün: {deadline}")
