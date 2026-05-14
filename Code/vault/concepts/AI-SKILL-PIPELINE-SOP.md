---
name: ai-skill-pipeline-sop
description: Kullanıcıdan (Birkan) gelen ham metin, makale veya GitHub linklerini otomatik olarak işleyip 3 farklı sisteme skill olarak entegre eden Standart Operasyon Prosedürü.
tags: [sop, workflow, automation, skill-creation]
---

# 🤖 AI Skill Creation & Integration Pipeline (SOP)

**DİKKAT (SİSTEM KURALI):** Yapay zeka ajanı, kullanıcıdan (Birkan) yeni bir bilgi, araştırma metni veya GitHub linki aldığında; kullanıcıya tek tek "ne yapayım?" diye sormadan aşağıdaki **4 adımlı otonom süreci** KESİNLİKLE çalıştırmakla yükümlüdür.

## 🔄 Adım 1: Analiz ve Zenginleştirme
- Metin veya GitHub reposu okunur. 
- Sadece yüzeysel bir özet çıkarılmaz; çalışma mantığı, mimarisi, Tufte/UX prensipleri veya performans kuralları çıkarılır.
- Varsa araçların (PyGWalker, Crawl4AI vb.) kod detayları ve parametreleri belirlenir.
- Gelişmiş bir komut (Prompt) ve RCI (`<thinking>`) döngüsü kurgulanır.

## 💾 Adım 2: Otonom 3'lü Kayıt Sistemi
Ajan, oluşturduğu Markdown formatındaki mükemmel Skill dosyasını kullanıcıya sormadan KESİNLİKLE şu **3 konuma eşzamanlı olarak** yazar:
1. **Ana SkillSeekers Sistemi:** `/Users/birkan/Documents/HariciAraclar/SkillSeekers/output/{skill-adi}/SKILL.md`
2. **Obsidian Vault (Graphify için):** `/Users/birkan/Desktop/Work /00 Github PROJELERI/vault/concepts/{skill-adi}.md`
3. **Masaüstü (Hızlı Erişim):** `/Users/birkan/Desktop/{skill-adi}-skill.md`

## 📦 Adım 3: Bağımlılık (Dependency) Tespiti ve Kurulumu
- Skill içinde geçen Python paketleri (`pip`) veya Node paketleri (`npm`) tespit edilir.
- Terminal üzerinden kurulum komutu (Mac ortamı için gerekirse `--break-system-packages` argümanı hazırda tutularak) otonom veya tek bir onay ile çalıştırılır.

## ✅ Adım 4: Kullanıcıya Rapor
Süreç tamamlandıktan sonra kullanıcıya sadece: *"Bilgiyi aldım, 3 konuma kaydettim ve gerekli kütüphaneleri kurdum. Hazırız."* şeklinde kısa bir özet geçilir. Kullanıcı yorulmaz.
