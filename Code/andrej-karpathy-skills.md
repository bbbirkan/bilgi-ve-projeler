# andrej-karpathy-skills

Andrej Karpathy'nin LLM kodlama hatalarına dair gözlemlerinden türetilmiş tek bir `CLAUDE.md` dosyası. Claude Code'un yanlış varsayım yapmasını, kodu şişirmesini ve alakasız değişiklikler yapmasını önleyen 4 temel ilkeyi uygular.

## Ne İşe Yarar

Claude Code'un en sık yaptığı 3 hatayı doğrudan hedefler:

> "Modeller senin adına yanlış varsayımlar yapıyor ve bunları sorgulamadan ilerliyor."  
> "Kodu aşırı karmaşık hale getiriyorlar, 100 satırla yapılacak şeyi 1000 satırla yapıyorlar."  
> "Görevle alakasız yorumları ve kodları değiştirip siliyorlar."  
> — Andrej Karpathy

## 4 Temel İlke

| İlke | Ne Engeller |
|------|-------------|
| **Think Before Coding** | Sessiz varsayımlar, gizli karışıklık, tradeoff'ları atlama |
| **Simplicity First** | Gereksiz abstraction, şişirilmiş kod, istenmeyen esneklik |
| **Surgical Changes** | Alakasız kod/yorum değiştirme, kırık olmayan şeyi "düzeltme" |
| **Goal-Driven Execution** | Belirsiz görevler — başarı kriterini tanımla, doğrulayarak ilerle |

**Anahtar insight:** "LLM'lere ne yapacağını söyleme — başarı kriterini ver ve bekle."

## Ne Zaman Kullanılır

- Mevcut bir projeye Claude Code ile dokunurken hata/yan etki yaşıyorsan
- LLM'in sormadan varsayım yapmasından şikayetçiysen
- Diff'lerde istemediğin değişiklikler görüyorsan
- Basit bir şeyi aşırı karmaşık şekilde implement ettiriyorsan

## Kurulum

**Option A — Claude Code Plugin (tüm projelerde geçerli):**
```bash
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Option B — Tek projeye CLAUDE.md olarak:**
```bash
# Yeni proje
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md

# Mevcut projeye ekle
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

**Option C — Cursor:**
`.cursor/rules/karpathy-guidelines.mdc` dosyası repo içinde geliyor, Cursor'da direkt çalışıyor.

## Çalıştığını Nasıl Anlarsın

- ✅ Diff'lerde sadece istenen değişiklikler var
- ✅ Implement etmeden önce clarifying sorular geliyor
- ✅ Kod ilk seferinde sade ve minimal
- ✅ Drive-by refactoring yok

## Dikkat

Bu kurallar **hız yerine dikkat**i tercih eder. Basit tek satırlık düzeltmelerde her ilkeyi zorla uygulamak gerekmez — judgment kullan.

## Repo İçeriği

```
CLAUDE.md          ← Asıl dosya — projeye kopyalanacak
EXAMPLES.md        ← Her ilke için detaylı örnekler
CURSOR.md          ← Cursor entegrasyon rehberi
skills/            ← Plugin skill dosyaları
.claude-plugin/    ← Claude Code plugin tanımı
.cursor/rules/     ← Cursor kuralı
```

**Kaynak:** [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) · MIT
