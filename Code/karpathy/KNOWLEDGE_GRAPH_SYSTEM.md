# 🧠 Knowledge Graph + Second Brain Sistemi
## Kurulum Rehberi — Tek Prompt ile Tam Entegrasyon

> **Ne işe yarar?**
> Claude (veya herhangi bir LLM) projelerinizi, notlarınızı ve kararlarınızı bir knowledge graph olarak görür.
> Her oturumda "Bu projede ne var?" diye sormak zorunda kalmazsınız.
> LLM projeyi bilir, bağlantıları görür, doğru cevap verir.

---

## 🎯 Bu Sistem Ne Kazandırıyor?

| Eski Yöntem | Bu Sistem |
|-------------|-----------|
| LLM 20-30 dosya okur, yine de bağlantıları kaçırır | LLM önce graph'ı okur, 1 dosyada her şeyi görür |
| "Bu özellik nerede implement edildi?" → grep + manuel arama | `graphify query "özellik adı"` → doğrudan cevap |
| Kararlar, stratejiler kaybolur | `brain "karar: ..."` → Obsidian'a otomatik kaydedilir |
| Projeler arası bağlantı görünmez | Cross-repo graph tüm projeleri birleştirir |
| Her oturumda bağlamı yeniden açıklamak | CLAUDE.md + graph → LLM projeyi tanıyor başlar |

**Birkan'ın projesinde kanıtlanan bağlantı:**
`01 Promt MUHENDISLIGI`'ndeki Conductor/DAAO teorisi →
`2026_Trade Bots`'taki TradingCouncil/WorkflowOrchestrator olarak implement edilmişti.
Graph bunu 83,858 node arasında otomatik buldu. İnsan gözü kaçırmıştı.

---

## 🔧 Gereksinimler (Kullanıcı Yapacak)

```bash
# 1. graphify kur
pip install graphifyy

# 2. Vault yolu belirle (Obsidian klasörün)
VAULT="/Users/KULLANICI/Obsidian Vault"

# 3. brain CLI'yi kur (aşağıdaki scripti .local/bin/brain olarak kaydet)
chmod +x ~/.local/bin/brain
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
```

**brain script dosyası:** → Bu dosyanın altında, "BRAIN SCRIPT" bölümünde.

---

## 🤖 LLM'e Verilecek Tek Prompt (Kurulum)

Aşağıdaki promptu herhangi bir LLM'e ver. Gerekli her şeyi yapar.

```
Sen bir knowledge graph + second brain kurulum ajanısın.
Kullanıcının projelerini ve Obsidian vault'unu entegre edeceksin.

## Kurulum Adımları

### 1. Graphify — Her Proje Klasörü İçin

Her proje klasöründe sırayla çalıştır:

```bash
cd "PROJE_YOLU"

# Python interpreter'ı bul ve kaydet
PYTHON=$(which graphify | xargs head -1 | tr -d '#!')
[ -z "$PYTHON" ] && PYTHON="python3"
mkdir -p graphify-out
"$PYTHON" -c "import sys; open('graphify-out/.graphify_python','w').write(sys.executable)"

# Dosyaları tespit et
$(cat graphify-out/.graphify_python) -c "
import json
from graphify.detect import detect
from pathlib import Path
result = detect(Path('.'))
print(json.dumps(result))
" > graphify-out/.graphify_detect.json

# AST extraction (kod dosyaları için — ücretsiz, LLM gerektirmez)
$(cat graphify-out/.graphify_python) -c "
import json
from graphify.extract import collect_files, extract
from pathlib import Path
detect = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
code_files = [Path(f) for f in detect.get('files',{}).get('code',[])]
result = extract(code_files, cache_root=Path('.')) if code_files else {'nodes':[],'edges':[],'input_tokens':0,'output_tokens':0}
Path('graphify-out/.graphify_ast.json').write_text(json.dumps(result, indent=2))
print(f'AST: {len(result[\"nodes\"])} nodes, {len(result[\"edges\"])} edges')
"
```

Semantic extraction için dosyaları 20'şer gruplu chunk'lara böl.
Her chunk için dosyaları oku ve bu JSON formatında extract et:

```json
{"nodes":[{"id":"stem_entity","label":"Human Readable","file_type":"document|paper|image|rationale|code","source_file":"relative/path","source_location":null,"source_url":null,"captured_at":null,"author":null,"contributor":null}],"edges":[{"source":"id","target":"id","relation":"conceptually_related_to|references|cites|semantically_similar_to","confidence":"EXTRACTED|INFERRED|AMBIGUOUS","confidence_score":1.0,"source_file":"relative/path","source_location":null,"weight":1.0}],"hyperedges":[],"input_tokens":0,"output_tokens":0}
```

Kurallar:
- confidence_score: EXTRACTED=1.0, INFERRED={0.95|0.85|0.75|0.65|0.55}, AMBIGUOUS=0.1-0.3
- Node ID: sadece [a-z0-9_], format: {dosyaadı}_{kavram}, chunk numarası EKLEME
- PDF için ilk 5 sayfayı oku (pages:"1-5")
- Image için vision kullan

Her chunk'ı .graphify_chunk_NN.json olarak kaydet, sonra birleştir:

```bash
$(cat graphify-out/.graphify_python) -c "
import json, glob
from pathlib import Path
chunks = sorted(glob.glob('graphify-out/.graphify_chunk_*.json'))
nodes, edges, hyperedges = [], [], []
for c in chunks:
    d = json.loads(Path(c).read_text())
    nodes += d.get('nodes',[]); edges += d.get('edges',[]); hyperedges += d.get('hyperedges',[])
Path('graphify-out/.graphify_semantic.json').write_text(json.dumps({'nodes':nodes,'edges':edges,'hyperedges':hyperedges,'input_tokens':0,'output_tokens':0},indent=2))
print(f'{len(chunks)} chunk, {len(nodes)} node, {len(edges)} edge')
"

# AST + semantic merge
$(cat graphify-out/.graphify_python) -c "
import json
from pathlib import Path
ast = json.loads(Path('graphify-out/.graphify_ast.json').read_text())
sem = json.loads(Path('graphify-out/.graphify_semantic.json').read_text())
seen = {n['id'] for n in ast['nodes']}
merged = list(ast['nodes']) + [n for n in sem['nodes'] if n['id'] not in seen]
Path('graphify-out/.graphify_extract.json').write_text(json.dumps({'nodes':merged,'edges':ast['edges']+sem['edges'],'hyperedges':sem.get('hyperedges',[]),'input_tokens':0,'output_tokens':0},indent=2))
print(f'Merged: {len(merged)} nodes')
"

# Graph build + report
$(cat graphify-out/.graphify_python) -c "
import json
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json
from pathlib import Path
extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
detection = json.loads(Path('graphify-out/.graphify_detect.json').read_text())
G = build_from_json(extraction)
communities = cluster(G)
cohesion = score_all(G, communities)
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: 'Community '+str(cid) for cid in communities}
questions = suggest_questions(G, communities, labels)
report = generate(G, communities, cohesion, labels, gods, surprises, detection, {'input':0,'output':0}, '.', suggested_questions=questions)
Path('graphify-out/GRAPH_REPORT.md').write_text(report)
to_json(G, communities, 'graphify-out/graph.json')
print(f'Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities')
"

# HTML export
graphify export html

# Obsidian export
graphify export obsidian --dir "VAULT_YOLU/Graphify/PROJE_ADI"

# Git hook kur (otomatik güncelleme için)
graphify hook install
```

### 2. CLAUDE.md — Her Proje Klasörüne Ekle

```markdown
## graphify

This project has a knowledge graph at graphify-out/.

Rules:
- ALWAYS read graphify-out/GRAPH_REPORT.md before reading any source files.
- For "how does X relate to Y" questions, use: graphify query "<question>"
- After modifying files, run: graphify update .
```

### 3. Cross-Repo Graph (Tüm Projeleri Birleştir)

```bash
graphify merge-graphs \
  "PROJE1/graphify-out/graph.json" \
  "PROJE2/graphify-out/graph.json" \
  "PROJE3/graphify-out/graph.json" \
  --out "cross-repo-graph.json"
```

### 4. brain CLI — Atomic Note Kaydetme

Aşağıdaki Python scriptini `~/.local/bin/brain` olarak kaydet ve `chmod +x` yap.
`echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`

### 5. graphify watch — Otomatik Güncelleme

```bash
graphify watch "VAULT_YOLU" --debounce 5 &
```

### 6. .gitignore — Her Proje İçin

```
graphify-out/graph.json
graphify-out/*.html
graphify-out/cache/
graphify-out/.graphify_*
# Bunlar commit'lenir:
# graphify-out/GRAPH_REPORT.md
# graphify-out/manifest.json
```

---
Kurulum tamamlandığında her proje için şunları raporla:
- Top 5 god node (label + degree)
- Top 3 surprising connection
- graph.html tam yolu
```

---

## 📋 Görev Dağılımı

### Kullanıcının Yapacakları (1 kez)
- [ ] `pip install graphifyy`
- [ ] Obsidian vault yolunu belirle
- [ ] brain script'i `~/.local/bin/brain` olarak kaydet
- [ ] `chmod +x ~/.local/bin/brain`
- [ ] PATH'e ekle: `echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`

### LLM'in Yapacakları (yukarıdaki promptu ver)
- [ ] Her proje için graphify pipeline'ı çalıştır
- [ ] CLAUDE.md dosyalarını oluştur
- [ ] Cross-repo graph oluştur
- [ ] Obsidian export'u çalıştır
- [ ] Git hook'ları kur
- [ ] .gitignore dosyalarını güncelle

### Günlük Kullanım (Otomatik)
- Commit → graph otomatik güncellenir (git hook)
- Obsidian'a not ekle → graph güncellenir (watch)
- Claude açılır → graph'ı önce okur (CLAUDE.md)

---

## 💻 Günlük Komutlar

```bash
# Soru sor (dosya aramak yerine)
graphify query "stop loss nerede implement edildi"
graphify query "yeni coin eklemek için ne değiştirmeliyim"

# Not kaydet
brain "karar: stop loss 2% olacak"
brain strategy "DAAO routing threshold 0.7"
brain insight "TradingCouncil ile DAAO aynı fikrin iki versiyonu"
brain list    # son notları gör

# Manuel güncelleme (çok yeni dosya ekleyince)
graphify update .

# Obsidian'a export
graphify export obsidian --dir "VAULT/Graphify/PROJE"

# Tarayıcıda aç
open graphify-out/graph.html
```

---

## 🌐 Diğer LLM'lerle Uyumluluk

### Claude Code (claude)
✅ Tam uyumlu — CLAUDE.md otomatik okunur, graph her oturumda aktif.

### GPT-4 / ChatGPT
⚠️ CLAUDE.md okunmaz. Çözüm:
```
System prompt'a ekle:
"Before answering any question about this codebase, read and summarize
the content of graphify-out/GRAPH_REPORT.md. Use it as your primary map."
```
Ya da her oturumda GRAPH_REPORT.md içeriğini system message olarak yapıştır.

### Gemini (Gemini CLI / Aistudio)
⚠️ CLAUDE.md okunmaz. `GEMINI.md` dosyası oluştur, aynı kuralları yaz.
Gemini CLI `GEMINI.md`'yi otomatik okur.

### Cursor / Windsurf / Copilot
⚠️ `.cursorrules` veya `.windsurfrules` dosyasına aynı kuralları ekle:
```
Always read graphify-out/GRAPH_REPORT.md before exploring the codebase.
```

### MCP Uyumlu Her LLM (Evrensel Çözüm)
✅ MCP server başlat — tüm MCP uyumlu LLM'ler graph'ı tool olarak kullanabilir:
```bash
python3 -m graphify.serve graphify-out/graph.json
```
Bu şekilde `query_graph`, `get_node`, `god_nodes`, `shortest_path` tool'ları
Claude Desktop, Cursor, ve MCP uyumlu her client'ta çalışır.

---

## 🗂️ BRAIN SCRIPT

Aşağıdaki içeriği `~/.local/bin/brain` olarak kaydet:

```python
#!/usr/bin/env python3
"""
brain — Obsidian vault'una typed atomic note kaydet
Kullanım:
  brain "stop loss 2% olacak"           # otomatik tip tespiti
  brain decision "stop loss 2% olacak"  # explicit tip
  brain list                             # son notları gör

Tipler: decision, strategy, insight, hypothesis, concept, pattern, problem
"""
import sys, os, re
from datetime import datetime
from pathlib import Path

VAULT = Path(os.environ.get("BRAIN_VAULT", str(Path.home() / "Obsidian Vault")))
BRAIN_DIR = VAULT / "07_Brain"

TYPES = {
    "decision":   ("Kararlar",    "🔴", "Alınan karar"),
    "strategy":   ("Stratejiler", "🔵", "Strateji/yaklaşım"),
    "insight":    ("Bulgular",    "💡", "Keşif/öğrenme"),
    "hypothesis": ("Hipotezler",  "🧪", "Test edilecek fikir"),
    "concept":    ("Kavramlar",   "🧠", "Kavram/teori"),
    "pattern":    ("Örüntüler",   "🔄", "Tekrarlayan örüntü"),
    "problem":    ("Problemler",  "⚠️",  "Çözülmesi gereken"),
}

AUTO_DETECT = {
    "decision":   ["karar", "decided", "seçtik", "kullanacağız", "yapacağız", "olmayacak", "olacak"],
    "strategy":   ["strateji", "yaklaşım", "plan", "yöntem", "approach", "implement"],
    "problem":    ["problem", "hata", "bug", "çalışmıyor", "sorun", "error", "fail"],
    "hypothesis": ["hipotez", "test", "deneyelim", "acaba", "belki", "sanırım", "should"],
    "insight":    ["keşfettim", "gördüm", "anladım", "discovered", "realized", "bulgu", "bağlantı"],
    "pattern":    ["her zaman", "sürekli", "pattern", "tekrar", "always", "repeatedly"],
}

def detect_type(content):
    scores = {t: sum(1 for kw in kws if kw in content.lower()) for t, kws in AUTO_DETECT.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "insight"

def detect_project(content):
    c = content.lower()
    if any(k in c for k in ["trade", "bot", "coinbase", "signal", "council", "stop loss", "btc", "eth"]): return "trade-bots"
    if any(k in c for k in ["prompt", "lyrix", "llm", "claude", "gemini", "conductor"]): return "prompt-muhendisligi"
    if any(k in c for k in ["graphify", "graph", "obsidian", "knowledge"]): return "graphify"
    return "genel"

def slugify(text):
    text = re.sub(r'[^a-z0-9\s-]', '', text.lower()[:50])
    return re.sub(r'\s+', '-', text.strip())

def save_note(tip, content):
    tipo = TYPES.get(tip, TYPES["insight"])
    klasor = BRAIN_DIR / tipo[0]
    klasor.mkdir(parents=True, exist_ok=True)
    now = datetime.now()
    tarih, saat = now.strftime("%Y-%m-%d"), now.strftime("%H:%M")
    project = detect_project(content)
    filepath = klasor / f"{tarih}-{slugify(content)}.md"
    filepath.write_text(f"""---
type: {tip}
date: {tarih}
time: {saat}
project: {project}
tags: [{tip}, {project}]
---

# {tipo[1]} {content.split('.')[0][:100]}

{content}

---
*Kaydeden: brain CLI · {tarih} {saat}*
""", encoding="utf-8")
    return filepath

def main():
    args = sys.argv[1:]
    if not args: print(__doc__); return
    if args[0] == "list":
        notes = sorted(BRAIN_DIR.rglob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[:10] if BRAIN_DIR.exists() else []
        [print(f"  {n.parent.name}/{n.stem[:55]}") for n in notes]
        return
    tip, content = (args[0], " ".join(args[1:])) if args[0] in TYPES else (detect_type(" ".join(args)), " ".join(args))
    if not content.strip(): print("❌ İçerik boş."); return
    path = save_note(tip, content)
    print(f"\n{TYPES[tip][1]} [{tip.upper()}] → {path.parent.name}/{path.name}\n")

if __name__ == "__main__": main()
```

**Vault yolunu özelleştirmek için:**
```bash
export BRAIN_VAULT="/Users/KULLANICI/Obsidian Vault"
```
Ya da script'teki `VAULT = Path(...)` satırını düzenle.

---

## 📊 Birkan'ın Mevcut Kurulumu (Referans)

| Bileşen | Yol | Durum |
|---------|-----|-------|
| graphify binary | `/Users/birkan/.local/bin/graphify` | ✅ |
| brain CLI | `/Users/birkan/.local/bin/brain` | ✅ |
| Obsidian vault | `/Users/birkan/Desktop/Work /Beynim/Obsidian Beynim/` | ✅ |
| 01 Promt MUHENDISLIGI graph | `...graphify-out/` — 229 node | ✅ |
| 00 Github PROJELERI graph | `...graphify-out/` — 48,696 node | ✅ |
| 2026_Trade Bots graph | `...graphify-out/` — 34,933 node | ✅ |
| Cross-repo graph | `/Users/birkan/Desktop/Work /cross-repo-graph.json` | ✅ |
| Obsidian Graphify export | `Obsidian Beynim/Graphify/` (3 klasör) | ✅ |
| Git hooks | Kurulacak | ⏳ |
| graphify watch | Manuel başlatılıyor | ⏳ |

---

*Oluşturuldu: 2026-05-10 · Graphify + Brain CLI entegrasyon projesi*
