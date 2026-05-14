# awesome-claude-agents (rahulvrane)

Claude Code agent ve subagent ekosisteminin kapsamlı rehberi. Kendi agent koleksiyonu değil, mevcut tüm repo'ları, araçları, eğitimleri ve videoları bir araya getiren **meta-dizin**.

## Ne İşe Yarar

Claude Code subagent dünyasını takip etmek için tek nokta. Hangi repo'da ne var, hangi araçları kullanmalısın, nasıl orchestrate edersin — hepsini özetler.

## En İyi Üretim Koleksiyonları

| Repo | Agent sayısı | Özellik |
|------|-------------|---------|
| [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) | 100+ | En büyük, uniform format |
| [wshobson/agents](https://github.com/wshobson/agents) | 184 | Production-ready, orchestration |
| [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | 26 | AI dev team odaklı |
| [davepoon/claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection) | 36 | Auto-delegation, best practices |

## Başlangıç Önerisi

| Durum | Öneri |
|-------|-------|
| Yeni başlayan | iannuttall/claude-agents (7 agent, basit) |
| Bireysel geliştirici | 0xfurai (100+ agent, tek clone) |
| Takım / enterprise | wshobson/agents (plugin sistemi, orchestration) |
| AI dev workflow | vijaythecoder/awesome-claude-agents |

## Orchestration Desenleri

```
Sequential   : A → B → C → Sonuç
Parallel     : Çoklu agent aynı anda, sonuçlar birleştirilir
Conditional  : Analize göre dinamik routing
Review Gate  : Birincil agent → Review agent → Final
```
**Not:** Maksimum 10 paralel görev (sistem sınırı).

## Öne Çıkan Araçlar

- **webdevtodayjason/sub-agents** — NPM ile kurulabilir CLI manager
- **baryhuang/claude-code-by-agents** — Masaüstü uygulama, @agent mention desteği
- **Dicklesworthstone/claude_code_agent_farm** — Çoklu Claude session paralel orchestration
- **subagents.cc** — Topluluk agent dizini

## Agent Geliştirme İpuçları

- `.claude/agents/` proje-spesifik, `~/.claude/agents/` global (proje öncelikli)
- Sistem promptları kısa tut — uzun promptlar token maliyeti artırır
- Her agent için sadece gerekli tool izinleri ver
- Agent'ları numara prefiksiyle sırala: `01_code-reviewer.md`

**Kaynak:** [rahulvrane/awesome-claude-agents](https://github.com/rahulvrane/awesome-claude-agents) · MIT
