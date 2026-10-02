# 🎯 FırsatPusulası — Geliştirme Yol Haritası (Roadmap)

> **Hedef Kitle:** Bilişim ve Mühendislik Öğrencileri (Lisans / Lise / Ön Lisans)  
> **Amaç:** Staj, burs, TEKNOFEST ve akademik bildiri/çağrı fırsatlarını tek merkezde toplayıp kişiselleştirilmiş bildirim ve eşleştirme sunmak.

---

## 📌 Faz 1: Temel Mimari & Streamlit MVP (Tamamlandı ✅)
- [x] Modüler proje yapısının kurulması (`main.py`, `database.py`, `scraper.py`, `matcher.py`, `notifier.py`, `app.py`).
- [x] SQLite veritabanı şemasının (`opportunities`, `user_profiles`) tasarlanması.
- [x] Örnek test verisi yükleme mekanizması (Mock Scraper).
- [x] Kullanıcı yetenek/etiketlerine göre eşleştirme algoritması (ProfileMatcher MVP).
- [x] Son başvuru tarihlerini izleyen acil bildirim modülü (OpportunityNotifier MVP).
- [x] Streamlit tabanlı modern ve şık web arayüzü (`app.py`).

---

## 🚀 Faz 2: Otomatik Veri Toplama & Web Scraping (Gelecek Aşama)
- [ ] **Kariyer & Staj Platformları:** Youthall, Kariyer.net, Linkedin API/Scraper entegrasyonu.
- [ ] **Yarışmalar:** TEKNOFEST, Hackathon.fi, Kaggle yarışma duyurularının takibi.
- [ ] **Akademik & Burs:** TÜBİTAK (BİDEB/STAR), Gençlik ve Spor Bakanlığı burs duyuruları.
- [ ] **Veri Temizleme & Tekilleştirme:** Çifte kayıtları engellemek için başlık/kurum hashing mekanizması.

---

## 🧠 Faz 3: Akıllı Eşleştirme & AI Entegrasyonu (2-3 Ay)
- [ ] **Vektör Arama & TF-IDF / NLP:** İlan gereksinimleri ile öğrenci özgeçmiş metinlerinin doğal dil işleme ile kıyaslanması.
- [ ] **Etiketleme Sistemi:** `#YapayZeka`, `#SiberGüvenlik`, `#WebGeliştirme`, `#Donanım` gibi etiketlerle otomatik sınıflandırma.

---

## 🔔 Faz 4: Bildirim & İletişim Kanalları (3-4 Ay)
- [ ] **Telegram Bot Entegrasyonu:** Günlük/haftalık kişiselleştirilmiş fırsat özeti mesajları.
- [ ] **E-Posta Bülteni (SMTP / SendGrid):** Kullanıcının ilgi alanlarına özel haftalık e-posta.
