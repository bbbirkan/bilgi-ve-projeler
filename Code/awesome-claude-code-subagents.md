# awesome-claude-code-subagents (VoltAgent)

Claude Code için 131+ özelleşmiş subagent koleksiyonu. VoltAgent tarafından yönetiliyor, plugin sistemi + manuel kurulum + interaktif installer desteği var.

## Ne İşe Yarar

Claude Code'un subagent sistemine hazır agent dosyaları sağlar. Her agent kendi context window'unda çalışır, domain'ine özel talimatları ve tool izinleri vardır. Plugin olarak kurulabilir.

## Kurulum Seçenekleri

```bash
# Plugin olarak (önerilen)
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang    # Dil uzmanları
claude plugin install voltagent-infra   # DevOps
claude plugin install voltagent-core-dev  # Temel geliştirme

# İnteraktif installer
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
cd awesome-claude-code-subagents
./install-agents.sh

# Inline (clone gerekmez)
curl -sO https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/install-agents.sh
chmod +x install-agents.sh && ./install-agents.sh
```

## 10 Kategori + Plugin'ları

| Plugin | Kategori | Örnek agent'lar |
|--------|----------|----------------|
| `voltagent-core-dev` | Core Dev | api-designer, frontend-developer, websocket-engineer |
| `voltagent-lang` | Diller | typescript-pro, python-pro, golang-pro, rust-engineer (+30) |
| `voltagent-infra` | Altyapı | kubernetes-specialist, terraform-engineer, sre-engineer |
| `voltagent-qa-sec` | QA & Güvenlik | penetration-tester, code-reviewer, chaos-engineer |
| `voltagent-data-ai` | Data & AI | llm-architect, mlops-engineer, prompt-engineer |
| `voltagent-dev-exp` | DX | mcp-developer, readme-generator, refactoring-specialist |
| `voltagent-domains` | Özel Alan | healthcare-admin (51 alt-agent!), m365-admin, fintech-engineer |
| `voltagent-biz` | İş / Ürün | product-manager, scrum-master, legal-advisor |
| `voltagent-meta` | Orkestrasyon | multi-agent-coordinator, workflow-orchestrator, task-distributor |
| `voltagent-research` | Araştırma | competitive-analyst, project-idea-validator, scientific-literature-researcher |

## Model Routing

```
Opus   → Güvenlik, mimari, fintech (derin düşünme)
Sonnet → Günlük kodlama, debug, refactoring
Haiku  → Hızlı: dokümantasyon, SEO, build
```

## Agent Dosya Formatı

```yaml
---
name: subagent-name
description: Ne zaman devreye girmeli
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---
Sen bir [rol]...
```

**Kaynak:** [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) · MIT
