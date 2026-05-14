# anthropics/skills — Anthropic'in Resmi Skill Koleksiyonu

Anthropic'in geliştirdiği ve yönettiği resmi skill örnekleri. Claude'un skill sistemini demonstrasyon ve referans amaçlı kullanır. Birçoğu açık kaynak (Apache 2.0), bazıları (docx, pdf, pptx, xlsx) kaynak-açık ama açık kaynak değil.

## Skill Nedir?

Klasör bazlı talimat paketi — `SKILL.md` dosyası içerir. Claude bir görevi yaparken alakalı skill'i dinamik olarak yükler (progressive disclosure: metadata → talimatlar → kaynaklar).

## Kurulum

```bash
# Claude Code'da marketplace olarak ekle
/plugin marketplace add anthropics/skills

# Sonra seç ve kur:
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

**Claude.ai:** Ücretli planlarda tüm example skill'ler zaten mevcut (Settings > Capabilities).

## Skill Kategorileri

### 📄 Doküman Skill'leri (production'da aktif)
- **docx** — Word dosyası oluşturma/düzenleme, tracked changes, format koruma
- **pdf** — PDF metin/tablo çıkarma, birleştirme/bölme, form işleme
- **pptx** — PowerPoint slayt oluşturma/düzenleme, şablonlar, grafikler
- **xlsx** — Excel tablo oluşturma/düzenleme, formüller, veri analizi

### 🎨 Yaratıcı Tasarım
- **algorithmic-art** — p5.js ile generative art (flow fields, particle systems)
- **canvas-design** — .png ve .pdf formatında görsel tasarım
- **slack-gif-creator** — Slack için optimized animated GIF

### 💻 Geliştirme
- **frontend-design** — "AI slop" önleme, React + Tailwind için bold tasarım kararları
- **web-artifacts-builder** — Claude.ai artifact'larında React/Tailwind/shadcn
- **mcp-builder** — Yüksek kaliteli MCP server oluşturma rehberi
- **webapp-testing** — Playwright ile yerel web uygulama testi

### 📢 İletişim
- **brand-guidelines** — Anthropic marka renkleri ve tipografisi
- **internal-comms** — Status report, newsletter, FAQ yazımı

### 🛠️ Skill Oluşturma
- **skill-creator** — İnteraktif Q&A ile yeni skill oluşturma rehberi

## Kendi Skill'ini Yazmak

```markdown
---
name: my-skill
description: Ne zaman devreye girmeli (keşif için kritik)
---

# Talimatlar buraya

## Örnekler
- Örnek 1
- Örnek 2
```

Gerekli alan: sadece `name` ve `description`.

**Kaynak:** [anthropics/skills](https://github.com/anthropics/skills) · Apache 2.0 + source-available
