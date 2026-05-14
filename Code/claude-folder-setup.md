# claude-folder-setup (Claude İleri Seviye Klasör Yapılandırması)

**Ne işe yarar:**
Claude Code'u sıradan bir kod asistanı olmaktan çıkarıp; içerisinde farklı uzmanlık alanlarına sahip ajanların, özel kısayol komutlarının ve güvenlik/kalite denetimlerinin (hooks) bulunduğu "tam donanımlı bir sanal geliştirici ekibine" dönüştüren ileri seviye (advanced) bir konfigürasyon mimarisidir.

**Nasıl çalışır:**
Projenin ana dizininde `.claude/` isimli gizli bir klasör oluşturulur ve Claude'un yetenekleri spesifik alt klasörlere bölünerek modüler hale getirilir:
- **`agents/`:** Farklı görevler için özel ajanlar tanımlar (örn. `code-reviewer.md` ajanı sadece güvenlik açıklarını arar ve `sonnet` modelini kullanır).
- **`commands/`:** Sık yapılan işlemleri otomatize eden özel slash (`/fix-issue 42`) komutları yaratır.
- **`hooks/`:** Claude herhangi bir terminal komutu çalıştırmadan önce (PreToolUse) veya dosyayı düzenledikten sonra (PostToolUse) araya giren kontrol betikleridir. (Örn. Commit öncesi zorunlu test/lint çalıştıran bash scripti).
- **`rules/`:** Sadece belirli dosya türleri veya dizinler (örn. `app/**/*.tsx`) düzenlenirken aktif olan bağlama duyarlı (context-aware) kurallardır.
- **`skills/`:** "Frontend tasarımı yap" gibi belirli durumlarda devreye giren özel talimat setleridir.
- **`settings.json`:** Claude'un terminalde hangi komutları çalıştırabileceğini (allow) ve hangilerini kesinlikle çalıştıramayacağını (deny) belirleyen güvenlik ve yetki merkezidir.
- **`CLAUDE.md`:** Tüm oturumlarda yüklenen, projenin genel hatlarını (stack, conventions) anlatan "ana beyin" dosyasıdır.

**Ne zaman kullanılır:**
- Claude Code ile yönetilen büyük, karmaşık veya kurumsal seviyedeki yazılım projelerinde
- Kod yazım standartlarını, güvenlik denetimlerini ve test süreçlerini yapay zekaya "tavsiye" olarak değil, "zorunlu (bloklayıcı) kurallar" olarak dayatmak gerektiğinde
- Aynı komut dizilerini (issue bul -> kodu incele -> fix yaz -> test et -> commit at) sürekli baştan promptlamak yerine, `/fix-issue` gibi tek bir komuta indirgemek için

**Kurulum ve kullanım:**
Tek seferlik hızlı kurulum için projenizin ana dizininde şu komutları çalıştırarak iskeleti oluşturabilirsiniz:
```bash
mkdir -p .claude/{agents,commands,hooks,rules,skills/frontend-design}
touch .claude/agents/{code-reviewer,debugger,test-writer,refactorer,doc-writer,security-auditor}.md
touch .claude/commands/{fix-issue,deploy,pr-review}.md
touch .claude/hooks/{pre-commit,lint-on-save}.sh
touch .claude/rules/{frontend,database,api}.md
touch .claude/skills/frontend-design/SKILL.md
touch .claude/settings.json CLAUDE.md

# Hook scriptlerinin çalışabilmesi için yetki verin
chmod +x .claude/hooks/*.sh
```
Ardından bu dosyaların içini paylaşılan örneklerdeki gibi kendi proje ihtiyaçlarınıza (kullanacağınız framework, kurallar vs.) göre doldurmanız gerekir.

**Limitler / dikkat edilecekler:**
- Bu yapılandırma oldukça güçlüdür; ancak `settings.json` içerisindeki `permissions` (izin) ayarları çok kısıtlayıcı yapılırsa Claude'un iş yapmasını (örneğin terminalde dosya aramasını) engelleyebilir.
- `hooks` klasöründeki scriptlerin (bash) mutlaka çalıştırılabilir (executable) izinlere (`chmod +x`) sahip olması şarttır, yoksa `exit 2` hataları vererek sistemi kilitler.
- Her projenin stack'i ve ihtiyacı farklı olduğu için, dosyalar kopyala-yapıştır yapıldıktan sonra muhakkak projeye özel (Tailwind kullanmıyorsanız o kuralın silinmesi gibi) revize edilmelidir.
