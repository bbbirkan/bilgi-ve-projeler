# Skills Index — Typed Relationship Graph
<!-- SkillDeck ilkesiyle: her skill'in depends_on / conflicts_with / composes_with ilişkileri -->
<!-- Claude bu index'i okuyarak hangi skill'i seçeceğine karar verir -->
<!-- Son güncelleme: 2026-06-07 -->

## Kullanım Kuralı
Skill seçmeden önce bu index'i tara:
- **conflicts**: Bu skill'lerden sadece BİRİNİ kullan (benzer/çakışan)
- **composes**: Birlikte güçlü çalışır
- **specializes**: Daha spesifik versiyon — önce bu'nu dene
- **depends**: Bu skill çalışmadan önce şu kurulu olmalı

---

## 📚 ARAŞTIRMA / KNOWLEDGE

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `research` | Hızlı codebase/dosya arama | deep-research, autoresearch | — | graphify |
| `deep-research` | Derin, çok-boyutlu araştırma | research, autoresearch | research | graphify, agent-browser |
| `autoresearch` | Otomatik web araştırması | research, deep-research | research | — |
| `autonomous-deep-research` | Tam otonom uzun araştırma | deep-research | deep-research | — |
| `content-autoresearch` | İçerik odaklı araştırma | autoresearch | autoresearch | content-strategy |
| `prompt-autoresearch` | Prompt optimizasyonu araştırması | autoresearch | autoresearch | — |
| `graphify` | Kod/döküman → knowledge graph | graphify-skill | — | deep-research, code-wiki |
| `graphify-skill` | Graphify skill editörü | graphify | graphify | — |
| `knowledge-pipeline` | Bilgi akışı pipeline kurma | — | — | graphify, conductor-memory |
| `karpathy-obsidian` | Obsidian-style second brain | — | — | graphify, knowledge-pipeline |
| `ai-agent-memory-rag` | RAG vs LLM Wiki vs GBrain mimari kararı | — | — | karpathy-obsidian, knowledge-pipeline |

---

## 🤖 AJAN / ORKESTRASYONˇ

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `orchester` | 3 CLI paralel (Claude+AGY+OpenCode) | — | — | kermes |
| `agency-agents` | 80 uzman ajan havuzu | recursive-mas | — | claude-parallel |
| `recursive-mas` | Özyinelemeli çok-ajan | agency-agents | agency-agents | — |
| `claude-parallel` | Claude'u paralel çalıştır | — | — | orchester, agency-agents |
| `multi-llm-architect` | Birden fazla LLM mimarisi | — | — | orchester, claude-parallel |
| `wshobson-agents` | wshobson ajan koleksiyonu | agency-agents | — | — |
| `subagents-catalog` | Hangi subagent'ı seçmeli | — | — | agency-agents |
| `conductor__context-driven-development` | Context-driven dev workflow | — | — | conductor-memory |
| `conductor-memory` | Conductor hafıza sistemi | — | — | conductor__context-driven-development |

---

## 🌐 WEB / TARAYICI

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `agent-browser` | Web otomasyonu, form, screenshot | — | — | deep-research, guvenlik-testi |
| `web-scraping-ai` | AI destekli scraping: Crawl4AI + DeepSeek/Groq, Pydantic şema, Cloudflare bypass | agent-browser | — | agent-browser |
| `page-cro` | Landing page dönüşüm optimizasyonu | — | — | ai-seo |
| `ai-seo` | SEO analizi ve öneriler | seo-pipeline | — | page-cro, content-strategy |
| `seo-pipeline` | Tam SEO pipeline otomasyonu | ai-seo | ai-seo | — |

---

## 💻 GELİŞTİRME / KOD

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `code-wiki` | Kod tabanı wiki oluştur | graphify | — | graphify |
| `frontend-design` | Frontend UI/UX tasarım | — | — | anthropic-canvas-design |
| `backend-development__api-design-principles` | API tasarım prensipleri | — | — | backend-development__workflow-orchestration-patterns |
| `backend-development__workflow-orchestration-patterns` | Backend orkestrasyon | — | — | backend-development__api-design-principles |
| `developer-essentials__code-review-excellence` | Kod review rehberi | zen-review | — | zen-comprehensive-review |
| `developer-essentials__debugging-strategies` | Debug stratejileri | — | — | — |
| `everything-claude-code` | Claude Code tüm özellikleri | claude-code-mastery | — | — |
| `claude-code-mastery` | Claude Code ileri teknikler | everything-claude-code | everything-claude-code | — |
| `claude-code-harness` | Token tasarrufu (%90+), hook'lar, CBM kurulumu | — | agent-code-pro-tips | orchester |
| `context-engineering` | KV-Cache hizalaması, CCR (Compress-Cache-Retrieve), AST sıkıştırma, API maliyet düşürme | — | claude-code-harness | claude-code-harness |
| `n8n-automation` | n8n v2.x Native Python Runner, N8N_PYTHON_BINARY, webhook, FastAPI/Prefect orkestrasyon | — | — | backend-development__workflow-orchestration-patterns |
| `telegram-bot-python` | PTB v21.x async, ApplicationBuilder, multi-bot BotManager, webhook vs polling production | — | — | — |
| `ultrathink-developer` | Derin teknik düşünme | — | — | deep-research |
| `guvenlik-testi` | Güvenlik testi | — | — | agent-browser |
| `init` | Yeni proje CLAUDE.md oluştur | — | — | — |
| `public-apis` | Public API referansı | — | — | — |

---

## 🎯 PROJELERİM

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `kermes` | Kermes projesi strateji/lansman | — | — | orchester |
| `hermes-agent-mastery` | Hermes ajan sistemi kullanımı | — | — | orchester |
| `orchester` | Terminal orkestrasyon | — | — | kermes, hermes-agent-mastery |

---

## 🤖 AI / MODEL

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `ai-model-scout` | Yeni AI model keşfi | model-scout | — | local-llm-recommender |
| `model-scout` | Model karşılaştırma | ai-model-scout | ai-model-scout | — |
| `local-llm-recommender` | Lokal LLM öneri | — | — | ai-model-scout |
| `uncensored-model-router` | Sansürsüz model yönlendirme | — | — | multi-llm-architect |
| `novita-api-guide` | Novita AI API kullanımı | — | — | — |

---

## 🎬 VİDEO / GÖRSEL

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `claude-video` | Video analizi ve işleme | — | — | — |
| `higgsfield` | Higgsfield AI platform | — | — | higgsfield-generate |
| `higgsfield-generate` | Video üretimi | higgsfield | higgsfield | — |
| `higgsfield-marketplace-cards` | Marketplace kart üretimi | — | higgsfield | — |
| `higgsfield-product-photoshoot` | Ürün fotoğraf çekimi | — | higgsfield | — |
| `higgsfield-soul-id` | Soul ID oluşturma | — | higgsfield | — |
| `seedance-prompter` | Seedance video prompt | — | — | video-prompt-builder |
| `video-production-kit` | Tam video prodüksiyon | — | — | claude-video, seedance-prompter |
| `video-prompt-builder` | Video prompt yazma | seedance-prompter | — | video-production-kit |
| `youtube-skill-25` | YouTube 2025 stratejisi | — | — | content-strategy |

---

## ✍️ İÇERİK / YAZI

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `copywriting` | Satış odaklı metin yazımı | content-strategy | — | humanizer |
| `content-strategy` | İçerik stratejisi | copywriting | — | ai-seo |
| `humanizer` | Metni daha insancıl yap | — | — | copywriting |
| `ai-novel-architect` | Roman/kurgu yazımı | — | — | humanizer |
| `anthropic-doc-coauthoring` | Doküman co-authoring | — | — | — |
| `chatterbox` | Konuşma/chat odaklı | — | — | humanizer |

---

## 📊 OFİS / DÖKÜMAN

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `zen-office-docx` | Word döküman işleme | — | — | — |
| `zen-office-pdf` | PDF işleme | — | — | — |
| `zen-office-pptx` | PowerPoint işleme | — | — | — |
| `zen-office-xlsx` | Excel işleme | — | — | zen-office-pdf |

---

## 🔍 REVIEW / KALİTE

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `zen-review` | Kod/içerik review | developer-essentials__code-review-excellence | — | zen-comprehensive-review |
| `zen-comprehensive-review` | Kapsamlı review | — | zen-review | cross-review |
| `zen-discovery` | Proje keşfi | research | — | graphify |
| `cross-review` | Çapraz review | — | — | zen-comprehensive-review |

---

## 🛠️ SKILL META / MCP

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `skill-creator` | Yeni skill oluştur | anthropic-skill-creator | — | — |
| `anthropic-skill-creator` | Anthropic formatında skill | skill-creator | skill-creator | — |
| `claude-skills-catalog` | Tüm Claude skill'lerini listele | — | — | — |
| `ai-skill-pipeline` | Skill pipeline otomasyonu | — | — | skill-creator |
| `mcp-catalog` | MCP server kataloğu | mcp-servers-guide | — | — |
| `mcp-servers-guide` | MCP kurulum rehberi | mcp-catalog | mcp-catalog | anthropic-mcp-builder |
| `anthropic-mcp-builder` | MCP server oluştur | — | — | mcp-servers-guide |
| `mcp-orchestration` | MCP mimari kararları, CLI vs MCP, A2A | — | mcp-catalog | mcp-servers-guide, anthropic-mcp-builder |

---

## 💹 TİCARET / FİNANS

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `algo-trading-stack` | Alpaca API, piyasa stratejisi, ETF rotasyon, Kelly, kripto edge | — | — | backtesting-python |
| `backtesting-python` | Framework seçimi (VectorBT/Backtrader/backtesting.py), walk-forward, slippage, metrikler | — | — | algo-trading-stack |

---

## 📋 PLAN / STRATEJİ

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `plan` | Implementasyon planı | — | — | ultrathink-developer |
| `checklist-manifesto` | Checklist tabanlı görev | — | — | plan |
| `superpowers-pm` | PM süper güçleri | — | — | plan, data-product-designer |
| `data-product-designer` | Veri ürün tasarımı | — | — | superpowers-pm |
| `gstack-company` | Şirket teknoloji stack | — | — | multi-llm-architect |
| `habits-for-success` | Başarı alışkanlıkları | — | — | — |
| `smarter-faster-better` | Verimlilik metodolojisi | — | — | — |

---

## 🌍 DİL / ÖZEL

| Skill | Ne Zaman | Conflicts | Specializes | Composes |
|-------|----------|-----------|-------------|----------|
| `turkce-commit-mesajlari` | Git commit Türkçe | — | — | — |
| `mapcn` | Map/coğrafi analiz | — | — | — |
| `cinema-worldbuilder-pro-2.0` | Film dünya inşası | — | — | ai-novel-architect |
| `banana-pro-director-2.0` | Banana direktör | — | — | — |
| `anthropic-canvas-design` | Canvas UI tasarımı | — | — | frontend-design |
| `anthropic-theme-factory` | Tema fabrikası | — | — | anthropic-canvas-design |
| `anthropic-web-artifacts-builder` | Web artifact oluştur | — | — | frontend-design |

---

## ⚡ HIZLI REFERANS — Sık Kullanılan Kombinasyonlar

```
Codebase analizi:    graphify → deep-research → code-wiki
Web scraping/test:   agent-browser → (deep-research opsiyonel)
Yeni skill:          skill-creator → anthropic-skill-creator → ai-skill-pipeline
Araştırma:           deep-research (tek yeterli, autoresearch ile karıştırma)
Video üretim:        video-prompt-builder → higgsfield-generate (veya seedance-prompter)
Orchester:           orchester → (kermes veya hermes-agent-mastery)
SEO:                 ai-seo → page-cro → content-strategy
Review:              zen-comprehensive-review → cross-review
Token tasarrufu:     claude-code-harness (CBM + context-mode + hooks)
API maliyet düşür:   context-engineering (KV-Cache + CCR + RTK)
Algo trading:        algo-trading-stack → backtesting-python (framework + kod)
Agent bellek:        ai-agent-memory-rag → karpathy-obsidian (implementasyon)
MCP seçimi:          mcp-orchestration → mcp-catalog → mcp-servers-guide
Web scraping:        web-scraping-ai (Crawl4AI + DeepSeek) — agent-browser değil (anti-bot)
n8n + Python:        n8n-automation (Native Runner + webhook + Prefect)
Telegram bot:        telegram-bot-python (PTB v21.x async + multi-bot)
xAI / Grok Build:    birkan-xai-grok-build (CLI headless pattern, API, batch, ses/görsel)
LLM maliyet düşür:   ecc-cost-aware-llm-pipeline → ecc-token-budget-advisor
Agent döngü:         ecc-autonomous-loops → ecc-verification-loop (ralph-loop ile tamamla)
Yıkıcı op koruması:  ecc-safety-guard (rm/delete öncesi otomatik kontrol)
Çok görüş kararı:    ecc-council (tartışma modu hafif alternatifi, tek model)
Agent değerlendirme: ecc-agent-eval → ecc-benchmark
```

---

## 📦 ECC Entegrasyonu (2026-07-14)

ECC (everything-claude-code) repo'sundan çakışmasız eklenenler:

| Skill | Ne İşe Yarar |
|-------|-------------|
| `ecc-cost-aware-llm-pipeline` | LLM API maliyet optimizasyonu: model routing, budget tracking, retry |
| `ecc-token-budget-advisor` | Token bütçe yönetimi, context penceresi optimizasyonu |
| `ecc-verification-loop` | Görev tamamlanma doğrulama döngüsü (orchester ile birlikte) |
| `ecc-safety-guard` | Yıkıcı işlem koruması (production/otonomous modlar için) |
| `ecc-autonomous-loops` | Otonom agent döngüsü tasarımı |
| `ecc-benchmark` | Model/sistem benchmark metodolojisi |
| `ecc-agent-eval` | Agent çıktı değerlendirme |
| `ecc-council` | 4 ses konsey: tartışma modu hafif alternatifi |

Rules: `~/.claude/rules/ecc/` → common (security, testing, git-workflow, performance, patterns, coding-style) + python (fastapi, patterns, testing)
