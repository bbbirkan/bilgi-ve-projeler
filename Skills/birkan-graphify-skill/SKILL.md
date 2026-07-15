---
name: graphify-skill
description: |
  Graphify knowledge graph aracının kurulum, çalıştırma, query ve sovereign-brain
  entegrasyon rehberi. VPS (Contabo) üzerinde çalışan canlı sistem.
  Binary: /root/.local/bin/graphify (v0.8.13)
  Ana kullanım: /root/sovereign-brain/ knowledge graph (Level 4 second brain)

  TRIGGER bu skill'i şu durumlarda çağır:
  - "/graphify", "knowledge graph", "graph build" istendiğinde
  - sovereign-brain güncelle, graph query, node analizi istendiğinde
  - Yeni bir proje klasörüne graphify eklenecekse
  - "graphify query", "graphify path", "graphify explain" sorulduğunda
---

# Graphify — Knowledge Graph Skill (VPS / Contabo)

Herhangi bir klasörü LLM-destekli knowledge graph'a çeviren araç.

**Binary:** `/root/.local/bin/graphify` (v0.8.13)
**Sunucu:** Contabo VDS, Ubuntu 24.04, `/root/`

## Second Brain Seviye Bağlamı

Bu araç bizim "Level 4 second brain" mimarimizin çekirdeği.
5 seviye şöyle sıralanır: dosya → wiki → vektör DB → knowledge graph (BİZ) → always-on OS
Graphify = Level 4. Şu an için yeterli, daha üste çıkmaya gerek yok.

## DevPass (LLM Gateway) ile Kullanım — OPENAI_API_KEY GEREKMİYOR

graphify `deepseek` backend'i DevPass üzerinden çalışır. `llm.py` patch edildi (2026-07-15):
- `DEEPSEEK_BASE_URL` env var ile base URL override edilebilir
- `DEEPSEEK_API_KEY` → `$LLMGATEWAY_KEY` kullan
- Model: `deepseek-v4-flash` (hızlı, ucuz ~$0.009/çalıştırma) veya `deepseek-v4-pro`

```bash
source /root/.sovereign_env

# Herhangi klasörü graphify et (DevPass deepseek-v4-flash)
DEEPSEEK_BASE_URL=https://api.llmgateway.io/v1 \
DEEPSEEK_API_KEY=$LLMGATEWAY_KEY \
graphify <klasör> --output <klasör>/graphify-out --backend deepseek

# Model seçimi
GRAPHIFY_DEEPSEEK_MODEL=deepseek-v4-pro   # daha derin
GRAPHIFY_DEEPSEEK_MODEL=deepseek-v4-flash # hızlı/ucuz (varsayılan)
```

**Patch dosyası:** `/root/.local/share/uv/tools/graphifyy/lib/python3.11/site-packages/graphify/llm.py`
- Satır ~90: `"base_url": os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")`
- Satır ~92: `"default_model": os.environ.get("GRAPHIFY_DEEPSEEK_MODEL", "deepseek-v4-flash")`

> ⚠️ graphify update sonrası patch kaybolabilir — tekrar uygulanması gerekir.

## Ana Graph — Sovereign Brain

```bash
# sovereign-brain'i güncelle (AST, hızlı — LLM gerekmez)
graphify update /root/sovereign-brain/

# Tam extraction — DevPass ile
source /root/.sovereign_env
DEEPSEEK_BASE_URL=https://api.llmgateway.io/v1 \
DEEPSEEK_API_KEY=$LLMGATEWAY_KEY \
graphify /root/sovereign-brain/ --backend deepseek

# Doğal dil sorgu
graphify query "sorum ne?" \
  --graph /root/sovereign-brain/graphify-out/graph.json \
  --budget 3000

# Node açıklaması + komşuları
graphify explain "yt-signal" \
  --graph /root/sovereign-brain/graphify-out/graph.json
```

## Temel Komutlar

```bash
# Tam extraction (AST + semantic LLM)
graphify extract <klasör>

# Sadece AST (LLM gerekmez, hızlı)
graphify update <klasör>

# Mevcut graph'tan cluster + HTML yeniden üret
graphify cluster-only <klasör>

# Git hook kur (her commit'te otomatik güncelleme)
graphify hook install
```

## Query Komutları

```bash
# Doğal dil sorgu (BFS)
graphify query "sorum ne?" --graph <path>/graphify-out/graph.json --budget 3000

# İki node arasındaki en kısa yol
graphify path "node-a" "node-b" --graph <path>/graphify-out/graph.json

# Node açıklaması + komşuları
graphify explain "node-adı" --graph <path>/graphify-out/graph.json
```

## Export Komutları

```bash
# Obsidian vault (her node = .md dosyası + graph.canvas)
graphify export obsidian \
  --graph /root/sovereign-brain/graphify-out/graph.json \
  --dir /root/sovereign-brain/obsidian-export/

# Collapsible tree HTML
graphify tree \
  --label "Sovereign Brain" \
  --graph /root/sovereign-brain/graphify-out/graph.json \
  --output /root/sovereign-brain/graphify-out/GRAPH_TREE.html

# Diğer formatlar
graphify export html        # İnteraktif D3 graph
graphify export graphml     # Neo4j uyumlu
graphify export svg         # Statik SVG
```

## Multi-Repo Birleştirme

```bash
# 2+ graph.json'u cross-repo graph'a birleştir
graphify merge-graphs \
  /root/sovereign-brain/graphify-out/graph.json \
  /root/2026-yt-signal/graphify-out/graph.json \
  --out /root/cross-repo-graph.json
```

## VPS'teki Aktif Graph'lar

| Klasör | graph.json | Not |
|--------|-----------|-----|
| `/root/sovereign-brain/` | `graphify-out/graph.json` | Ana beyin — kararlar, araştırmalar, ekip |
| Diğer projeler | Henüz eklenmedi | İleride birleştirilebilir |

## Oturum Sonu Rutini

Her önemli oturum sonunda sovereign-brain'i güncelle:
```bash
graphify update /root/sovereign-brain/
```

## .gitignore için Önerilen

```gitignore
graphify-out/graph.json
graphify-out/graph_slim.json
graphify-out/*.html
graphify-out/cache/
graphify-out/.graphify_chunk_*.json
```

## Slim Graph (Büyük Graph'lar İçin)

```python
# Yüksek-degree node'ları filtrele
python3 slim_graph.py --min-degree 3 --max-label 80 --top 3000 \
  --input graphify-out/graph.json \
  --output graphify-out/graph_slim.json
```
