# awesome-claude-skills (travisvn)

Claude skill ekosisteminin en kapsamlı meta-listesi. Resmi Anthropic skill'lerinden partner skill'lerine, topluluk katkılarına ve güvenlik uyarılarına kadar her şeyi belgeler.

## Ne İşe Yarar

Claude skill'leri hakkında araştırma ve referans kaynağı. Ne bulacaksın, nasıl kurarsın, nasıl yazarsın, güvenlik riskleri neler — hepsini açıklar.

## Skill Nasıl Çalışır (3 Katmanlı Progressive Disclosure)

```
1. Metadata    (~100 token)  → Her zaman yüklü, keşif için
2. Talimatlar  (<5k token)   → Skill aktive olunca yüklenir
3. Kaynaklar   (değişken)    → Sadece gerektiğinde
```

Bu mimari sayesinde birden fazla skill eş zamanlı hazır tutulabilir, context dolmaz.

## Kurulum Yolları

```bash
# Claude Code
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills

# API
import anthropic  # /v1/skills endpoint

# Claude.ai → Settings > Capabilities > Skills
```

## Öne Çıkan Skill'ler

### Resmi (anthropics/skills)
- **docx / pdf / pptx / xlsx** — Doküman oluşturma/düzenleme (production'da aktif)
- **mcp-builder** — MCP server oluşturma rehberi
- **webapp-testing** — Playwright ile test
- **frontend-design** — "AI slop" önleme
- **skill-creator** — Yeni skill oluşturma asistanı

### Topluluk
- **obra/superpowers** — 20+ battle-tested skill; TDD, debug, `/brainstorm`, `/write-plan`
- **Trail of Bits Security Skills** — CodeQL/Semgrep statik analiz, güvenlik audit
- **shadcn/ui** — shadcn component context + pattern enforcement
- **Expo Skills** — Resmi Expo/React Native skill'leri
- **loki-mode** — 37 agent, 6 swarm → startup'ı sıfırdan deploy et
- **ios-simulator-skill** — iOS uygulama build ve test otomasyonu
- **playwright-skill** — Browser otomasyonu
- **yusufkaraaslan/Skill_Seekers** — Dokümantasyon sitesini Claude skill'ine çevir

## Ne Zaman Ne Kullan

| Araç | En iyi kullanım |
|------|----------------|
| **Skill** | Tekrarlayan prosedürel bilgi, taşınabilir |
| **Subagent** | Bağımsız görev, kısıtlı tool erişimi |
| **MCP** | Harici veri/API entegrasyonu |
| **Project** | Kalıcı arka plan bilgisi (workspace içi) |
| **Prompt** | Tek seferlik talimat |

**Altın kural:** Aynı prompt'u defalarca yazıyorsan → Skill yap.

## Skill vs MCP Karşılaştırması

| | Skill | MCP |
|--|-------|-----|
| Amaç | Görev uzmanlığı, iş akışı | Harici veri/API |
| Taşınabilirlik | Claude.ai, Code, API — aynı format | Server konfigürasyonu gerekir |
| Token | 30-50 başlangıç, <5k aktifken | Değişken |
| İdeal | Tekrarlayan görevler, doküman | DB erişimi, API entegrasyonu |

**İkisi birlikte:** `mcp-builder` skill, MCP server oluşturmanı sağlar.

## Güvenlik Uyarısı

Skill'ler ortamında keyfi kod çalıştırabilir. Kurulmadan önce SKILL.md ve script'leri incele. Güvenilir kaynaklardan yükle.

**Kaynak:** [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
