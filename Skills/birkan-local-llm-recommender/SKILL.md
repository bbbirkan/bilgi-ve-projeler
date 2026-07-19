---
name: local-llm-recommender
description: "Sistemin donanım özelliklerini (CPU, GPU, RAM, Disk) tespit ederek Ollama, LM Studio veya llama.cpp için en uygun 3 yerel LLM önerisinde bulunur."

TRIGGER bu skill'i şu durumlarda çağır:
- Kullanıcı "yerel olarak hangi modeli çalıştırabilirim?", "bilgisayarım X modelini kaldırır mı?" dediğinde.
- Ollama veya LM Studio kurulumu hakkında soru sorduğunda.
- Donanım performansına göre model tavsiyesi istediğinde.
---

# 💻 Local LLM Recommender Skill

Bu yetenek, ana makinenin işletim sistemi, CPU, GPU, VRAM ve sistem RAM'ini gerçek kabuk komutlarıyla tespit eder ve donanıma tam uyan üç açık kaynaklı LLM önerir.

## 🛠 Donanım Tespit Komutları

### macOS (Apple Silicon)
- **CPU:** `sysctl -n machdep.cpu.brand_string`
- **RAM:** `sysctl -n hw.memsize | awk '{printf "%.0f GB\n", $1/1073741824}'`
- **GPU/VRAM:** `system_profiler SPDisplaysDataType | grep -E "Chipset|Total Number of Cores|Metal"`
- **Disk:** `df -h ~ | tail -1`

### Linux (NVIDIA)
- **VRAM:** `nvidia-smi --query-gpu=name,memory.total --format=csv,noheader`
- **RAM:** `grep MemTotal /proc/meminfo | awk '{printf "%.0f GB\n", $2/1048576}'`

## 📊 Öneri Kategorileri
1. **COMFORTABLE:** Hızlı, düşük thermal stres, geniş bağlam penceresi.
2. **BALANCED:** En yüksek kalite/performans dengesi.
3. **STRETCH:** Makinenin yükleyebileceği en büyük model (RAM offload ile yavaş çalışabilir).

## 📥 Kurulum Önerileri
- **Ollama:** Genel kullanım için en kolayı.
- **llama.cpp / LM Studio:** Qwen3.6 gibi özel vision modelleri veya güç kullanıcıları için.

---
*Snapshot Date: 11-05-2026 (Artificial Analysis Intelligence Index)*
