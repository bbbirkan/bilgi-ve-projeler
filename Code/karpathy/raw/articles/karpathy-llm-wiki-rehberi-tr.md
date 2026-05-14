# LLM Wiki — Yapay Zeka ile İkinci Beyin Kurma

Kaynak: @karpathy  
Tarih: 2026-05-09  
Tür: Rehber / Özet

---

Andrej Karpathy'nin viral fikri: ham veri ver, Claude organize etsin, ilişkilendirsin, sorgulayabilir bilgi tabanı oluştursun. Vektör veritabanı yok, embedding yok. Sadece markdown dosyaları.

Bir kullanıcı 383 dağıtık dosyayı bu yöntemle organize etti → token kullanımı %95 düştü.

## Klasör Yapısı

| Klasör / Dosya | Açıklama |
|---|---|
| `raw/` | Ham veriyi buraya at — makale, transkript, not |
| `wiki/` | Claude'un oluşturduğu organize bilgi |
| `wiki/index.md` | Tüm sayfaların listesi — ana navigasyon |
| `wiki/log.md` | İşlem geçmişi — ne zaman ne eklendi |
| `wiki/hot.md` | Sıcak önbellek — en son bilginin 500 kelimelik özeti |
| `.claude/claude.md` | Proje kuralları — Claude'un davranış rehberi |

## Kurulum Prompt'u

```
You are my LLM wiki agent. Implement Karpathy's LLM wiki idea as my second brain.
This project is specifically for [AMACINI YAZ].
Create the claude.md, the folder structure, the index, and the log.
```

## Kaynak Ekleme Prompt'ları

- İlk kurulum: `You are my LLM wiki agent...`
- Kaynak ekle: `I just added [dosya.md] to raw/. Please ingest it.`
- Sorgulama: `What do all my sources say about [KONU]?`
- Boşluk bul: `Where are the gaps in my knowledge about [KONU]?`
- Bakım: `Run a lint on the wiki. Find inconsistencies, missing links, suggest interesting connections.`

## Baska Projeden Bağlama (claude.md'ye ekle)

```
## Wiki Path
When you need information about me or my business:
1. Go to /Users/[KULLANICI ADI]/[WIKI KLASORU]/wiki/
2. hot.md -> most recent info
3. index.md -> list of all pages
4. Read wiki pages as needed
Do not read the wiki unless you actually need it.
```

## LLM Wiki vs Geleneksel RAG

| | LLM Wiki | RAG |
|---|---|---|
| Altyapı | Sadece markdown | Embedding + vektör DB |
| Kurulum | 5 dakika | Saatler |
| Maliyet | Sadece token | Sürekli compute |
| İlişki | Derin (linkler) | Yüzeysel (benzerlik) |
| En iyi olduğu | Yüzlerce sayfa | Milyonlarca doküman |

## Kullanım Senaryoları

- Rakip analizi
- Kripto/yatırım araştırması
- Kişisel ikinci beyin
- YouTube kanal bilgi sistemi
