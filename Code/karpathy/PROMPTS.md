# Ready-to-Use Prompts

LLM-Wiki deseninin tüm operasyonları için hazır prompt'lar. Beş prompt, iki kategori:

**Kurulum (bir kerelik, başlangıçta):**
- [SETUP — Kontrollü](#setup--kontrollü) — adım adım, onayla ilerleyen güvenli kurulum
- [SETUP — Otomatik](#setup--otomatik) — tek pass'te her şey kurulu + ilk ingest'ler yapılmış

**Günlük operasyonlar (her zaman):**
- [INGEST](#ingest--yeni-kaynak-ekle) — yeni kaynak ekle
- [QUERY](#query--wikiye-soru-sor) — wiki'ye soru sor
- [LINT](#lint--sağlık-kontrolü) — periyodik sağlık kontrolü

Herhangi bir Obsidian vault ile çalışır. `{{ }}` içindeki placeholder'ları kendi ayarlarınla değiştir, Claude Code'a (veya başka bir LLM ajanına) yapıştır.

---

## Hangi kurulum prompt'unu kullanmalıyım?

| Durum | Öneri |
|---|---|
| İlk defa vault kuruyorsun, sistemin nasıl çalıştığını görmek istiyorsun | **SETUP — Kontrollü** |
| Şema dosyasını (CLAUDE.md) elle iterate edip görmek istiyorsun | **SETUP — Kontrollü** |
| Küçük bir test ile başlamak istiyorsun | **SETUP — Kontrollü** |
| Tam otomatik olmasını istiyorsun, arada durmasın | **SETUP — Otomatik** |
| Büyük bir kaynak arşivini (örn. 10+ JSONL, 50+ makale) tek seferde işlemek istiyorsun | **SETUP — Otomatik** |
| Vault yapısından zaten eminsin, sadece kurulup bitsin istiyorsun | **SETUP — Otomatik** |

**Öneri**: İlk kez kuruyorsan **Kontrollü** ile başla, gör nasıl çalışıyor, sonraki projelerde **Otomatik**'e geç.

---

## SETUP — Kontrollü

**Ne zaman kullan:** İlk defa vault kuruyorsan, şemayı elle görmek istiyorsan, küçük bir yapı ile başlayıp büyütmek istiyorsan. Bu prompt klasörleri kurar, `CLAUDE.md` yazar, mevcut kaynakları sayar ve **durur**. İlk ingest'i sen manuel olarak tetiklersin.

```
HEDEF KLASÖR: {{VAULT_YOLU}}

Bu klasör zaten mevcut. İçine yeni bir alt-klasör OLUŞTURMA. Doğrudan bu
klasörün içine kur. Tüm içerik {{DIL}} olacak.

Görevler:

1) {{VAULT_YOLU}} içinde klasör yapısını kur:
   - raw/{{KAYNAK_KLASORU}}/   (ham kaynaklar, DOKUNULMAZ)
   - raw/docs/                 (statik dökümanlar)
   - sources/{{KAYNAK_KLASORU}}/  (her ham kaynak için bir özet sayfası)
   - entities/                 (dosyalar, fonksiyonlar, servisler, kişiler)
   - concepts/                 (soyut kavramlar)
   - decisions/                (atomik kararlar — her karar = tek sayfa)
   - {{SORUN_KLASORU}}/        (düzeltilen sorunlar: kök neden + fix)
   - syntheses/                (üst düzey genel bakış sayfaları)
   - archive/                  (eskimiş sayfalar, asla silinmez)
   Her klasöre bir .gitkeep koy.

2) {{VAULT_YOLU}} kök dizinine iki dosya oluştur:
   - index.md   (boş iskelet, kategori bazında içerik kataloğu)
   - log.md     (boş iskelet, append-only zaman damgalı olay kaydı)

3) {{VAULT_YOLU}}/CLAUDE.md dosyasını yaz. İçeriği:
   - Amaç: {{PROJE_ADI}} için kalıcı bilgi arşivi. {{PROJE_AMACI}}
   - Dil: TÜM wiki sayfaları {{DIL}}. Teknik terimler İngilizce kalabilir.
   - Naming: kebab-case dosya adları
   - Sayfa formatı: YAML frontmatter (title, tags, source, date, status)
     + H1 başlık + içerik + "## Sources" + "## Related"
   - llm-wiki skill'ini temel alan üç operasyon workflow'u (ingest/query/lint),
     {{PROJE_ADI}}'a uyarlanmış
   - INGEST özel durumu: raw/{{KAYNAK_KLASORU}}/ içindeki {{KAYNAK_TIPI}}
     dosyaları. Her kaynak için: içeriği tara, ana konuyu çıkar,
     sources/{{KAYNAK_KLASORU}}/YYYY-MM-DD-slug.md olarak özet yaz
     (amaç, ne yapıldı, değişenler, kararlar, sorunlar, açık konular),
     index'i güncelle, bahsedilen entity/concept/decision/sorun sayfalarını
     çapraz-güncelle.
   - Hard rules: raw/ asla değiştirilmez, kaynaksız iddia yasak, sayfa
     silme yok (archive'a taşı), çelişkiler "## ÇELİŞKİ" başlığıyla
     işaretlenir, silinmez.

4) Mevcut kaynakları SAY ama HENÜZ ingest ETME:
   ls {{KAYNAK_TARAMA_YOLU}} 2>/dev/null | wc -l

5) Bitince listele: hangi klasörleri oluşturdun, hangi dosyaları yazdın,
   CLAUDE.md'nin kaç satır olduğunu, bulunan kaynak sayısını. Otomatik
   ingest BAŞLATMA — ben ilk ingest'i manuel olarak tetikleyeceğim.
```

### Placeholder'lar

| Placeholder | Açıklama | Örnek |
|---|---|---|
| `{{VAULT_YOLU}}` | Vault'un tam yolu | `/Users/you/my-vault` |
| `{{PROJE_ADI}}` | Projenin/vault'un adı | `my-research`, `book-notes` |
| `{{PROJE_AMACI}}` | Tek cümlelik amaç | `Yapay zeka araştırmalarını biriktiren kalıcı arşiv` |
| `{{KAYNAK_KLASORU}}` | Ham kaynakların alt klasörü | `sessions`, `articles`, `papers`, `transcripts` |
| `{{KAYNAK_TIPI}}` | Kaynakların tipi | `JSONL transkriptleri`, `PDF makaleleri`, `markdown notları` |
| `{{KAYNAK_TARAMA_YOLU}}` | Mevcut kaynakları saymak için glob | `~/.claude/projects/*/*.jsonl`, `~/Downloads/*.pdf` |
| `{{SORUN_KLASORU}}` | Sorun/bug klasörünün adı | `bugs`, `issues`, `lessons`, `mistakes` |
| `{{DIL}}` | Wiki dili | `Türkçe`, `English` |

---

## SETUP — Otomatik

**Ne zaman kullan:** Tek pass'te her şeyin kurulmasını ve ilk kaynakların ingest edilmesini istiyorsan. Prompt kaynak seçimini kendisi yapar, ingest eder, sentez sayfaları yazar, lint çalıştırır ve rapor verir. Arada durmaz. Büyük bir arşivle başlayacaksan veya vault yapısından eminsen idealdir.

```
HEDEF: {{VAULT_YOLU}} — bu klasör zaten var, içine kur. llm-wiki skill'ini
tam olarak uygula. Tüm içerik {{DIL}} olacak. Tek pass'te her şeyi kur
VE ilk ingest'leri yap. Bana soru sorma, sen seç, sen karar ver, sen uygula.
Sonuçta bitmiş çalışan bir vault teslim et.

PHASE 1 — SETUP

1) {{VAULT_YOLU}} içinde şu klasörleri oluştur, her birine .gitkeep koy:
   raw/{{KAYNAK_KLASORU}}/, raw/docs/, sources/{{KAYNAK_KLASORU}}/,
   entities/, concepts/, decisions/, {{SORUN_KLASORU}}/, syntheses/, archive/

2) {{VAULT_YOLU}}/index.md ve {{VAULT_YOLU}}/log.md iskelet dosyalarını
   oluştur (kategori başlıkları + boş altlar).

3) {{VAULT_YOLU}}/CLAUDE.md yaz. İçerik llm-wiki skill'ini temel alsın,
   {{PROJE_ADI}}'a uyarlansın:
   - Amaç: {{PROJE_ADI}} için kalıcı bilgi arşivi. {{PROJE_AMACI}}
   - Dil: tüm sayfalar {{DIL}}
   - Naming: kebab-case
   - Sayfa formatı: YAML frontmatter (title, tags, source, date, status)
     + H1 + içerik + "## Sources" + "## Related"
   - {{PROJE_ADI}}'a uyarlanmış Ingest / Query / Lint workflow'ları
   - Hard rules: raw/ immutable, kaynaksız iddia yasak, silme yok
     (archive), çelişkiler "## ÇELİŞKİ" başlığıyla işaretlenir

PHASE 2 — KAYNAK SEÇİMİ

4) {{KAYNAK_TARAMA_YOLU}} yolundaki kaynakları tara. Aşağıdaki kriterleri
   kullanarak EN İYİ {{KAYNAK_SAYISI}} dosyayı kendi başına seç:
   - En az {{MIN_BOYUT}} boyutunda (küçük/test kaynakları elenir)
   - İçeriğinde {{ANAHTAR_KELIMELER}} gibi proje-ilgili kelimeler geçen
   - Tarihi en yeniden eskiye doğru öncelikli
   - Farklı konuları kapsasın (tek bir konuya sıkışmasın)
   Bu dosyaları raw/{{KAYNAK_KLASORU}}/ içine SEMBOLIK LINK olarak bağla
   (ln -s). Orijinali taşıma, kopyalama — sadece link. raw/ immutable kalır.

PHASE 3 — INGEST

5) Seçtiğin dosyaları TEK TEK CLAUDE.md'deki ingest workflow'una göre işle.
   Her biri için:
   a) Dosyayı oku, ana konuyu çıkar
   b) sources/{{KAYNAK_KLASORU}}/YYYY-MM-DD-<slug>.md yaz: frontmatter +
      goal + what-was-done + files-changed + decisions + issues + open-threads
      + sources referansı
   c) Bahsedilen her entity (dosya yolu, fonksiyon, servis, API, kişi) için
      entities/ altında sayfa oluştur veya mevcudu güncelle. Çift yönlü
      link kur.
   d) Her mimari/ürün kararı için decisions/ altında atomik sayfa
   e) Her sorun/düzeltme için {{SORUN_KLASORU}}/ altında sayfa
      (kök neden + fix + ilgili dosyalar)
   f) Her soyut kavram için concepts/ altında sayfa oluştur veya güncelle
   g) log.md'ye "## [YYYY-MM-DD] ingest | <slug>" girişi, altında dokunulan
      dosyaların listesi
   h) index.md'yi her ingest sonrası güncelle

PHASE 4 — SYNTHESIS

6) Tüm ingest'ler bittikten sonra şu yüksek seviyeli sentez sayfalarını yaz:
{{SENTEZ_SAYFALARI}}
   Her sentez, ilgili sources / decisions / issues / entities / concepts
   sayfalarına link versin.

PHASE 5 — LINT

7) Kurulan wiki üzerinde bir lint pass çalıştır. lint-report.md yaz:
   çelişkiler, orphan sayfalar, eksik cross-ref'ler, kendi sayfası olmayan
   kavramlar. Otomatik düzeltme yapma, sadece raporla.

PHASE 6 — REPORT

8) Bitince özetle:
   - Kaç klasör oluşturuldu
   - Kaç kaynak seçildi ve hangi kriterlere göre
   - Her kategori için kaç sayfa (sources, entities, concepts, decisions,
     sorunlar, syntheses)
   - Toplam kaç cross-reference kuruldu
   - lint-report.md'deki bulgu sayısı
   - Obsidian'ı nasıl açacağım (vault path)

KURALLAR

- raw/ klasörüne ASLA yazma, sadece sembolik link + oku
- Kaynaksız iddia yazma — her bulgu ilgili kaynağa referans versin
- Hiçbir adımda bana soru sorma, karar ver ve devam et
- Hata olursa dur, log'la, devam et (tek bir kaynağın bozulması tüm
  pass'i durdurmasın)
- Bitince tek bir özet mesajı ver
```

### Placeholder'lar

| Placeholder | Açıklama | Örnek |
|---|---|---|
| `{{VAULT_YOLU}}` | Vault'un tam yolu | `/Users/you/my-vault` |
| `{{PROJE_ADI}}` | Projenin adı | `my-research`, `vibeapp` |
| `{{PROJE_AMACI}}` | Tek cümlelik amaç | `Backend + iOS projesinin bilgi arşivi` |
| `{{KAYNAK_KLASORU}}` | Ham kaynak alt klasörü | `sessions`, `articles`, `papers` |
| `{{KAYNAK_TARAMA_YOLU}}` | Mevcut kaynakları nerede ara | `~/.claude/projects/*/*.jsonl` |
| `{{KAYNAK_SAYISI}}` | İlk batch'te kaç kaynak | `5`, `8`, `15` |
| `{{MIN_BOYUT}}` | Minimum dosya boyutu | `500 KB`, `1 MB` |
| `{{ANAHTAR_KELIMELER}}` | Filtre kelimeleri (virgülle) | `deploy, oauth, bug, fix, auth` |
| `{{SORUN_KLASORU}}` | Sorun klasörü adı | `bugs`, `issues`, `lessons` |
| `{{SENTEZ_SAYFALARI}}` | Hangi sentez sayfaları yazılsın | `- syntheses/architecture.md — mimari genel bakış\n   - syntheses/security.md — güvenlik özeti` |
| `{{DIL}}` | Wiki dili | `Türkçe`, `English` |

---

## INGEST — Yeni kaynak ekle

**Ne zaman kullan:** Vault kurulduktan sonra, her yeni kaynak eklediğinde. Makale, toplantı transkripti, yeni bir oturum, okuduğun bir bölüm — hepsi için aynı prompt.

```
HEDEF: {{VAULT_YOLU}}

{{VAULT_YOLU}}/raw/ klasörüne yeni bir kaynak ekledim. En son değiştirilen
dosyayı bul (ls -lt), oku ve {{VAULT_YOLU}}/CLAUDE.md'deki ingest workflow'una
göre işle.

Adımlar:
1) Yeni kaynağı oku. Çıkar: ana konu, anahtar bulgular, bahsedilen entity'ler
   (kişiler, dosyalar, servisler, yerler), kavramlar, kararlar ve varsa
   sorunlar.
2) Bana 5 maddeli bir özet göster ve hiçbir şey yazmadan önce onay iste.
3) Onay verdiğimde:
   a) {{VAULT_YOLU}}/sources/<kategori>/<YYYY-MM-DD>-<slug>.md dosyası yaz.
      YAML frontmatter (title, tags, source, date, status) + H1 başlık +
      bölümler (Amaç, Ne yapıldı, Anahtar noktalar, Kararlar, Açık konular,
      Kaynaklar, İlgili).
   b) Bahsedilen her entity için {{VAULT_YOLU}}/entities/ altında sayfa
      oluştur (yoksa) veya güncelle (varsa). Çift yönlü link kur.
   c) Her karar için {{VAULT_YOLU}}/decisions/ altında atomik bir sayfa
      (tek karar = tek sayfa).
   d) Her sorun veya öğrenilen ders için {{VAULT_YOLU}}/{{SORUN_KLASORU}}/
      altında sayfa.
   e) Her soyut kavram için {{VAULT_YOLU}}/concepts/ altında sayfa oluştur
      veya güncelle.
   f) {{VAULT_YOLU}}/index.md'yi ilgili kategori bölümlerinde güncelle.
   g) {{VAULT_YOLU}}/log.md'ye "## [YYYY-MM-DD] ingest | <slug>" girişi ekle,
      altında dokunulan her dosyanın listesi.
4) Bitince özetle: kaç sayfa oluşturuldu, kaç sayfa güncellendi, kaç
   cross-reference kuruldu. Obsidian'da açıp kontrol etmem için dosya
   listesi ver.
5) raw/ klasörüne ASLA yazma, sadece oku.

Dil: {{DIL}}
```

### Placeholder'lar

| Placeholder | Açıklama | Örnek |
|---|---|---|
| `{{VAULT_YOLU}}` | Vault'un tam yolu | `/Users/you/vault` |
| `{{SORUN_KLASORU}}` | Sorun klasörünün adı (yoksa (d) adımını sil) | `bugs`, `issues`, `lessons` |
| `{{DIL}}` | Wiki dili | `Türkçe`, `English` |

---

## QUERY — Wiki'ye soru sor

**Ne zaman kullan:** Wiki'den bilgi çekmek istediğinde. Özellik: iyi cevaplar otomatik olarak yeni sayfa olarak geri-dosyalanır, böylece keşiflerin de birikim yapar.

```
HEDEF: {{VAULT_YOLU}}

Aşağıdaki soruya wiki üzerinden cevap ver:

SORU: {{SORUNUZ}}

Adımlar:
1) Önce {{VAULT_YOLU}}/index.md'yi oku. Sorunun hangi kategorilerde
   aranması gerektiğini belirle.
2) İlgili sayfaları bul (sources/, entities/, concepts/, decisions/,
   syntheses/ altında) ve tamamını oku.
3) Cevabı sentezle. KURAL: her önemli iddia için kaynak referansı ver —
   hangi wiki sayfasından geldiği ve o sayfanın hangi raw kaynağa dayandığı.
4) Cevap bir karşılaştırma, analiz veya yeni bir sentez içeriyorsa,
   SADECE sohbette bırakma — {{VAULT_YOLU}}/syntheses/ veya
   {{VAULT_YOLU}}/concepts/ altında yeni bir sayfa olarak geri dosyala.
   Sayfa YAML frontmatter ile başlasın ve kullanılan tüm kaynak sayfalara
   link versin.
5) Eğer wiki'de cevap bulunamıyorsa, hangi bilgi eksik söyle ve hangi
   kaynakları ingest etmem gerektiğini öner.
6) {{VAULT_YOLU}}/log.md'ye "## [YYYY-MM-DD] query | <kısa soru özeti>"
   girişi ekle. Eğer geri-dosyalama yaptıysan, o dosyanın yolunu da belirt.
7) Cevabı bana göster ve yeni oluşturduğun veya güncellediğin sayfaların
   listesini ver.

Dil: {{DIL}}
```

### Placeholder'lar

| Placeholder | Açıklama | Örnek |
|---|---|---|
| `{{VAULT_YOLU}}` | Vault'un tam yolu | `/Users/you/vault` |
| `{{SORUNUZ}}` | Asıl soru | `Deploy nasıl çalışıyor?` |
| `{{DIL}}` | Cevap dili | `Türkçe`, `English` |

---

## LINT — Sağlık kontrolü

**Ne zaman kullan:** Haftalık veya aylık olarak. Wiki büyüdükçe çelişkiler, eskimiş iddialar ve orphan sayfalar birikir — bu prompt hepsini tarayıp rapor eder.

```
HEDEF: {{VAULT_YOLU}}

Wiki üzerinde tam bir sağlık kontrolü (lint pass) çalıştır.
{{VAULT_YOLU}}/raw/ HARİÇ tüm markdown dosyalarını tara.

Ara:
1) ÇELİŞKİLER: iki sayfa aynı konuda birbirine zıt iddialar içeriyor mu?
2) ESKİMİŞ İDDİALAR: son {{ESKI_ESIK_GUN}} günde raw/ içine eklenen
   kaynaklar, mevcut sayfaları geçersiz kılmış olabilir mi?
3) YETİM SAYFALAR: hiçbir yerden [[link]] almayan sayfalar. Bunlar ya
   bir hub'a bağlanmalı, ya index'e eklenmeli, ya da arşivlenmeli.
4) EKSİK KAVRAM SAYFALARI: wiki'de en az {{MIN_BAHIS_SAYISI}} sayfada
   geçen ama kendi sayfası olmayan kavramlar.
5) TEK-YÖNLÜ CROSS-REFERENCELAR: A sayfası B'ye link veriyor ama B,
   A'yı "İlgili" bölümünde saymıyor.
6) KAYNAK BOŞLUKLARI: önemli ama sadece tek bir raw kaynağa dayanan
   sayfalar. Ek doğrulama önerisiyle işaretle.

Bulguları {{VAULT_YOLU}}/lint-report.md dosyasına yaz. Her bulgu için:
- Kategori (çelişki / eskimiş / yetim / eksik-kavram / tek-yönlü-xref /
  zayıf-kaynak)
- Etkilenen dosya(lar) ve mümkünse satır numarası
- Somut düzeltme önerisi (hangi dosya nasıl güncellenmeli)
- Öncelik (yüksek / orta / düşük)

OTOMATIK DÜZELTME YAPMA. Sadece raporla. Ben raporu okuyup hangi
düzeltmeleri yapacağıma karar vereceğim.

Bitince {{VAULT_YOLU}}/log.md'ye "## [YYYY-MM-DD] lint | N bulgu
(Y:x O:y D:z)" girişi ekle.

Özet: kaç dosya tarandı, her kategoride kaç bulgu var, en kritik 3
bulgu ne.

Dil: {{DIL}}
```

### Placeholder'lar

| Placeholder | Açıklama | Örnek |
|---|---|---|
| `{{VAULT_YOLU}}` | Vault'un tam yolu | `/Users/you/vault` |
| `{{ESKI_ESIK_GUN}}` | Kaç günü "yakın zaman" sayalım | `30`, `60` |
| `{{MIN_BAHIS_SAYISI}}` | Kaç sayfada geçince kavram sayfası olmalı | `3`, `5` |
| `{{DIL}}` | Rapor dili | `Türkçe`, `English` |

---

## Kullanım tavsiyeleri

### Shell alias olarak sakla

Her seferinde prompt'u yapıştırmak yerine, `~/.zshrc` veya `~/.bashrc` dosyana kısayol ekle:

```bash
alias wiki-ingest='claude -p "$(cat ~/wiki-prompts/ingest.txt)"'
alias wiki-query='claude -p "$(cat ~/wiki-prompts/query.txt)"'
alias wiki-lint='claude -p "$(cat ~/wiki-prompts/lint.txt)"'
```

Beş prompt'u `~/wiki-prompts/` altında ayrı txt dosyalarına kaydet, aliaslarla çağır.

### Claude Code slash command olarak sakla

Daha zarif bir yöntem: `~/.claude/commands/` altına her biri için bir `.md` dosyası:

```
~/.claude/commands/wiki-ingest.md
~/.claude/commands/wiki-query.md
~/.claude/commands/wiki-lint.md
```

Claude Code içinde `/wiki-ingest` yazarak çağırırsın. Slash komutlar argüman da alabilir (sorunu query'ye parametre olarak geçirebilirsin).

### Cron'a bağla (otomatik lint)

Her Pazar sabah 9'da otomatik lint pass:

```bash
(crontab -l 2>/dev/null; echo "0 9 * * 0 cd ~/vault && claude -p \"\$(cat ~/wiki-prompts/lint.txt)\"") | crontab -
```

---

## Daha fazlası

- **Desen detayları:** [SKILL.md](./SKILL.md)
- **Sunum (canlı):** [selmakcby.github.io/knowledge-pipeline](https://selmakcby.github.io/knowledge-pipeline/)
- **Kaynak kod:** [github.com/selmakcby/knowledge-pipeline](https://github.com/selmakcby/knowledge-pipeline)

## Lisans

MIT. İstediğin gibi kullan, değiştir, paylaş.
