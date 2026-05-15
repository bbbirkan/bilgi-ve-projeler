# Claude Code: 18 Token Management Hacks
> Kaynak: Nate Herk — "Claude Code Token Limit: 18 Hacks to Double Your Usage"  
> Tarih: 2026-05-15 | Kategori: `Code / AI-Tool Optimization`

---

## Özet
Claude Code'un token ekonomisi "eklemeli" değil "bileşik (compounding)" şekilde çalışıyor. Her mesaj, tüm sohbet geçmişini + system prompt'ları + MCP server tanımlarını + Claude.md'yi yeniden okuyor. 100 mesajlık bir sohbette tokenlerin %98.5'i sadece eski geçmişi tekrar okumaya gidiyor.

---

## 📊 Token Mekaniği

| Metrik | Değer |
|--------|-------|
| Mesaj 1 maliyeti | ~500 token |
| Mesaj 30 maliyeti | ~15,000 token (31x) |
| 30 mesaj sonrası kümülatif | ~250,000 token |
| Gizli overhead | Claude.md, MCP servers, system prompts, loaded files |
| Fenomen | **Lost in the middle** — ortadaki context görmezden gelinir |

> Önemli: şişmiş context sadece pahalı değil, aynı zamanda **daha kötü çıktı** üretir.

---

## 💎 Tier 1 Hacks (9 adet — Herkes uygulayabilir)

1. **Yeni sohbet başlat** — `/clear` kullan. Konu A'dan Konu B'ye geçerken context taşıma.
2. **MCP server'ları disconnect et** — Her mesajda tüm tool tanımları yüklenir. Tek server ~18,000 token.
3. **Prompt'ları tek mesajda topla** — 3 ayrı mesaj = 3 kat maliyet. "Özetle, hataları çıkar, düzelt" hepsini bir mesajda.
4. **Plan mode kullan** — Önce plan sor, sonra kod yaz. Yanlış yolda gitmek en büyük token israfı.
5. **\`/context\` ve \`/cost\` komutlarını kullan** — Gizli token akışını gör.
6. **Status line kur** — Terminalde anlık görünürlük: model, context %, token sayısı.
7. **Dashboard'ı açık tut** — Limit'e yaklaştığını şüpheye bırakma.
8. **Smart paste** — Tüm dosya yerine sadece ilgili fonksiyon/paragrafı yapıştır.
9. **Claude'ı çalışırken izle** — Kötü loop'a girince anında durdur. Kötü loop'ta %80 token boşa gidiyor.

---

## 🥇 Tier 2 Hacks (5 adet — Orta seviye)

1. **Claude.md'yi 200 satır altında tut** — Her mesajda okunur. Index gibi davran: "Daha fazla bilgi şurada".
2. **Cerrahi file reference** — "Repo'yu ara" yerine "`@auth.js` içindeki `verifyUser` fonksiyonuna bak".
3. **%60'da compact et** — Auto compact %95'te tetiklenir, o zamana kadar kalite düşmüş olur. `\`/compact\`` + neyin korunacağını söyle. 3-4 compact sonrası kalite bozulur → `\`/clear\`` + session summary ile devam et.
4. **5 dakikalık cache timeout** — 5 dk'dan uzun ara verince cache bozulur, her şey sıfırdan işlenir. Ara vermeden önce `\`/compact\`` veya `\`/clear\``.
5. **Command output bloat'ı engelle** — 200 commit'lik `git log` çıktısının tamamı context'e girer. Gereksiz komut izinlerini reddet.

---

## 🏆 Tier 3 Hacks (4 adet — Advanced)

1. **Doğru modeli seç**:
   - **Sonnet** → Default kod işi
   - **Haiku** → Sub-agent, format, basit işler
   - **Opus** → Derin mimari planlama (kullanımın %20'sini geçme)
   - **Codex** → Büyük codebase review (Claude token'larından tasarruf)

2. **Sub-agent maliyeti** → Sub-agent 7-10x daha fazla token harcar (her seferinde full context yeniden yüklenir). Ama **Haiku sub-agent** ile araştırma yapıp özet döndürmek pahalı modelin token'larını kurtarır.

3. **Peak saatler** → 8:00-14:00 ET haftaiçi en yoğun. Büyük refactor ve multi-agent işlemlerini off-peak yap. Reset'e yakınsan harca, limite yakınsan mola ver.

4. **Claude.md = System Constitution** — Stable kararlar, mimari kurallar, ilerleme özetleri sakla. "Bugün -> gerçek tarih", tekrarlanan açıklamaları one-line bullet (≤15 kelime) olarak ekle. Self-evolving ama bloat kontrolü yap.

---

## 🧠 Skill Çıkarımı (Reuse İçin)

### Prompt: Claude.md Constitution Template
```
# System Constitution — {proje}

## Teknoloji Stack
- {stack listesi}

## Kod Standartları
- {naming, formatting, testing kuralları}

## 95% Confidence Kuralı
Do not make any changes until you have 95% confidence in what you need to build. 
Ask me follow-up questions until you reach that confidence level.

## Sub-Agent Delegasyon
- 3+ dosya / multi-file analiz gerektiğinde Haiku sub-agent spawn et.
- Sadece özet insight döndür.

## Applied Learning (Self-Evolving)
When something fails repeatedly, when I have to re-explain, or when a workaround 
is found, add a one-line bullet here. Keep each bullet under 15 words. 
No explanations.
```

### Prompt: \`/compact\` Instructions Template
```
\`/compact\`
Preserve the following:
- Active architectural decisions and open questions
- Current file structure and key paths
- TODO items and next steps
- Any unresolved errors or bugs being tracked
Discard: completed explorations, old code drafts, confirmed-fixed issues.
```

### Prompt: Token Dashboard Checklist
```
1. \`/context\` → MCP overhead, loaded files, history'i gör
2. \`/cost\` → Anlık session maliyeti
3. Claude.md satır sayısını kontrol et (<200)
4. Bağlı MCP server sayısını kontrol et (sadece gerekli olanlar)
5. Status line: context % 60'ı aştyor mu?
```

---

## 📝 Raw Notlar
- "Most people don't need a bigger plan, they need to stop resending their entire conversation history 30 times."
- "It's not a limits problem, it's a context hygiene problem."
- Hitting limit negatif algılanmamalı — power user olduğunun göstergesi.
- Bir geliştirici 100+ mesajlık sohbeti takip etmiş: tokenlerin %98.5'i eski history.

---

*Son güncelleme: 2026-05-15 | Birkan Otonom Pipeline*