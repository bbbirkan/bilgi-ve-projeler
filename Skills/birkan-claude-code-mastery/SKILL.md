---
name: claude-code-mastery
description: "Claude Code ileri düzey kullanım teknikleri: Ücretsiz OpenRouter kurulumu, Agent Teams (Ajan Takımları) yönetimi, vibecoding best practice'leri ve 5 seviyeli otomasyon (Routines) mimarisi."
---
# Claude Code Mastery (İleri Düzey Orkestrasyon ve Otomasyon)

Bu skill, Claude Code'u standart bir sohbet asistanından çıkarıp otonom bir proje yöneticisine, kodlayıcıya ve görev otomatikleştiriciye dönüştürmek için gereken "gizli" ve ileri düzey teknikleri içerir. Bu bilgiler, alanındaki uzmanların (Simon Scrapes, Brad Bonanno, Hasan, Selma vb.) anlattığı metodolojilerden derlenmiştir.

## 🌟 1. Claude Code'u Ücretsiz Kullanma (OpenRouter + Local Settings)
Claude API maliyetlerini sıfırlamak ve projelerinizi ücretsiz modellerle geliştirmek için şu adımları izleyin:

1. Projenizin kök dizininde `.claude` adında bir klasör oluşturun.
2. İçine `settings.json.local` adında bir dosya açın.
3. Aşağıdaki konfigürasyonu yapıştırın:
   ```json
   {
     "primaryModel": "minimax/minimax-free",
     "apiBaseUrl": "https://openrouter.ai/api/v1",
     "apiKey": "sk-or-v1-YOUR_OPENROUTER_API_KEY"
   }
   ```
4. OpenRouter'dan ücretsiz bir API anahtarı alın ve `apiKey` kısmına yazın. Arama kısmına "free" yazarak Nvidia veya MiniMax gibi ücretsiz modelleri kullanıp limitsiz kod yazdırabilirsiniz.

## 🤖 2. Sub-Agents vs. Agent Teams (Deneysel Özellik)
Büyük projelerde "Context Limit" (bağlam sınırı) dolmasını önlemek için ajanlar kullanılır. Ancak eski "Sub-Agent" (Alt Ajan) modeli bir darboğaz (bottleneck) yaratır çünkü ajanlar birbirleriyle konuşamaz, sadece ana Claude'a rapor verirler.

**Agent Teams (Ajan Takımları) Nasıl Açılır ve Kullanılır?**
Agent takımları, ortak bir görev listesi (shared task list) üzerinden birbirleriyle iletişim kurabilen otonom ajanlardan oluşur (Örn: Frontend ajanı, backend ajanıyla uyumu kontrol eder).

1. Global veya lokal `settings.json` dosyanızda şu ayarı aktif edin:
   ```json
   {
     "claudeCodeExperimentalAgentTeams": true
   }
   ```
2. Güncellemeyi yapın: `claude update`
3. Terminalde `claude --dangerously-skip-permissions` ile çalıştırarak ajanların her dosya değişiminde sizden onay beklemesini (yavaşlatmasını) engelleyin.
4. "Create an agent team to..." diyerek taskınızı verin. Ajanlar arası manuel geçiş yapmak ve spesifik bir ajana direkt komut vermek için terminalde `Shift + Yukarı/Aşağı` ok tuşlarını kullanabilirsiniz. (tmux kullanıyorsanız ajanları farklı sekmelerde de izleyebilirsiniz).

## ⚙️ 3. Claude Otomasyonunun 5 Seviyesi (Brad's Framework)
İş akışlarınızı otomatize ederken doğru aracı seçmek kritik öneme sahiptir. Neyi, nerede otomatize etmelisiniz?

- **Seviye 1: Skills (Yetenekler)** - Sık tekrarlanan promptları `SKILL.md` olarak kaydetmek (Şu an okuduğunuz belge gibi). Kendi tetiklediğiniz rutin işler içindir.
- **Seviye 2: Desktop Routines (Masaüstü Rutinleri)** - Sadece sizin bilgisayarınızda, bilgisayar açıkken çalışan rutinler. (Örn: Her sabah 9'da lokal Chrome'u açıp LinkedIn'den mesaj atma).
- **Seviye 3: Scheduled Cloud Routines (Zamanlanmış Bulut Rutinleri)** - Anthropic sunucularında çalışan, bilgisayarınız kapalı olsa bile çalışan zamanlı rutinler. Bilgileri GitHub reposundan (Context) ve API'lerden (Slack, FireCrawl) alır.
- **Seviye 4: API Cloud Routines (Webhook / Event-Driven)** - Bir olay gerçekleştiğinde anında tetiklenen bulut rutinleri. (Örn: Fireflies toplantı bitirince webhook atar, Claude transkripti okuyup GitHub'a not alır ve Slack'e özet geçer). *Önemli Uyarı: Anthropic özel header'lar istediği için araya n8n veya Make.com gibi bir middleware koyarak gelen webhook'u Claude'un anlayacağı şekle sokmanız gerekebilir.*
- **Seviye 5: Managed Agents (Yönetilen Ajanlar)** - Kendi ürettiğiniz bir uygulamanın (SaaS vb.) içine Claude altyapısını gömmek istediğinizde kullanılır. Platform API'sidir, kişisel işlerinizi otomatize etmek için fazla karmaşıktır.

*(Not: Düz ve karar gerektirmeyen veri aktarım işlemleri için n8n/Make kullanmaya devam edin. Claude'u sadece muhakeme, yazarlık ve karar verme gerektiren süreçlerde otomasyona dahil edin.)*

## 🚀 4. Vibecoding Best Practices (Hatadan Kaçınma Kuralları)
1. **Modüler Dosya Yapısı:** Asla tüm kodları devasa bir dosyaya yığmayın. Dosyaları 600 satırın altında, küçük ve odaklı tutun. Aksi halde LLM'ler "halüsinasyon" görmeye başlar ve çalışan yeri de bozar.
2. **Kavramları ve Temelleri Bilin:** Claude'un mimari bir sorunu çözebilmesi için o sorunu ona sizin tanımlayabilmeniz gerekir (Örn: "Race condition oluşmasını engelle" demezseniz, aynı anda veri kaydeden iki kullanıcının birbirini ezmesini engelleyemez). Sadece fikir vermek yetmez, sistemi bilmek zorundasınız.
3. **Her Oturumda Tek Görev (One Task Per Session):** Önce projenin en başına bir `plan.md` veya `product.md` yapın. Görevleri böldükten sonra her oturumda (session) tek bir özelliği bitirmesini isteyin. Özellik çalışıyorsa test edin ve **anında GitHub'a commit'leyin (pushlayın)**. Eğer bir sonraki oturumda yapay zeka projeyi bozarsa, saatlerce hatayı çözmek yerine tek tuşla geri sarabilirsiniz (rewind).
