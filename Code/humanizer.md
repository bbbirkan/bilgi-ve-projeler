# humanizer

**Ne işe yarar:**
Claude Code ve OpenCode gibi yapay zeka kod ajanları (AI agents) için, metinlerdeki yapay zeka tarafından yazıldığına dair izleri (AI-generated signs) kaldıran ve metni daha doğal, insan elinden çıkmış gibi yeniden yazan bir yetenek (skill) eklentisidir.

**Nasıl çalışır:**
Yetenek, Wikipedia'nın "Signs of AI writing" rehberinden türetilmiş 29 farklı kuralı ve kalıbı kullanarak (örneğin aşırı em-dash kullanımı, bağlaç hataları, basmakalıp sözcükler) metni tarar ve yapay zeka klişelerinden arındırır. Ardından "bariz yapay zeka üretimi" denetimi yapar ve dilerseniz sizin daha önce verdiğiniz örnek metinleri analiz edip (voice calibration - ses tonu eşleştirme) kendi yazım ritminize ve kelime tercihlerinize göre metni son haline getirir.

**Ne zaman kullanılır:**
- AI tarafından üretilmiş makale, dökümantasyon veya e-posta metinlerini daha insansı hale getirmek istediğinizde
- Yapay zekaya bir metni sizin yazım tarzınızda ve üslubunuzda yeniden yazdırtmak için
- Sıkıcı ve jenerik "AI tonundan" kurtulmak gerektiğinde

**Kurulum ve kullanım:**
```bash
# Repo zaten bulunduğunuz dizine klonlandı. 
# Ancak Claude Code veya OpenCode ile kullanılmak üzere araçların kendi skill klasörlerine de atılabilir:
mkdir -p ~/.claude/skills
git clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer

# Kullanım örneği (Claude Code veya OpenCode içerisinde):
/humanizer [AI metninizi buraya yapıştırın]

# Kendi yazım tarzınıza uyarlamak (Voice Calibration) için kullanım:
/humanizer Here's a sample of my writing for voice matching: [kendi yazdığınız 2-3 paragraf]. Now humanize this text: [AI metni]
```

**Limitler / dikkat edilecekler:**
- Tam bir "insan" kalitesine ulaşması ve sizin tarzınızı taklit edebilmesi için sisteme sağladığınız örnek metnin belirgin ve uzun olması gerekir.
- Düzenlenen metinler her zaman insan tarafından bir son kontrolden geçmelidir, özellikle teknik terimler ve kod detaylarında anlam kaymaları oluşabilir.
- Temel olarak İngilizce kalıplar ve Wikipedia verileri üzerine oturtulduğundan, Türkçe veya diğer dillerdeki başarısı kısıtlı olabilir.
