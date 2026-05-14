# claude-mem (Hafıza Uzmanı)

**Ne işe yarar:**
Claude'a kalıcı bir hafıza (memory) kazandıran, böylece her yeni oturumda (session) projenin detaylarını sıfırdan açıklama zorunluluğunu ortadan kaldıran bir eklentidir. 21K GitHub yıldızına sahiptir.

**Nasıl çalışır:**
Proje bağlamını, önceki oturumlardaki kararları, kuralları veya dosya yapılarını kalıcı bir şekilde kaydeder (örneğin `.claude_mem` gibi yerel bir hafıza dosyası kullanarak). Claude her yeni oturuma başladığında bu kalıcı hafızadan mevcut bilgileri geri yükler.

**Ne zaman kullanılır:**
- Uzun soluklu ve çok session'lı projelerde bağlam (context) ve bilgi kaybetmemek için
- Aynı projeyi her defasında Claude'a baştan tarif etmekten yorulduğunuzda
- Kullanıcıya ait spesifik çalışma tercihlerini ve yapılandırmaları sürekli hatırlaması istendiğinde

**Kurulum ve kullanım:**
```bash
git clone https://github.com/nicholasgasior/claude-mem
```

**Limitler / dikkat edilecekler:**
- Hafızaya alınan bilgi yığını büyüdükçe token bağlamını (context window) tüketebilir.
- Projede köklü değişiklikler olduğunda eski bilgilerin manuel olarak temizlenmesi veya güncellenmesi gerekebilir, aksi takdirde eski kararlara takılı kalabilir.
