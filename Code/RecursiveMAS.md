# RecursiveMAS (Recursive Multi-Agent Systems)

**Ne işe yarar:**
Çoklu ajan sistemlerinde (Multi-Agent Systems) ajanların birbirleriyle metin (text) yerine doğrudan **latent-space (gizli alan)** üzerinden haberleşmesini sağlayan devrimsel bir framework'tür. Bu yöntemle hızı **2.4 kat** artırırken, token maliyetini **%75** oranında azaltır ve doğruluğu ortalama **%8.3** yükseltir.

**Nasıl çalışır:**
Geleneksel sistemlerdeki her adımda gerçekleşen "decode (text) -> encode" döngüsünü ortadan kaldırır. `RecursiveLink` adı verilen hafif bir modül sayesinde ajanlar, düşüncelerini metne dökmeden doğrudan vektörel (latent) olarak birbirlerine aktarır. Sistem, tüm ajanları tek bir "recursive loop" içinde birleştirir ve sadece en son aşamada metin çıktısı üretir.

**Ne zaman kullanılır:**
- **Karmaşık Akıl Yürütme:** Matematik, kodlama veya mantık sorularında yüksek doğruluk gerektiğinde.
- **Maliyet Optimizasyonu:** Çok sayıda ajan çalıştırırken token harcamasını ciddi oranda düşürmek istendiğinde.
- **Hız (Latency) Kritik Projeler:** Ajanlar arası iletişimin yavaşlığını gidermek için.
- **Hibrit Modeller:** Farklı model ailelerini (örn. GPT + Claude + Llama) tek bir verimli döngüde birleştirmek için.

**Kurulum ve kullanım:**
1.  **Klasöre Girin:** `cd RecursiveMAS`
2.  **Kurulum:** `pip install -e .` (Bağımlılıklar: Python 3.9+, PyTorch, Transformers)
3.  **Çalıştırma:** 
    - `python main.py` (Örnek modelleri ve iş birliği stillerini denemek için)
    - Desteklenen stiller: `Sequential`, `Mixture`, `Deliberation`, `Distillation`.

**Limitler / dikkat edilecekler:**
- **Model Erişimi:** Kapalı kaynak API'larda latent-space erişimi sınırlı olabileceğinden, genellikle yerel (local) veya açık kaynaklı modellerde (HuggingFace) tam performans gösterir.
- **Eğitim:** En iyi sonuç için "inner-outer loop" öğrenme algoritmasıyla ajanların birlikte optimize edilmesi gerekebilir.
