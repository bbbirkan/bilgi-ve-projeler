---
name: alphaevolve-patterns
description: "When the user wants to implement evolutionary algorithms, LLM-driven code optimization, or an AI Scientist. Uses Google DeepMind's AlphaEvolve methodologies."
---

# AlphaEvolve Patterns Skill

Bu skill, kod ve algoritmaları kendi kendine optimize eden otonom ajanlar inşa ederken (örneğin Trade Bot katsayı optimizasyonu, evrimsel hiper-parametre arayışları) DeepMind AlphaEvolve'un kullandığı yöntemleri uygular.

## Neler Öğrenebiliriz? (Açık Kaynak Verileri)
Google DeepMind, AlphaEvolve'un tam otonom çalışma motorunu açık kaynak yapmasa da, araştırma sürecinde kullandıkları verileri ve promtları barındıran iki GitHub deposunu herkese açık yayınlamıştır:
1. **`alphaevolve_results`**: Bulunan matematiksel çözümlerin doğrulamalarını ve çıktıklarını içerir. Otonom sistemlerin ürettiği çıktıların "nasıl test edildiğini (Evaluation function)" gösterir.
2. **`alphaevolve_repository_of_problems`**: LLM'e verilen görev tanımlarını, problemleri ve otonom sistemin nasıl yönlendirildiğini (Prompt engineering) içerir.

Bu repolardan şu mantığı öğrenip kendi projelerimize uyguluyoruz:
**Mutation (Kod Üretimi)** -> **Evaluation (Test/Skorlama)** -> **Selection (En İyi Kodu Seçme ve Bir Sonraki Jenerasyona Aktarma)**.

## Göreviniz
Bir projede "AlphaEvolve tarzı" otonom bir evrimsel algoritma (örneğin trade botları için kendi stratejisini geliştiren kod) yazmanız istendiğinde:
1. `00 Github PROJELERI/alphaevolve_repository_of_problems` klasöründeki prompt ve notebookları inceleyin. LLM'i "bir önceki kodu al ve bunu daha iyi yapacak mutasyonlar ekle" şeklinde nasıl programladıklarına bakın.
2. Sabit, tek seferlik bir kod yazmak yerine; sistemi kendi kendini test eden, başarılı kodları (fitness function) hafızada tutan sürekli bir döngü (loop) olarak inşa edin.
3. Çıktıların istikrarlı olması için mutlaka AlphaEvolve'daki gibi katı bir `Evaluation` (Değerlendirme) test modülü tasarlayın.
