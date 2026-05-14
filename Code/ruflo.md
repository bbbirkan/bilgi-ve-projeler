# Ruflo (ruvnet/ruflo)

**Ne işe yarar:**
Claude Code'u sadece bir sohbet arayüzü olmaktan çıkarıp, içerisinde 100'den fazla uzman ajanın çalıştığı devasa bir **Multi-Agent Orkestrasyon Platformu**'na dönüştürür. Karmaşık yazılım süreçlerini "Swarm" (Sürü) mantığıyla otonom olarak yönetmeyi sağlar.

**Nasıl çalışır:**
- **Swarm Koordinasyonu:** Ajanları hiyerarşik (hierarchical), ağ (mesh) veya halka (ring) yapılarında birbirine bağlar.
- **Plugin Marketplace:** Kendi eklenti sistemine sahiptir. Yeni yetenekler ve MCP araçları `/plugin` komutuyla anında eklenebilir.
- **Persistent Learning:** HNSW vektör hafızası ve **SONA (Self-learning)** motoru sayesinde yaptığı hataları hatırlar ve kendini optimize eder.
- **Multi-LLM:** Sadece Claude değil; GPT, Gemini, Cohere ve Ollama (local) modellerini aynı anda koordine edebilir.

**Ne zaman kullanılır:**
- **Devasa Kod Tabanları:** Tek bir ajanın context limitine takıldığı büyük projelerde.
- **Uzmanlık Gerektiren Görevler:** Aynı anda bir Security Auditor, bir Senior Architect ve bir QA Engineer'ın kodunuzu incelemesini istediğinizde.
- **Otonom İş Akışları:** "Hata bul, fixle, test et ve commit at" döngüsünü tamamen otomatize etmek için.

**Kurulum ve kullanım:**
1. **Hızlı Başlangıç:** `npx ruflo@latest init --wizard`
2. **Geliştirici Kurulumu:** 
   ```bash
   cd ruflo
   npm install
   ```
3. **Komutlar:**
   - `/plugin marketplace add ruvnet/ruflo` (Marketplace'e bağlanır)
   - `/coordination:spawn` (Yeni bir ajan sürüsü başlatır)

**Limitler / dikkat edilecekler:**
- **Maliyet:** Çok fazla ajan ve MCP aracı kullanımı API faturasını kabartabilir.
- **Karmaşıklık:** Swarm yapıları büyüdükçe ajanlar arası çelişkiler oluşabilir; bu noktada `RecursiveMAS` gibi latent-space optimizasyonları ile birleştirilmesi (hibrit kullanım) önerilir.
