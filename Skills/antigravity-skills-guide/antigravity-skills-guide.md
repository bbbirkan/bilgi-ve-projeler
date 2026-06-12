# Antigravity Agent Skills Guide

Google Antigravity platformunda ajanların yeteneklerini genişletmek için kullanılan açık standartlı beceri (skill) oluşturma rehberi.

## Skill Nedir?
Ajanın belirli görevleri nasıl yapacağını anlatan yeniden kullanılabilir bilgi paketleridir. Bir skill şunları içerir:
- Görev yaklaşımı için spesifik talimatlar
- En iyi pratikler ve kurallar (conventions)
- İsteğe bağlı yardımcı scriptler ve kaynaklar

## Konumlar (Scope)
Antigravity iki tür skill dizini destekler (Eski `.agent/skills` yerine artık `.agents/skills` varsayılandır):
1. **Workspace-specific:** `<workspace-root>/.agents/skills/<skill-folder>/` (Projeye veya takıma özel iş akışları)
2. **Global:** `~/.gemini/config/skills/<skill-folder>/` (Tüm projelerde geçerli genel araçlar)

## Oluşturma Adımları
Her skill klasörü içinde bir `SKILL.md` dosyası barındırmak zorundadır. Bu dosyanın en üstünde YAML frontmatter bulunmalıdır:

```yaml
---
name: my-skill
description: Belirli bir görevi yapar. X veya Y gerektiğinde kullanın.
---

# My Skill
Detaylı talimatlar...
```

### Frontmatter Alanları
- `name` (Opsiyonel): Skill için benzersiz isim (boşluksuz, tire ile). Verilmezse klasör adı kullanılır.
- `description` (Zorunlu): Ajanın skill'i ne zaman kullanacağını anlaması için net bir açıklama. **Tavsiye:** 3. şahıs ağzından yazın ve ajanın eşleştirebileceği tetikleyici anahtar kelimeler ekleyin.

## Skill Klasör Yapısı (Opsiyonel)
```text
.agents/skills/my-skill/
├── SKILL.md       # Ana talimatlar (Zorunlu)
├── scripts/       # Yardımcı scriptler (Opsiyonel)
├── examples/      # Referans implementasyonlar (Opsiyonel)
└── resources/     # Şablonlar ve diğer varlıklar (Opsiyonel)
```

## En İyi Pratikler
- **Odaklı Olun:** Her skill tek bir işi iyi yapmalı. "Her şeyi yapan" bir skill yerine ayrı ayrı skill'ler oluşturun.
- **Net Açıklamalar (Description):** Ajanın bu skill'i seçmesi tamamen `description` alanındaki kelimelere bağlıdır.
- **Scriptleri Kara Kutu (Black Box) Gibi Kullanın:** Ajanın uzun script kodlarını okuması yerine, script'i `--help` flag'i ile çalıştırmasını öğütleyin.
- **Karar Ağaçları:** Karmaşık yetenekler için ajanın duruma göre yol seçebileceği karar ağaçları (decision trees) ekleyin.
