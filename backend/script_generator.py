import google.generativeai as genai
import json

# Configure Gemini API
genai.configure(api_key="")

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

def generate_script():
    try:
        with open("news_articles.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        articles = data.get("articles", [])

        if not articles:
            return "No articles available to generate script."

        summaries = "\n\n".join(
            [f"Headline: {a['headline']}\nSummary: {a['summary']}" for a in articles]
        )

        prompt = (
            "You're a scriptwriter for a news channel. Based on the following latest news summaries, "
            "generate a 1-2 minute engaging and informative video script in English:\n\n"
            f"{summaries}\n\n"
            "The script should have a brief intro and use natural spoken English style."
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating script: {str(e)}"
