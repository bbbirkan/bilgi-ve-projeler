# security-guidance (Güvenlik Uzmanı)

**Ne işe yarar:**
Yazılımı canlı ortama (production) almadan önce tüm kod tabanını derinlemesine analiz eden, olası güvenlik açıklarını tespit edip raporlayan bir "Güvenlik Uzmanı" yeteneğidir.

**Nasıl çalışır:**
Projenizdeki dosyaları güvenlik best-practice'leri, bilinen zafiyetler, sızıntılar ve zayıf noktalar açısından tarar. Tek bir dosya yerine bütünsel bir kontrol gerçekleştirerek hiçbir güvenlik zafiyetinin gözden kaçmamasını hedefler.

**Ne zaman kullanılır:**
- Projeyi deploy (yayın) etmeden önceki son güvenlik taraması ve denetiminde
- Şifreleme, yetkilendirme, veri tabanı sorguları (SQL injection vb.) gibi hassas bileşenleri incelerken
- Mevcut kod tabanının güvenlik denetimini (audit) yapmak istendiğinde

**Kurulum ve kullanım:**
Bu yetenek resmi bir Anthropic eklentisidir:
`https://claude.com/plugins/security-guidance`

**Limitler / dikkat edilecekler:**
- Kod tabanının büyüklüğüne bağlı olarak, tüm dosyaların analiz edilmesi işlemi oldukça uzun sürebilir ve context limitlerini zorlayabilir.
- İleri seviye sızma testlerinin (pentest) yerini tamamen tutmaz; mantıksal zafiyetleri gözden kaçırma ihtimali olabilir.
