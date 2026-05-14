# Knowledge Pipeline (Karpathy LLM-Wiki Desen)

**Proje Amacı**: Yapay zeka asistanları (Claude Code vb.) ile ham sohbetleri, makaleleri veya kaynakları düzenli, aranabilir ve sürekli büyüyen bir "LLM Wiki"ye (kişisel bilgi arşivine) dönüştürmek için tasarlanmış bir kalıptır.

## Temel Dosyalar ve İşlevleri

- **`index.html`**: Terminal/matrix estetiğine sahip tek dosyalık bir sunum. SPACE tuşuyla sahneler arası geçiş yapılarak bu yöntemin felsefesi anlatılır.
- **`SKILL.md`**: `llm-wiki` yeteneğini (skill) tanımlayan dokümandır. Yapay zeka asistanına bu dosya gösterildiğinde, asistan nasıl bir "vault" (kasa/arşiv) kuracağını, klasör yapısını ve Markdown iskeletini anlar. Alan bağımsız çalışır (araştırma, kitap okuma, ürün geliştirme vs.).
- **`PROMPTS.md`**: Üç adet hazır (INGEST, QUERY, LINT) komut istemi (prompt) barındırır. Bu prompt'lar kopyala-yapıştır ile asistanı yönlendirmek için kullanılabilir.
- **`karpathy-llm-wiki-rehberi.pdf`**: Sistemin ve LLM kullanım pratiklerinin anlatıldığı detaylı bir rehber belgesidir.

## Çalışma Mantığı (Desen Özeti)

Sistem üç temel aşamadan oluşur:
`RAW (değişmez/ham veri) → WIKI (LLM'nin yazdığı ağ) ← SCHEMA (kuralları belirten anayasa)`

1. **INGEST (İçeri Alma)**: Yeni bir kaynak geldiğinde, yapay zeka bu kaynağı okuyarak wiki'ye entegre eder ve eski sayfalarla yeni bağlantılar (çapraz referanslar) kurar.
2. **QUERY (Sorgulama)**: Kullanıcı sorularını direkt olarak wiki üzerinden cevaplar. Eğer çok iyi ve derinlikli bir cevap üretilirse, bu cevap yeni bir wiki sayfası olarak arşive kaydedilir.
3. **LINT (Bakım/Temizlik)**: Periyodik olarak çalıştırılır. Bilgi ağındaki çelişkileri, bağlantısı kopmuş (orphan) sayfaları ve eksik referansları tespit edip düzenler.

## Nasıl Kullanılır?

1. `SKILL.md` dosyasını yapay zeka asistanınıza (örneğin Antigravity veya Claude Code) okutun.
2. "Bu desene göre bana bir vault kur" komutunu verin.
3. Asistan sizin için klasör yapısını, `CLAUDE.md` kural şemasını ve temel index dosyalarını oluşturacaktır. Ardından `PROMPTS.md` içerisindeki yöntemleri kullanarak kişisel bilgi ağınızı büyütmeye başlayabilirsiniz.
