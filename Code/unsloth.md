# unsloth

**Kaynak**: https://github.com/unslothai/unsloth  
**Site**: https://unsloth.ai  
**Yazar**: Daniel Han + Michael Han (Unsloth AI)  
**Lisans**: Apache 2.0 (core) + AGPL-3.0 (Studio UI)  
**Yerel**: `/Users/birkan/Desktop/Work /00 Bilgi - Projeler/Code/unsloth/`

---

## Ne İşe Yarar?

Unsloth Studio, herhangi bir açık kaynak AI modelini **kendi bilgisayarında** çalıştırmana ve fine-tune etmene yarayan bir web arayüzü.

- **%100 offline** — Mac, Windows, Linux
- **2× daha hızlı** eğitim (özel Triton kernel'lar)
- **%70 daha az VRAM** tüketimi
- **Kod bilmeden** fine-tune

```bash
# Kur
curl -fsSL https://unsloth.ai/install.sh | sh

# Başlat
unsloth studio -p 8888
# → Tarayıcıda http://localhost:8888
```

---

## Neden Bu Kadar Hızlı?

Unsloth, PyTorch'un standart backward pass'ini tamamen yeniden yazdı. Özel **Triton kernel'ları** ile:

| Yöntem | VRAM | Hız |
|--------|------|-----|
| Standart PyTorch LoRA | 24GB | 1× |
| Unsloth LoRA | ~7GB | 2× |
| Unsloth QLoRA | ~5GB | 1.8× |
| Unsloth RL | ~5GB (-%80) | — |
| Unsloth MoE | %35 daha az | 12× |

---

## Desteklenen Modeller (500+)

| Kategori | Modeller |
|----------|----------|
| Text | Gemma 4, Qwen3, Qwen3.5, Llama 4, DeepSeek-V3/R1, Mistral, Phi-4, gpt-oss |
| Vision | Vision-language modeller |
| Audio | Ses modeller |
| Embedding | Embedding modeller |

**Mac'te çalışanlar**: MLX + GGUF inference, training da destekleniyor.

---

## Fine-Tuning Yöntemleri

### 1. QLoRA (Başlangıç için önerilir)
- Base modeli 4-bit quantize eder → en az VRAM
- LoRA adaptörü 16-bit eğitilir
- ~5-8GB VRAM yeterli

### 2. LoRA
- Base model 16-bit yüklü kalır
- Daha yüksek kalite, daha fazla VRAM

### 3. Full Fine-Tuning (FFT)
- Tüm model ağırlıkları eğitilir
- Maksimum kalite, maksimum kaynak

---

## Kritik LoRA Hiperparametreleri

```python
# Temel LoRA ayarları
lora_config = {
    "r": 16,                    # LoRA rank — 8,16,32,64,128. Daha yüksek = daha fazla parametre
    "lora_alpha": 32,           # Genellikle r×2. Güç çarpanı
    "lora_dropout": 0,          # Varsayılan 0. 0.05-0.1 overfitting'i azaltır
    "target_modules": [         # Hangi katmanlar eğitilecek
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj"
    ],
}

# Eğitim parametreleri
training_config = {
    "learning_rate": 2e-4,      # Başlangıç noktası. Küçük veri = daha düşük
    "num_train_epochs": 3,      # 1-3 arası. Daha fazla = overfitting riski
    "per_device_train_batch_size": 2,
    "gradient_accumulation_steps": 8,  # Efektif batch = 2×8 = 16
    "warmup_steps": 0.05,       # Toplam adımların %5'i
    "weight_decay": 0.01,
    "lr_scheduler_type": "cosine",
    "optimizer": "adamw_8bit",  # VRAM tasarrufu
    "seed": 3407,
}
```

**Kayıp (loss) hedefi**: 0.5–1.0 arası. 1.5+ ise az veri. 0.1 altı overfitting.

---

## Dataset Formatları

### Sohbet (Chat) Formatı
```json
{
  "conversations": [
    {"role": "user", "content": "Soru nedir?"},
    {"role": "assistant", "content": "Cevap budur."}
  ]
}
```

### Talimat (Instruction) Formatı
```json
{
  "instruction": "Şunu yap:",
  "input": "Bu veriye göre",
  "output": "Bu sonucu ver"
}
```

### Unsloth Studio — Otomatik Dataset
- PDF, CSV, JSON, DOCX yükle
- "Data Recipes" ile graf-node iş akışı
- Otomatik soru-cevap çifti üretir

---

## Adım Adım Fine-Tune (Studio)

```
1. unsloth studio -p 8888
2. Model seç → Qwen3-8B / Gemma-4-4B / Llama-3.2-3B
3. Dataset tab → HuggingFace dataset ID veya dosya yükle
4. Parameters → r=16, alpha=32, lr=2e-4, epochs=3
5. Training → Başlat, loss grafiğini izle
6. Export → GGUF (Ollama için) veya safetensors
```

---

## Export ve Deploy

```bash
# Unsloth → GGUF (Ollama'ya yükle)
# Studio'dan export et → model.gguf

# Ollama ile çalıştır
ollama create benim-modelim -f Modelfile
ollama run benim-modelim

# vLLM ile serve et
vllm serve ./fine-tuned-model --tensor-parallel-size 1
```

---

## Donanım Gereksinimleri

| Kullanım | Minimum |
|----------|---------|
| Chat + Data Recipes | CPU (GPU yok) |
| QLoRA 7B model | NVIDIA RTX 3060 (8GB) |
| LoRA 13B model | NVIDIA RTX 3090 (24GB) |
| Mac training | Apple Silicon M1+ (MLX) |
| AMD | Chat ✓, Training yakında |

---

## Benim İçin Ne Kullanımı Var?

| Proje | Kullanım |
|-------|---------|
| Trade Bot | Finans terminolojisi + coin analizi için özel model |
| Hermes | Türkçe optimizasyonlu base model |
| Covenant Fuel | Yakıt/lojistik domain knowledge injection |
| Genel | Kendi datasetime göre küçük ama keskin model |

---

## Kaynaklar

- [Unsloth Studio Docs](https://unsloth.ai/docs/new/studio)
- [LoRA Hyperparameters Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide)
- [Gemma 4 Fine-tuning](https://unsloth.ai/docs/models/gemma-4/train)
- [Qwen3 Fine-tuning](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune)
- [Llama 3 + Ollama Tutorial](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/tutorial-how-to-finetune-llama-3-and-use-in-ollama)
- [DataCamp Unsloth Guide](https://www.datacamp.com/tutorial/unsloth-studio-fine-tuning-llms-guide)
