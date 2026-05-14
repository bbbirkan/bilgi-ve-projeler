# PLFM_RADAR

**Ne işe yarar:**
AERIS-10, açık kaynaklı, düşük maliyetli 10.5 GHz PLFM faz dizilimli bir radar sistemidir. Drone geliştiricileri, araştırmacılar ve ileri düzey SDR meraklıları için radar teknolojisini (hüzme yönlendirme, darbe sıkıştırma, Doppler vb.) deneyimleme imkanı sunar.

**Nasıl çalışır:**
Sistem; güç yönetimi, frekans sentezleyici, ana kart, DAC, mikserler ve ADAR1000 faz kaydırıcıları gibi donanım bileşenlerinden oluşur. Sinyaller DAC ile üretilir, anten dizilimleriyle (3km veya 20km menzil için yama/dalga kılavuzu antenler) yönlendirilir ve FPGA üzerinde Doppler, MTI, CFAR gibi algoritmalarla işlenip STM32 mikrokontrolcü ve Python GUI aracılığıyla yönetilir.

**Ne zaman kullanılır:**
- Drone takip ve algılama sistemleri geliştirmek gerektiğinde
- Faz dizilimli radar (phased array) konseptlerini ve hüzme yönlendirmeyi test etmek için
- Doppler ve darbe sıkıştırma (pulse compression) sinyal işleme araştırmalarında
- Üniversite araştırma projeleri veya donanım prototipleme süreçlerinde

**Kurulum ve kullanım:**
```bash
git clone https://github.com/NawfalMotii79/PLFM_RADAR
cd PLFM_RADAR
# GUI veya araçlar için Python ortamını kurun:
pip install .
```

**Limitler / dikkat edilecekler:**
- İleri düzey donanım bilgisi gerektirir (PCB üretimi, FPGA ve STM32 programlama).
- Çift versiyon (AERIS-10N/AERIS-10E) donanım maliyeti ve üretim zorluğu açısından farklılık gösterir.
- Mikrodalga frekanslarında (10.5 GHz) çalışıldığı için lehimleme, montaj hatalarına ve PCB empedans uyumuna karşı oldukça hassastır.
- Sistem karmaşık bir güç sırası (power-up/down sequencing) ve termal yönetim gerektirir (özel soğutma fanları vb.).
