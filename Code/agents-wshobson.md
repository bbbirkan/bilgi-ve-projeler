# agents (wshobson)

En kapsamlı Claude Code agent + skill + plugin koleksiyonu. 184 özelleşmiş agent, 150 skill, 78 plugin, 16 çok-ajanlı orchestrator ve 98 komut. Smithery marketplacei üzerinden direkt kurulabilir.

**Smithery:** https://smithery.ai/skills?ns=wshobson

## Ne İçerir

| Kategori | Sayı | Açıklama |
|----------|------|----------|
| Plugin | 78 | Granüler, tek-amaçlı plugin'lar |
| Agent | 184 | Domain expert'ler |
| Skill | 150 | Modüler bilgi paketleri |
| Orchestrator | 16 | Çok-ajanlı iş akışları |
| Komut | 98 | Slash commands |

## Nasıl Kurulur

```bash
# Marketplace'i ekle (tek seferlik)
/plugin marketplace add wshobson/agents

# İstediğin plugin'ları kur
/plugin install python-development
/plugin install kubernetes-operations
/plugin install full-stack-orchestration
/plugin install comprehensive-review
```

## 3 Katmanlı Model Stratejisi

| Tier | Model | Kullanım alanı |
|------|-------|----------------|
| Tier 1 | Opus 4.7 | Mimari kararlar, güvenlik, kod review |
| Tier 2 | Inherit | Frontend/mobile, AI/ML (sen seçersin) |
| Tier 3 | Sonnet | Destek görevleri, test, debug |
| Tier 4 | Haiku | Hızlı: SEO, deploy, basit dokümantasyon |

## 25 Kategori Özeti

🎨 Development · 📚 Documentation · 🔄 Workflows · ✅ Testing · 🔍 Quality  
🤖 AI & ML · 📊 Data · 🗄️ Database · 🚨 Operations · ⚡ Performance  
☁️ Infrastructure · 🔒 Security · 🛡️ Governance · 💻 Languages (10 dil)  
🔗 Blockchain · 💰 Finance · 💳 Payments · 🎮 Gaming · ♿ Accessibility  
📢 Marketing · 💼 Business · 🔌 API · 🛠️ Utilities · 🔧 Modernization

## Öne Çıkan Plugin'lar

- **Conductor** — Context → Spec → Implement iş akışı yönetimi
- **Agent Teams** — 7 preset'li paralel team orchestration (`/team-review`, `/team-debug`)
- **PluginEval** — Skill kalitesi için 3 katmanlı değerlendirme sistemi (Platinum/Gold/Silver/Bronze)
- **protect-mcp** — Cedar policy enforcement + Ed25519 imzalı kayıtlar

## Neden Bu Repo

- Her plugin sadece kendi component'larını yükler → minimal token kullanımı
- 184 agent'ın tamamı 25 kategoride erişilebilir
- Smithery marketplacei üzerinden plug-and-play

**Kaynak:** [wshobson/agents](https://github.com/wshobson/agents) · MIT
