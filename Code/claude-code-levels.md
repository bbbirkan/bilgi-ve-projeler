# Claude Code: 5 Levels from Enthusiast to Architect
> Kaynak: Nate Herk — "Every Level of Claude Code Explained in 21 Minutes"  
> Tarih: 2026-05-15 | Kategori: `Code / AI-Tool Progression`

---

## Özet
Claude Code kullanımı 5 seviyeye ayrılır. Her seviyenin bir **cheat code**'u vardır — bu kod bir sonraki seviyeye atlamanın anahtarıdır. Bu doküman her seviyenin özelliklerini, sınırlarını ve bir sonraki seviyeye geçiş stratejisini derler.

---

## 💎 Level 1 — Enthusiast (30 dk tasarruf/gün)

**Tanim:** Aç, soru sor, cevap al, kapat. E-posta yazdırma, hızlı script, açıklama isteme.

**Ne kaçırılıyor:**
- Claude görsel okuyabilir (screenshot paste etmek yerine yazı yazılıyor)
- Context across conversations
- Project/connector yapısı

**Cheat Code → Level 2:**
> **İlk projeni oluştur.** Tekrar gelen bir iş alanı seç (işletme, yan proje). Referans dokümanları at, kısa system prompt yaz (İkim, nasıl cevap istiyorum). Artık her sohbet önceden yüklenmiş başlıyor.

---

## 💎 Level 2 — Beginner (5+ saat tasarruf/hafta)

**Tanim:** Proje merkezli çalışma. Claude stateless değil, devamlılık kazanıyor.

**6 özellik:**

1. **Memory + Past Chat Search**
   - Roller, tercihler, haftalar önceki kararlar hatırlanır.
   - Memory tüm planlarda ücretsiz. Chat search Pro'ya özel.

2. **Connectors (50+)**
   - Slack, Google Drive, Gmail, GitHub, Notion, Calendar.
   - Artık copy-paste değil, Claude direkt gidip getiriyor.

3. **File Creation**
   - Excel (formüllü), PowerPoint, Word, PDF — gerçek indirilebilir dosyalar.
   - Free kullanıcılar da yapabilir.

4. **Artifacts (persistent)**
   - Kalıcı depolama, sessionlar arası veri hatırlama.
   - Claude API'sini doğrudan çağrabilir (app kendi kendine düşünebilir).
   - Public link ile paylaşılabilir → kod bilmeyen kişi işlevsel araç üretir.

5. **Inline Visuals**
   - Sohbet içinde canlı grafik/diagram.
   - CSV'den anlık görselleştirme.
   - Artifacts'tan farkı: ephemeral (sohbetle birlikte evrimleşiyor, dosya olarak kaydolmuyor).

6. **Office Add-ins (Excel/Word/PPT)**
   - Claude, gerçek Microsoft uygulamaları içinde çalışır.
   - Excel'de çoklu sekme okuma, formül açıklama, bağımlılıkları koruyarak edit.
   - Nisan 2026 itibariyle 3 uygulama context paylaşıyor.

**Ücretsiz vs Ödemeli:**
- Free: Memory, File Creation, Inline Visuals
- Pro+: Past Chat Search, Persistent Artifacts, Office Add-ins

**Sınır:** Claude makinede işlem yapmıyor. Hâlâ çıktıyı başka yere kopyalıyorsun, el ile çalıştırıyorsun.

**Cheat Code → Level 3:**
> **Claude Desktop ↔ Co-Work tabına geç.** Terminal bilgisi gerekmez. Dosya sistemi erişimi başlıyor.

---

## 💎 Level 3 — Intermediate (10+ saat tasarruf/hafta)

**Tanim:** Claude bilgisayarında fiilen iş yapıyor. n8n zihniyetli kullanıcılar için doğal.

**5 özellik:**

1. **File System Access**
   - İzole VM içinde kod çalıştırır ama senin dosyalarını okur/yazar.
   - Örn: "Downloads klasöründeki 3 aylık PDF'leri türüne göre sırala, yeniden adlandır, özet çıkar."

2. **Skills**
   - Tekrar kullanılabilir markdown iş akışları.
   - 100+ yayınlanmış skill (16+ Anthropic resmi + topluluk).
   - Co-Work ↔ Chat ↔ Claude Code arasında taşınabilir.
   - Kaynak güvenilirliğine dikkat.

3. **Scheduled Tasks**
   - `\`/schedule\`` ile belirli aralıklarla görev (8AM stand-up, Pazartesi rakip brief'i).
   - Makinenin uyanık ve Desktop app açık olması gerekir.
   - Cloud-based alternative: **Routines** (Level 5'te).

4. **Mobile Control (Dispatch)**
   - Telefon-desktop eşleşmesi.
   - Toplu taşımada/sporda görev gönder, Claude masaüstünde işleyip bitince ping atar.

5. **Claude Design**
   - Pro plan ile gelen ayrı Anthropic Labs ürünü.
   - Plain English prototip/slide/landing page tasarımı.
   - Marka sistemini okur (renk, font, tipografi) → generic AI görüntüsü çıkmaz.
   - Handoff bundle: Claude Code veya Canva'ya aktarılabilir.
   - Kod bilmeyen → Claude Design → Claude Code = fikirden ürüne pipeline.

**Ekstra:**
- **Plugins:** Skill + Connector + Hook paketi. Marketplace var.
- **Computer Use:** Görsel navigasyon (Mac & Windows).

**Sınır:** Co-Work güvenli ama daha az hassas. $5000+ projeler için version control ve engineering rigor gerekir.

**Cheat Code → Level 4:**
> **Klasör yapısı kur:** `about-me`, `templates`, `projects`, `outputs`. Claude'ı önce about-me ile tanıştır. "Templates'e asla dokunma. Çıktı her zaman outputs'a."

---

## 💎 Level 4 — Advanced ($5K–$15K projeler)

**Tanim:** Mümün paralel iş akışı. Boris Cherny (Claude Code builder'u) günde **en az 5 paralel session** çalıştırıyor. Her biri izole workspace, birbiriyle çakışmıyor.

**5 özellik:**

1. **Claude.md (Claw.md)**
   - Her session başlangıcında okunan proje markdown'ı.
   - Tech stack, naming conventions, kurallar (“never do X”).
   - **Kritik kural:** <200 satır tut. Fazla detay ayrı dosyalara at, `@filename` ile referans ver.
   - **Sırları:** Her hata sonrası "Claude.md'yi güncelle, bu hatayı tekrar yapma." → Haftalar içinde kendi kendine öğrenir.

2. **Plan Mode**
   - `Shift + Tab` (2 kez) → Plan mode.
   - **Opus Plan:** Opus plan yapar, Sonnet işletir. Maliyet yılınır, kalite korunur.

3. **Sub-Agents**
   - Her biri kendi context window'unda izole.
   - Örn: bir test, bir güvenlik review, bir dokümantasyon ajanı.
   - Paralel çalışabilirler.

4. **Worktrees**
   - `claude-worktree <feature-name>` → izole git workspace + branch.
   - 3-4 paralel feature üzerinde aynı anda çalışılabilir.

5. **MCP (Asterisk ile)**
   - Önce CLI, sonra API endpoint, sonra Skill, en son MCP.
   - **Tool Search (Ocak 2026):** MCP overhead %10'a geçince auto-defer. 85% overhead azalımı.
   - **Sıralama:** CLI > API > Skill > MCP

**Power Moves:**
- **\`/compact\` + \`/context\`:** Proaktif compact. Prompt caching otomatik. Maliyet %60-90 düşer.
- **Auto Mode + Focus:** `Shift + Tab` → auto mode (safe commands classifier ile). `/focus` → sadece final result göster.
- **Verification Loop:** Claude'ın kendi işini test etmesini sağla. Boris Chrome extension ile UI test yapıyor, 2-3x kalite artışı.
- **Custom Commands:** Tekrarlanan prompt'ı slash command yap. Örn: `/commit-push-pr` (Boris günde onlarca kez kullanıyor). `~/.claude/commands/` altında saklanır.
- **\`/re\` (Escape 2x):** Başarısız denemeyi context'ten tamamen silip geri dön.
- **\`/btw\`:** Ana akışı bozmadan hızlı soru sor.
- **\`/branch\`:** Conversation'ı o noktada çatalla (git gibi). Bir yaklaşım dene, geri dön, başka dene.
- **\`/insights\`:** Son 1 aylık kullanım raporu. Tekrarlayan işleri skill'şa çevir, token israfını bul.
- **\`/output-style\`:** Personality değiştir (reviewer mode, no-fluff, documentation writer).

**Sınır:** Paralel işleri manuel yönetmek zorundasın. Kendin bottleneck oluyorsun. "Babysitting" modu.

**Cheat Code → Level 5:**
> **Her hafta tekrar ettiğin en rutin işlem nedir?** Review, dependency check, manuel skill çalıştırma... O rutini bul, onu **ilk otomasyonun** yap.

---

## 💎 Level 5 — Architect (24/7 Infrastructure)

**Tanim:** Laptop kapalıyken bile iş oluyor. PR açılınca Claude review yapıp comment yazıyor. Sen telefonuna bakınca her şey bitmiş.

**3 özellik:**

1. **Cloud Routines**
   - Anthropic cloud'ünda çalışan, makine bağımsız konfigürasyonlar.
   - Trigger: Schedule, API call, GitHub event.
   - Örn: Her gün 8AM backlog triage, her PR açılışında review.

2. **Hooks**
   - Lifecycle event'lerinde çalışan güvenlik rayları.
   - Pre-tool: Tehlikeli komutu engelle.
   - Post-edit: Oto-format.
   - Stop: Slack ping, ses bildirimi.

3. **Channels**
   - Terminal dışından kontrol: Discord, Telegram, iMessage.
   - Tek yönlü: External event → Claude (takvim randevusu → briefing hazırla)
   - Çift yönlü: Telefondan mesaj at → Claude gerçek codebase üzerinde çalışır.

**Ekstra Layer'lar:**
- **Headless Mode:** `claude -p "prompt"` → no human session. Pipe anywhere (Slack, Datadog, başka ajan).
- **Agent SDK:** Python/TS kütüphaneleri → Claude Code engine üzerine kendi ürününü kur.
- **Remote Control:** `/remote-control` → QR kod ile telefondan session yönet. Yürüyüşte kod yaz.
- **Memory Consolidation (autodream):** Arka plan sub-agent memory dosyalarını budar. Çelişkiyi siler, duplicate merge eder, "yesterday"→gerçek tarihe çevirir.
- **Task Budgets (Opus 4.7 beta):** Token hedefi verilir, ajan bütçeyi görüp kendini regüle eder.
- **Agent Teams (experimental):** Çoklu Claude koordinasyonu. Shared channel, task list, birbirlerine challenge. Çok token yer ama yüksek kalite.
- **MCP + Ato:** Agent-agent iletişim protokolleri.

**Sınır:** Teknik değil, **güven.** Herkes routine kurabilir ama yapmaz. "Uykudayken araba kullanmak" gibi hissediyor.

**Çözüm:** Boş otoparktan başla. Low-stakes rutin (günlük stand-up özeti, sadece sana giden). Günlerce izle, dokunma. Güven kazandıkça 10 tane daha ekle.

> "Trust is the main thing standing between level four and level five. It's a skill that takes reps and time, not a feature you install."

---

## 🎯 Reusable Cheatsheet

| Seviye | Kim | Anahtar Özellik | Sınır | Cheat Code |
|--------|-----|------------------|-------|------------|
| 1 | Enthusiast | Chat Q&A | Stateless | Proje oluştur |
| 2 | Beginner | Project + Connectors | Manuel copy-paste | Co-Work tabına geç |
| 3 | Intermediate | File system access | Hassasiyet eksikliği | Klasör yapısı kur |
| 4 | Advanced | Paralel worktrees | Manuel yönetim | Rutini bul, otomasyona başla |
| 5 | Architect | 24/7 cloud routines | Güven sorunu | Low-stakes routine ile başla |

---

## 📝 Context'ten Çıkarılan Taktiksel Notlar

- **Token Stack Sıralaması (En ucuz → En pahalı):** CLI > API Endpoint > Skill > MCP
- **Paralel Session Sayısı:** Boris 5+ session. 3-4 worktree sweet spot.
- **Claude.md limit:** <200 satır. Her mesajda okunur.
- **Verification Loop:** En yüksek ROI alışkanlık (Boris çıktısı: 2-3x kalite).
- **/insights çalıştırma sıklığı:** Aylık.
- **Topluluk envanteri:** 5000+ skill, 800+ MCP server, 3000+ marketplace.

---

*Son güncelleme: 2026-05-15 | Birkan Otonom Pipeline*