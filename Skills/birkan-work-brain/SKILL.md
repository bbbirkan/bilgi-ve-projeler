---
name: work-brain
description: |
  Work klasörü bilgi sistemi — 40+ projeyi indeksler, knowledge graph kurar, VPS'e senkronize eder.
  Şu skill'leri orkestre eder (silmez, referans verir): graphify, ai-agent-memory-rag, llm-wiki, karpathy-obsidian.
  
  TRIGGER: "work indexle", "projeleri indexle", "knowledge graph güncelle", "work-brain", "wq", "proje ara",
  "build_brain", "iş beyin", "ekosistemi indexle", "workspace index"
---

# work-brain — Work Klasörü Bilgi Sistemi

Birkan'ın ~/Desktop/Work/ ekosistemini (40+ proje) tam indeksleyip VPS'e senkronize eden şemsiye skill.
Hiçbir alt skill'i değiştirmez — hepsini sırayla çağırır.

---

## Sistem Mimarisi

```
LOCAL MAC (~/Desktop/Work/)
┌─────────────────────────────────────────────────────┐
│ AŞAMA 1: OpenCode + DeepSeek V4 Pro                 │
│   → Her proje klasöründe INDEX.md (40 adet)         │
│   → WORK_INDEX.md (master index, ~20K token)        │
│   Skill referans: (index_work.py — doğrudan script) │
├─────────────────────────────────────────────────────┤
│ AŞAMA 2: graphify (knowledge graph)                 │
│   → graphify-out/graph.json  (GraphRAG sorgu)       │
│   → graphify-out/wiki/       (agent-crawlable wiki) │
│   → graphify-out/graph.html  (görsel tarayıcı)      │
│   Skill referans: [[graphify]]                      │
├─────────────────────────────────────────────────────┤
│ AŞAMA 3 (OPSİYONEL): llm-wiki büyütme              │
│   Her konuşmada yeni öğrenilenler wiki'ye yazılır   │
│   Skill referans: [[llm-wiki]], [[karpathy-obsidian]]│
└─────────────────────────────────────────────────────┘
         ↓ rsync / scp
VPS (root@207.180.204.66)
┌─────────────────────────────────────────────────────┐
│ /root/.hermes/context/work_index.md                 │
│   → CAG: Hermes her konuşmada okur, RAG gerekmez   │
│   Mimari karar: [[ai-agent-memory-rag]]             │
├─────────────────────────────────────────────────────┤
│ /root/work-wiki/        (graphify wiki makaleleri)  │
│ /root/work-graph.json   (local projeler graph)      │
│ /root/unified-graph.json (local + VPS merge)        │
├─────────────────────────────────────────────────────┤
│ VPS-native projeler (ayrıca graphify ile)           │
│   /root/2026-sovereign, /root/2026-orchester, vb.   │
│   → merge-graphs → unified-graph.json              │
└─────────────────────────────────────────────────────┘
```

---

## Mimari Kararlar (ai-agent-memory-rag'e göre)

| Soru | Cevap | Neden |
|------|-------|-------|
| RAG mı CAG mı? | **CAG** | WORK_INDEX.md ~20K token → Hermes context'e sığar, RAG karmaşıklığı gereksiz |
| Vector DB gerekli mi? | **Hayır** | <500K token, statik, CAG yeterli |
| LLM Wiki ne zaman? | Büyürken | Her konuşmadan öğrenilen şeyler wiki'ye yazılırsa değer artıyor |
| graphify ne için? | **Cross-project ilişkiler** | "Orchester → Hermes → Kermes" bağlantıları, CAG'den daha güçlü sorgu |

---

## Komutlar

### Tam sistem kurulumu (ilk kez veya büyük güncelleme)
```bash
bash "/Users/birkan/Desktop/Work /build_brain.sh"
```

### Sadece OpenCode (INDEX.md'ler)
```bash
python3 "/Users/birkan/Desktop/Work /index_work.py"
# Test için:
python3 "/Users/birkan/Desktop/Work /index_work.py" --test
```

### Sadece graphify (knowledge graph güncelle)
```bash
cd "/Users/birkan/Desktop/Work "
graphify . --update --wiki
```

### Sadece VPS sync
```bash
bash "/Users/birkan/Desktop/Work /build_brain.sh" --phase 3
```

### VPS'te sorgu (SSH sonrası)
```bash
wq 'Kermes nasıl çalışır?'          # doğal dil sorgu
wpath 'Orchester' 'Hermes'          # iki proje arası bağlantı
wexplain 'sovereign'                # proje açıklaması
windex                              # master index oku
wwiki                               # wiki makaleleri listesi
```

---

## Dosya Haritası

| Dosya | Konum | Açıklama |
|-------|-------|----------|
| `index_work.py` | `Work /index_work.py` | OpenCode orkestrasyon scripti |
| `build_brain.sh` | `Work /build_brain.sh` | Tam sistem kurulum scripti |
| `WORK_INDEX.md` | `Work /WORK_INDEX.md` | Master index (40 proje özeti) |
| `graphify-out/` | `Work /graphify-out/` | Graph JSON + wiki + HTML |
| `work_index.md` | VPS: `/root/.hermes/context/` | Hermes CAG context |
| `work-wiki/` | VPS: `/root/work-wiki/` | Agent wiki |
| `unified-graph.json` | VPS: `/root/` | Sorgulanabilir tam graph |

---

## Günceleme Sıklığı

| Ne zaman çalıştır | Komut |
|-------------------|-------|
| Yeni proje eklendiğinde | `build_brain.sh` (tam) |
| Proje içeriği değiştiğinde | `index_work.py` + `build_brain.sh --phase 2 3` |
| Sadece VPS context güncelle | `build_brain.sh --phase 3` |
| Hızlı graph güncelle | `graphify . --update` → `build_brain.sh --phase 3` |

---

## Alt Skill Referansları (değiştirilmez, sadece referans)

- [[graphify]] → knowledge graph motoru
- [[ai-agent-memory-rag]] → mimari karar: RAG vs CAG vs LLM Wiki
- [[llm-wiki]] → birikimli wiki pattern (her konuşmadan öğren)
- [[karpathy-obsidian]] → graphify wiki'yi Obsidian vault'a çevir
- [[graphify-skill]] → VPS'te graphify yönetimi
- [[knowledge-pipeline]] → bilgi akışı pipeline

---

## LLM Wiki Büyütme (OPSİYONEL — Faz 2)

Şu an INDEX.md'ler statik. Büyüyen sistem için:

```
Her VPS konuşmasında:
  Claude öğrendiği yeni şeyi → /root/work-wiki/<proje>.md'ye yazar
  graphify update /root/work-wiki/ → graph güncellenir
  Böylece wiki her konuşmayla büyür
```

Kurmak için: [[llm-wiki]] skill'ini çağır, vault root olarak `/root/work-wiki/` kullan.

---

## VPS'te İlk Kurulum Sonrası Kontrol

```bash
ssh root@207.180.204.66
# Hermes context kontrolü
ls /root/.hermes/context/
cat /root/.hermes/context/work_index.md | head -30

# Graph sorgu testi
wq 'hangi projeler Python kullanıyor?'

# Wiki makaleleri
wwiki
```
