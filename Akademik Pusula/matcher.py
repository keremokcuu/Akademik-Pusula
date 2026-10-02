"""
matcher.py - FırsatPusulası Profil Eşleştirme Modülü
"""

import sys
from typing import List, Dict, Any, Tuple
from database import DatabaseManager

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class MatchTuple(tuple):
    """
    Streamlit app.py 'for title, cat, deadline, score in matches' döngüsü ile 
    %100 geriye dönük uyumlu ve aynı zamanda zengin nitelikler içeren özel tuple sınıfı.
    """
    def __new__(cls, title: str, category: str, deadline: str, score: float, 
                organization: str = "", link: str = "#", tags: str = "", reasons: List[str] = None):
        obj = super().__new__(cls, (title, category, deadline, score))
        obj.title = title
        obj.category = category
        obj.deadline = deadline
        obj.score = score
        obj.organization = organization
        obj.link = link
        obj.tags = tags
        obj.reasons = reasons or []
        return obj


class ProfileMatcher:
    """Kullanıcı etiketleri ile veritabanındaki fırsat etiketlerini kıyaslayan eşleştirici."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def match_user_profile(self, user_tags: List[str]) -> List[MatchTuple]:
        """
        Kullanıcının girdiği etiket kümesi ile fırsat etiketlerini ve alanlarını eşleştirir.
        Döndürür: List[MatchTuple(title, category, deadline, score)]
        """
        if not user_tags:
            return []
            
        clean_user_tags = [t.strip().lower() for t in user_tags if t.strip()]
        if not clean_user_tags:
            return []

        all_opps = self.db.get_all_opportunities_dict()
        results = []

        for opp in all_opps:
            opp_tags = [t.strip().lower() for t in opp.get("tags", "").split(",") if t.strip()]
            req_text = opp.get("requirements", "").lower()
            title_text = opp.get("title", "").lower()
            desc_text = opp.get("description", "").lower()
            
            matched_tags = []
            reasons = []

            for u_tag in clean_user_tags:
                if u_tag in opp_tags or u_tag in req_text or u_tag in title_text or u_tag in desc_text:
                    matched_tags.append(u_tag.title())

            if matched_tags:
                # Eşleşme skoru hesaplama
                match_ratio = len(matched_tags) / len(clean_user_tags)
                score = round(min(100.0, match_ratio * 100.0), 1)
                
                reasons.append(f"✓ Eşleşen etiketler: {', '.join(matched_tags)}")
                
                match_item = MatchTuple(
                    title=opp["title"],
                    category=opp["category"],
                    deadline=opp["deadline"],
                    score=score,
                    organization=opp.get("organization", "Genel"),
                    link=opp.get("link", "#"),
                    tags=opp.get("tags", ""),
                    reasons=reasons
                )
                results.append(match_item)

        # Skora göre büyükten küçüğe sırala
        results.sort(key=lambda x: x.score, reverse=True)
        return results


# CLI Uyumlu Takma İsim
OpportunityMatcher = ProfileMatcher

if __name__ == "__main__":
    db = DatabaseManager()
    matcher = ProfileMatcher(db)
    matches = matcher.match_user_profile(["Python", "Lise"])
    print(f" Bulunan eşleşme sayısı: {len(matches)}")
    for title, cat, deadline, score in matches:
        print(f" - [{cat}] {title} (Son Tarih: {deadline}) -> %{score} Uyum")
