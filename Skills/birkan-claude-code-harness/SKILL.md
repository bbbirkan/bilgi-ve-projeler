# Claude Code Harness — Token Tasarrufu ve Production Kalıpları

## Ne Zaman Kullan
- Claude Code token maliyeti/hızı sorunları varsa
- Production agent harness kuruyorsan
- Uzun oturumlarda context tükeniyorsa
- Multi-agent koordinasyon (Claude + AGY + OpenCode = Orchester) tasarlarken

---

## 5 Katmanlı Token Tasarrufu Sistemi

```
PROMPT / QUERY
    ↓
[Layer 1: CBM — Knowledge Graph]       → dosya okumak yerine AST grafik sorgula (%99 tasarruf)
    ↓
[Layer 2: IntelligentContext (Headroom)] → önem puanlamasıyla bağlam daraltma (%98)
    ↓
[Layer 3: RTK — Shell Compression]     → CLI çıktısını yerinde sıkıştır (%60–90)
    ↓
[Layer 4: Headroom — API Proxy]        → CCR (Compress-Cache-Retrieve) ile kayıpsız sıkıştırma (%47–92)
    ↓
Anthropic API
```

> **Caveman hook çalışmaz:** `UserPromptSubmit` hook'u çıktıyı *değiştirmez*, orijinal isteğin başına *ekler* (prepend). Token sayısını düşürmez — ikiye katlar. Token tasarrufu için mutlaka proxy katmanı (Headroom/RTK) kullan.

### CBM (Codebase Memory MCP) — Detaylar
- 159 dil destekler, tek Rust binary (bağımlılıksız)
- VS Code/Copilot/Claude Desktop'a JSON ayar ile ekle
- Kod tabanını bilgi grafiğine dönüştürür — sadece ilgili düğümleri sorgular
- Kaynak: `github.com/DeusData/codebase-memory-mcp`

### RTK (Rust Token Killer) — Detaylar
- 64 terminal komutu için CLI proxy
- "Auto-Rewrite Hook" (rtk-rewrite.sh) → komut otomatik yakalanır, RTK'dan geçer
- WSL: otomatik hook. **Native Windows: hook çalışmaz → CLAUDE.md injection moduna düşer**
- Kaynak: `github.com/rtk-ai/rtk`

### Headroom — CCR Mimarisi
- Sıkıştırılan veriyi silmez → SQLite'ta hash ile saklar
- Ajana `headroom_retrieve` aracı verilir → gerektiğinde orijinal veri geri çağrılır
- **Kayıpsız** sıkıştırma (lossless): kaynak bilgi kaybolmaz
- "Failure Learning" (headroom learn): ajandaki geçmiş başarısızlıklar → CLAUDE.md'ye otomatik yazar
- Kaynak: `github.com/chopratejas/headroom`

**Kaynak:** `github.com/sgaabdu4/claude-code-tips` — tek tıkla yükleyici mevcut.

---

## Zorunlu Hook'lar

```json
// ~/.claude/hooks/ altına ekle
{
  "bash-ban-raw-tools": "cat/grep/find/head/tail komutlarını engeller — CBM kullanmaya zorlar",
  "cbm-code-discovery-gate": "CBM sorgusu yapılmadan Read/Grep araçlarını kilitler"
}
```

---

## Settings (.claude/settings.json)

```json
{
  "model": "claude-opus-4-8",
  "effortLevel": "xhigh",
  "advisorModel": "opus",
  "env": {
    "ENABLE_PROMPT_CACHING_1H": "1",
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-4-6"
  }
}
```

---

## MCP Kuralı: Az Tut

```bash
# Aktif MCP'leri listele
claude mcp list

# Gereksiz olanları kaldır
claude mcp remove <isim>

# Sadece 2 MCP her zaman açık:
# 1. codebase-memory-mcp  (CBM — kod keşfi)
# 2. context-mode          (büyük çıktı sandboxing)

# Diğerleri: sadece o görev için ekle, bitince kaldır
```

---

## CLAUDE.md Optimizasyonu

```
/caveman:compress  →  CLAUDE.md'yi sıkıştır
```
Her oturum başında yükleniyor → küçülmesi çarpan etkisi yaratır. Bunu bir kez yap, tüm oturumlar kazanır.

---

## Hızlı Kazanımlar (Hemen Uygula)

1. **`/clear` agresif kullan** — kısa, odaklı oturumlar uzun oturumdan daha verimli
2. **Mermaid > prose** — mimari şeması için 6 satır Mermaid = 3 paragraf; Claude native parse eder
3. **CLI > MCP** — Tavily, Appwrite gibi araçlar CLI üzerinden çok daha az context harcar
4. **Per-stack rule files** — `~/.claude/rules/<stack>.md` — özel stack için kural dosyaları

---

## Multi-Agent Koordinasyon (Orchester Paterni)

```
Opus 4.8 → Plan (/ultraplan)
    ↓
Opus → Implement (paralel subagentler)
    ↓
Cross-vendor review (farklı modelden)
    ↓
E2E test (Agent Browser / Dart MCP)
```

Birkan'ın mevcut Orchester'ı bu modeli zaten uyguluyor:
- Claude (analiz)  
- OpenCode (implementasyon)  
- AGY (sentez + koordinasyon)

---

## Skills Mimarisi Best Practices

- Her skill SKILL.md içinde `## Ne Zaman Kullan` bölümüyle başlar
- `conflicts` / `composes` / `specializes` ilişkilerini SKILLS_INDEX.md'e ekle
- Skill tetiklenme mekanizmasını `model.default` yönlendirmesiyle optimize et
- Skill'leri gereksiz MCP gibi değil, "always-on routing katmanı" gibi tasarla

---

## Production Agent Güvenilirliği

### 3-Katmanlı Self-Heal (Her operasyona uygula)

```
L1 — Deterministik Guard (anlık, token maliyetsiz)
     → Kural tabanlı, her operasyonda çalışır
     → Başarısızsa L2'ye el ver

L2 — Kısıtlı Agentic Loop (token harcamalı, sadece L1 başarısızsa)
     → Max 3 deneme, her denemede gerçek sonucu RE-TEST et
     → Confidence gate ≥ 70: Claude 0-100 öz-puanlama yapar,
       70 altıysa harekete geçme, L3'e aktar
     → "Ground truth on the wire" prensibi:
       Claude'un "hallettim" demesi yetmez — gerçek komutu yeniden çalıştır

L3 — Operator Escalation (otomatik çözüm başarısızsa)
     → L2'nin tüm trail'ini (her deneme, her aksiyon, confidence'lar) ilet
     → Operator "bir şeyler bozuldu" değil, tam bağlamla devralır
```

### Anti-Spiral Kuralları

```python
# Retry budget — sonsuz döngü engeli
MAX_CONSECUTIVE_FAILURES = 3   # aşıldığında eskalasyon

# Author-aware dedup — botun kendi cevabını tekrar vermesini engelle
if last_bot_message_time > last_human_message_time:
    skip_reply()   # zaten cevapladık
```

### MCP Watchdog Prensibi

```
Her 10 dakikada bir: her MCP için no-op tool call dene
  → Başarısız → sessizce token refresh dene
  → Refresh de başarısız → operatöre bildirim gönder
  → 2 ardışık başarısız → uyarı seviyesi yükselt

Neden: Süresi dolmuş token "model bugün aptal" görünür —
       ama gerçekte "tool empty result döndürüyor"
```

**Referans:** `github.com/DenisSergeevitch/agents-best-practices` — provider-neutral production harness template

---

## Token Ölçüm

- **Codeburn**: `github.com/getagentseal/codeburn` — session token kullanımını izle
- Bir `cargo test` (262 test) = ~4,823 token
- Bir `git diff HEAD~1` = ~21,500 token
- 500 satır dosya okuma = context penceresi dolabilir

---

## VPS (Hermes) için Ek Ayarlar

```bash
# /root/.hermes/.env veya systemd servis dosyasına ekle
ENABLE_PROMPT_CACHING_1H=1
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50
CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-4-6
```
Rate-limit'leri önler, otonom döngülerde context tükenmesini geciktirir.
