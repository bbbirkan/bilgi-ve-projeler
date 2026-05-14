# code-review (5 Kişilik Kalite Kontrol)

**Ne işe yarar:**
5 farklı ajanın aynı anda paralel olarak çalışıp kodunuzu buglar, güvenlik açıkları ve proje kuralları gibi farklı açılardan detaylı incelediği "Kalite Kontrol" (QA) yeteneğidir.

**Nasıl çalışır:**
Eklenti, Claude Code içerisinde çoklu ajan (multi-agent) mimarisiyle çalışır. Yazılan veya mevcut olan kodu incelemesi için birden fazla ajanı eşzamanlı olarak devreye sokar ve her biri farklı bir perspektiften (güvenlik, standartlar, performans) değerlendirme yapar.

**Ne zaman kullanılır:**
- Kodu canlıya (production) almadan önce çok detaylı bir hata incelemesi (code review) gerektiğinde
- Tek bir yapay zeka ajanı gözünden kaçabilecek kompleks bug ve açıkları tespit etmek için
- Takım tabanlı kalite kontrol süreçlerini tek adımda simüle ederken

**Kurulum ve kullanım:**
Bu yetenek resmi bir Anthropic eklentisidir:
`https://claude.com/plugins/code-review`

**Limitler / dikkat edilecekler:**
- Paralel çalışan 5 ajan yoğun bir inceleme süreci yürüteceği için CPU kullanımı, token harcaması ve bekleme süresini katlayabilir.
- Her incelemede ajanslar arası "false-positive" (yanlış alarm) çakışmaları yaşanma ihtimaline karşı geliştiricinin son kararı vermesi önemlidir.
