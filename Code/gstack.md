# gstack (Tüm Şirket Hiyerarşisi)

**Ne işe yarar:**
Y Combinator CEO'su Garry Tan tarafından oluşturulmuş, tek bir plugin içinde CEO, mühendislik müdürü, release manager, QA dahil 23 farklı rolü (şirket hiyerarşisi) barındıran kapsamlı bir yönetim eklentisidir.

**Nasıl çalışır:**
Claude'u tek bir yazılımcı gibi düşünmek yerine komple bir yazılım şirketi ekibi gibi konfigüre eder. İlgili rolün prompt setlerini yükleyerek süreç içinde kodun ürün yönetimi, mühendislik kararları ve kalite aşamalarından farklı "sanal çalışanların" değerlendirmesiyle geçmesini sağlar.

**Ne zaman kullanılır:**
- Start-up projelerini veya kompleks işleri uçtan uca (fikir aşamasından test aşamasına kadar) yönetirken
- Şirket içindeki farklı departmanların (ürün, yazılım, kalite güvence) geri bildirimlerini tek bir platformda simüle etmek için
- Geniş çaplı projelerin release (yayınlama) süreçlerinde farklı uzman görüşlerine ihtiyaç duyulduğunda

**Kurulum ve kullanım:**
```bash
git clone https://github.com/garrytan/gstack
```

**Limitler / dikkat edilecekler:**
- İçerisinde 23 farklı skill/rol barındırdığından, doğru zamanda doğru rolü çağırmazsanız rol karmaşasına veya hedeften sapmalara sebep olabilir.
- Çok spesifik ve basit görevler için (örneğin ufak bir bug fix) bu eklentiyi kullanmak gereksiz bir operasyonel yüke (overhead) dönüşebilir.
