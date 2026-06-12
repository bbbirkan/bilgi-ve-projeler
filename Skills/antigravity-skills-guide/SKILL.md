---
name: antigravity-skills-guide
description: Creates, structures, and documents new skills for Google Antigravity agents according to official guidelines. Use when writing a new skill, setting up a SKILL.md file, or advising on skill architecture.
---

# Antigravity Skills Guide

Google Antigravity platformu için yeni bir skill (yetenek) yazarken, kurgularken veya düzenlerken bu rehberi kullan. Ajan yetenekleri "Progressive Disclosure" (Kademeli Açıklama) prensibiyle çalışır: Discovery (Keşif) -> Activation (Aktifleştirme) -> Execution (Çalıştırma).

## Dizin Kuralları
- **Global Skill:** `~/.gemini/config/skills/<skill-folder>/`
- **Workspace Skill:** `<workspace-root>/.agents/skills/<skill-folder>/` (Not: Eski `.agent` yerine `.agents` tercih edilmelidir)
- Birkan'ın özel kurallarına (GEMINI.md) göre global skill'ler `~/.gemini/config/plugins/birkan-skills/skills/` dizininde de senkronize edilebilir.

## SKILL.md Yazım Kuralları
1. **YAML Frontmatter Zorunludur:**
   ```yaml
   ---
   name: my-skill
   description: 3. şahıs ağzından, ajanın ne zaman kullanacağını anlaması için tetikleyici kelimeler barındıran açıklama.
   ---
   ```
2. **Odak:** "Her şeyi yapan" agent'lar yerine, tek bir göreve odaklanan (örneğin sadece Code Review yapan) ayrık skill'ler tasarla.
3. **Script Kullanımı:** Eğer skill `scripts/` klasöründe yardımcı script barındırıyorsa, ajana kodu okumasını değil, direkt `python scripts/tool.py --help` şeklinde çalıştırmasını söyle (Black Box prensibi).
4. **Karar Ağaçları (Decision Trees):** Birden fazla yol varsa, "Durum A ise bunu yap, Durum B ise şunu yap" şeklinde bir Decision Tree ekle.
