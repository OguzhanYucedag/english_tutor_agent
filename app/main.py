# app/main.py
import ollama
from prompts import TUTOR_SYSTEM_PROMPT

MODEL_NAME = "qwen3:8b"

def run_terminal_tutor():
    print("İngilizce Öğretmeni Başlatıldı! (Çıkmak için 'q' yazın)\n" + "-" * 50)
    
    messages = [
        {"role": "system", "content": TUTOR_SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("\nSen: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "q":
            print("Görüşmek üzere!")
            break

        messages.append({"role": "user", "content": user_input})

        # RAM şişmesini önlemek için sistem mesajı + son 10 mesajı tut
        if len(messages) > 11:
            messages = [messages[0]] + messages[-10:] #(senin son 5 mesajın + öğretmenin son 5 cevabı) tutar; arada kalan çok eski mesajları listeden atar.

        print("\nÖğretmen: ", end="", flush=True)
        
        full_response = ""
        stream = ollama.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True,
            think=False,  # Sesli/anlık pratik için düşünme gecikmesini kapatır
            options={
                "num_ctx": 4096,     # 16 GB RAM için sabit bağlam sınırı
                "temperature": 0.3   # Tutarlı ve öğretici yanıtlar için düşük yaratıcılık
            }
        )

        for chunk in stream:
            content = chunk["message"]["content"]
            print(content, end="", flush=True)
            full_response += content

        print()
        messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    run_terminal_tutor()