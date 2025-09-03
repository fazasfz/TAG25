# backend/generate_video.py
import requests
import base64
import time

AVATAR_ID = "amy"  # You can change this to any D-ID public avatar name.
API_TOKEN = ""

def generate_avatar_video():
    with open("final_audio.mp3", "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode("utf-8")

    url = "https://api.d-id.com/talks"
    headers = {
        "Authorization": f"Basic {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "source_url": "",
        "script": {
            "type": "audio",
            "audio": audio_b64
        },
        "driver_id": AVATAR_ID,
        "config": {
            "fluent": True,
            "pad_audio": 0.2
        }
    }

    r = requests.post(url, headers=headers, json=data)
    talk_id = r.json().get("id")

    # Poll until video is ready
    while True:
        poll = requests.get(f"https://api.d-id.com/talks/{talk_id}", headers=headers)
        status = poll.json()
        if status.get("result_url"):
            break
        time.sleep(5)

    video_url = status["result_url"]
    video_data = requests.get(video_url).content

    with open("static/video/anchor.mp4", "wb") as f:
        f.write(video_data)
        
