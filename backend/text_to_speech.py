# backend/text_to_speech.py
import requests

API_KEY = "sk_5bd507055c6787ef1ab8890d8878ec6b59064b604a52b362"
VOICE_ID = "VzCzzZS0ff2iL6Izl8fR"

def generate_voiceover():
    with open("final_script.txt", "r") as f:
        text = f.read()

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open("final_audio.mp3", "wb") as f:
        f.write(response.content)