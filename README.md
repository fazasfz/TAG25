# 📰 VOXBYTE — AI-Powered News Anchor App - Presented at TAG25

VOXBYTE is a cutting-edge AI-driven news broadcasting web application that delivers real-time news through an AI anchor. It combines web scraping, script generation using the Gemini API, and text-to-speech to automate the entire news pipeline — from data to delivery.

---

## 🔥 Features

- 🧠 Generates news anchor scripts using Gemini API (LLM by Google)  
- 🌐 Automatically scrapes and processes latest news headlines  
- 🎤 Converts scripts to realistic AI voice using TTS  
- 🕒 Backend automation using APScheduler for hourly script updates  
- 🎥 Embedded AI-generated anchor videos  
- ⚡ Modern, responsive frontend with animated Spline integration  

---

## 🧩 Tech Stack

- Python, Flask  
- Gemini API (Google Generative AI)  
- APScheduler (for backend automation)  
- HTML, CSS, JavaScript (Vanilla)  
- Text-to-Speech (via Person C’s module)  
- Spline 3D Animation  

---
📁 Project Structure
├── backend/
│   ├── app.py                    # Flask backend with script automation
│   ├── script_generator.py       # Script generation logic using Gemini
│   ├── news_articles.json        # Scraped news data
│
├── static/
│   ├── styles.css
│   ├── video/
│       └── anchor.mp4            # AI anchor video
│   └── generated_script.txt      # Latest script saved here
│
├── templates/
│   └── index.html                # Main frontend page

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/voxbyte.git
cd voxbyte
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Add your Gemini API Key
In app.py:
```bash
genai.configure(api_key="YOUR_API_KEY")
```
### 4. Run the app
```bash
python app.py
```
Open your browser at: http://localhost:5000
---
👥 Team Roles
👤 Nabira Salman — Web scraping, TTS automation, video generation

👤 Syeda Fatima Zahra (You) — Backend API integration, Gemini scripting, Flask server setup

👤 Amna Maryam Fatima — TTS module & frontend animation

🏆 Achievements
🏅 2nd Place (Runner-Up) at [TAG25 Nust]
Built in under 48 hours and delivered a fully functional AI news broadcasting solution.
