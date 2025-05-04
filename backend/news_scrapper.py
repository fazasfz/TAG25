# web scraper file, scrapes dawn news website and parses data and stores in json file
# Web scraper using BeautifulSoup/Newspaper3k
import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import schedule

def scrape_articles():
    print("🔁 Scraping started...")
    base_url = "https://www.dawn.com"
    news_url = base_url + "/latest-news"

    response = requests.get(news_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article', limit=5)
    parsed_articles = []

    for i, article in enumerate(articles, start=1):
        try:
            headline_tag = article.find('h2')
            link_tag = article.find('a')

            if headline_tag and link_tag:
                headline = headline_tag.get_text(strip=True)
                link = link_tag['href']
                if not link.startswith("http"):
                    link = base_url + link

                article_page = requests.get(link)
                article_soup = BeautifulSoup(article_page.content, 'html.parser')
                paragraphs = article_soup.find_all('p')
                summary = " ".join([p.get_text(strip=True) for p in paragraphs[:5]])

                parsed_articles.append({
                    "id": i,
                    "headline": headline,
                    "url": link,
                    "summary": summary
                })

        except Exception as e:
            print(f"❌ Failed to process an article: {e}")

    data_to_save = {
        "last_updated": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "source": news_url,
        "articles": parsed_articles
    }

    with open("news_articles.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)

    print(f"✅ Updated 'news_articles.json' with {len(parsed_articles)} articles at {data_to_save['last_updated']}")

# ⏱ Hourly schedule (change to minutes while testing)
schedule.every(1).hours.do(scrape_articles)

# 🟢 Run once immediately
scrape_articles()
while True:
    schedule.run_pending()
    time.sleep(60)