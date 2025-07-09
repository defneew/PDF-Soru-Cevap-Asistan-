# 📄 PDF Soru-Cevap Asistanı (LLM Destekli)

Küçük ama etkili bir yapay zekâ uygulaması!  
PDF dosyasını yükle, sorunu sor, Gemini ile hızlıca yanıt al.  
Bu proje Flask ve Gemini 1.5 Flash LLM modeli ile geliştirilmiştir.

---

## 🚀 Özellikler

- ✅ Kullanıcıdan PDF ve soru alma
- 🤖 Gemini 1.5 Flash ile içerik anlama ve soru yanıtlama
- 📜 PyMuPDF ile PDF metni çıkarımı
- 💡 Basit ama şık Bootstrap arayüz
- 🔐 .env dosyası ile güvenli API anahtarı yönetimi

---

## 🛠️ Kurulum
1. `pip install -r requirements.txt`
2. .env dosyası oluştur ve API anahtarını ekle: GEMINI_API_KEY=your_api_key_here
3. `python app.py` ile başlat
