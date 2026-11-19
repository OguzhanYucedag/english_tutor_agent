# English Tutor Agent

Terminal üzerinden çalışan, yerel LLM tabanlı İngilizce öğretmen asistanı. Türkçe konuşan A1–A2 seviyesindeki öğrenciler için pratik odaklı geri bildirim verir.

Model: **Ollama** + **qwen3:8b** (bilgisayarında çalışır, API anahtarı gerekmez).

## Ne yapar?

Öğrenci Türkçe soru sorabilir veya hatalı İngilizce cümle yazabilir. Öğretmen her turda şu yapıyı takip eder:

1. **Türkçe açıklama** — hata veya kelimeyi sade Türkçe ile açıklar  
2. **Doğru İngilizce** — doğal ve doğru cümleyi verir  
3. **Kelime notu** — 1–2 önemli kelime ve Türkçe karşılığı  
4. **Sıradaki soru** — öğrenileni pekiştiren kısa İngilizce soru  

## Gereksinimler

- Python 3.10+
- [Ollama](https://ollama.com) kurulu ve çalışıyor olmalı
- Model: `qwen3:8b`

## Kurulum

```bash
# Depoyu aç
cd english_tutor_agent
sadasdasdsdsa
# Sanal ortam
python3 -m venv venv
source venv/bin/activate

# Bağımlılık
pip install ollama
```

Ollama modelini indir:

```bash
ollama pull qwen3:8b
```

## Çalıştırma

Ollama servisinin ayakta olduğundan emin ol. macOS’ta genelde arka planda zaten çalışır. Port doluysa (`address already in use`) servis zaten açıktır; yeniden `ollama serve` çalıştırmana gerek yok.

```bash
cd english_tutor_agent
source venv/bin/activate
cd app
python main.py
```

`python` komutu sistem Python’una gidiyorsa (alias / PATH), venv Python’unu doğrudan kullan:

```bash
cd english_tutor_agent
./venv/bin/python app/main.py
```

Çıkmak için sohbette `q` yaz. `Ctrl+C` de durdurur; o durumda görünen `KeyboardInterrupt` normaldir.

## Proje yapısı

```text
english_tutor_agent/
├── app/
│   ├── main.py      # Terminal sohbet döngüsü, Ollama çağrısı
│   └── prompts.py   # Sistem prompt (öğretmen kuralları)
├── data/            # (ileride veri / notlar için)
├── venv/            # Sanal ortam
└── README.md
```

## Ayarlar (`app/main.py`)

| Ayar | Değer | Açıklama |
|------|--------|----------|
| `MODEL_NAME` | `qwen3:8b` | Kullanılan Ollama modeli |
| `num_ctx` | `4096` | Bağlam penceresi (RAM kullanımı) |
| `temperature` | `0.3` | Daha tutarlı, öğretici yanıtlar |
| `think` | `False` | Düşünme gecikmesini kapatır |
| Geçmiş | system + son 10 mesaj | RAM şişmesini önler |

Öğretmen davranışını değiştirmek için `app/prompts.py` içindeki `TUTOR_SYSTEM_PROMPT` metnini düzenle.

## Örnek kullanım

```text
Sen: Yesterday I go to okul
Öğretmen:
1. Türkçe Açıklama: ...
2. Doğru İngilizce: Yesterday I went to school.
3. Kelime Notu: ...
4. Sıradaki Soru: ...
```

