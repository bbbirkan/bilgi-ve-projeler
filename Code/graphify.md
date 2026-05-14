# graphify

**Kaynak**: https://github.com/safishamsi/graphify  
**Yazar**: safishamsi  

---

## Ne İşe Yarar?

`graphify`, yapay zeka kodlama asistanları için tüm projenizi (kodlar, belgeler, PDF'ler, görseller, videolar) bir bilgi grafiğine (knowledge graph) dönüştüren bir araçtır. Dosyalar içinde `grep` ile arama yapmak yerine asistanınızın bu grafik üzerinde sorgulama yapmasını sağlar. 

Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi ve Google Antigravity gibi pek çok platformla entegre çalışır.

Asistanınızda `/graphify .` komutunu çalıştırdığınızda şu üç dosyayı üretir:
- `graph.html`: Tarayıcıda açılıp incelenebilen görselleştirilmiş grafik.
- `GRAPH_REPORT.md`: Projenin temel konseptleri, bağlantıları ve önerilen sorular.
- `graph.json`: Asistanın projeyi sorgulamak için kullanacağı ana veri dosyası.

---

## Nasıl Kurulur?

**Gereksinim:** Python 3.10+

```bash
uv tool install graphifyy && graphify install
# veya: pipx install graphifyy && graphify install
# veya: pip install graphifyy && graphify install
```

Google Antigravity asistanı için projede yapılandırma:
```bash
graphify antigravity install
```

Bu komut asistanınıza projeyle ilgili sorulara cevap vermeden önce `GRAPH_REPORT.md` dosyasını okumasını söyleyen küçük bir konfigürasyon dosyası yazar. 

---

## Temel Komutlar

```bash
/graphify .                        # Mevcut dizin için grafik oluşturur
/graphify ./docs --update          # Sadece değişen dosyaları yeniden çıkarır
/graphify query "what connects auth to the database?"  # Grafikte sorgu yapar
/graphify add https://arxiv.org/abs/1706.03762   # Bir makale ekler
/graphify add <youtube-url>        # Bir videoyu deşifre edip grafiğe ekler
```

---

## Öne Çıkan Özellikler

1. **Geniş Dosya Desteği:** 28 kodlama dili, dokümanlar (.md, .txt vb.), ofis dosyaları (.docx, .xlsx), Google Workspace dosyaları, PDF'ler, görseller ve videolar.
2. **Gizlilik Odaklı:** Kod dosyaları (tree-sitter ile) ve videolar yerel olarak işlenir. Yalnızca belgeler, PDF'ler ve görseller anlamsal çıkarım (semantic extraction) için kullandığınız modelin API'sine gönderilir.
3. **Takım Uyumu:** `graphify-out/` dizinini Git'e ekleyerek tüm ekibin aynı bilgi grafiğiyle çalışması sağlanabilir.
4. **Kavramsal Çıkarım:** Sadece kod ilişkilerini değil, yorum satırlarındaki (`# WHY:`, `# HACK:`) açıklamaları da kodlarla bağlantılı düğümler (node) olarak grafiğe ekler.

---

## Özet

> **graphify** = Tüm projenizin anlamsal ve yapısal ilişkilerini bir bilgi grafiğine (knowledge graph) dönüştüren yapay zeka destekli analiz aracı. Asistanınızın codebase içinde körlemesine arama yapmak yerine projenin mimarisini ve "neden"lerini anlamasını sağlar.
