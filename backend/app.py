from flask import Flask, jsonify, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os
import google.generativeai as genai
import json
from script_generator import generate_script


app = Flask(__name__)
def scheduled_script_generation():
    print("Generating script at", datetime.datetime.now())
    script = generate_script()
    with open("static/generated_script.txt", "w", encoding="utf-8") as f:
        f.write(script)
    print("Script saved.")

# Schedule the job
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_script_generation, trigger="interval", minutes=60)  # every hour
scheduler.start()

# Gemini config
genai.configure(api_key="AIzaSyBTxaEzGGLVrskzx7UK374NgV4BXn-4nqs")
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/latest-news-script", methods=["POST"])
def latest_news_script():
    try:
        # Load news from JSON file
        with open("news_articles.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        articles = data.get("articles", [])
        if not articles:
            return jsonify({"error": "No articles found"}), 400

        # Build a prompt for Gemini
        summaries = "\n\n".join(
            [f"Headline: {a['headline']}\nSummary: {a['summary']}" for a in articles]
        )

        prompt = (
            "You're a scriptwriter for a news channel. Based on the following latest news summaries, "
            "generate a 1-2 minute engaging and informative video script in English:\n\n"
            f"{summaries}\n\n"
            "The script should have a brief intro and use natural spoken English style."
        )

        # Generate response from Gemini
        response = model.generate_content(prompt)
        return jsonify({"script": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
