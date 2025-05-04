document.addEventListener('DOMContentLoaded', function () {
    // News data
    const newsData = {
        "last_updated": "2025-05-03T17:57:38",
        "source": "https://www.dawn.com/latest-news",
        "articles": [
            {
                "id": 1,
                "headline": "Roses of Humanity offers a hauntingly heartfelt tribute to 15,000 children killed in Gaza genocide",
                "url": "https://images.dawn.com/news/1193586/roses-of-humanity-offers-a-hauntingly-heartfelt-tribute-to-15000-children-killed-in-gaza-genocide",
                "summary": "A unique and heartfelt exhibition, titled Roses of Humanity, allows visitors in Lahore to stroll through a rose garden made of hand-stitched roses paying homage to 15,000 children killed during the genocide in Gaza."
            },
            {
                "id": 2,
                "headline": "National Women's T20 cricket tournament to start on May 7 in Karachi",
                "url": "https://www.dawn.com/news/1908187/national-womens-t20-cricket-tournament-to-start-on-may-7-in-karachi",
                "summary": "A total of five teams will vie for the title of the National Women's T20 Tournament 2025 beginning on May 7 at two venues in Karachi."
            },
            {
                "id": 3,
                "headline": "PML-N Senator Sajid Mir passes away at 86 after heart attack",
                "url": "https://www.dawn.com/news/1908184/pml-n-senator-sajid-mir-passes-away-at-86-after-heart-attack",
                "summary": "Notable religious and political leader Senator Professor Sajid Mir passed away at the age of 86 on Saturday after a heart attack."
            },
            {
                "id": 4,
                "headline": "Security forces kill 5 terrorists, arrest 2 in KP operations: ISPR",
                "url": "https://www.dawn.com/news/1908178/security-forces-kill-5-terrorists-arrest-2-in-kp-operations-ispr",
                "summary": "Five terrorists were killed and two were apprehended in three separate intelligence-based operations (IBOs) conducted by the security forces in Khyber Pakhtunkhwa."
            },
            {
                "id": 5,
                "headline": "Alvi to be held accountable if Bilawal's claim on canals proven: PTI MNA",
                "url": "https://www.dawn.com/news/1908170/alvi-to-be-held-accountable-if-bilawals-claim-on-canals-proven-pti-mna",
                "summary": "PTI lawmaker Ali Muhammad Khan said that the party would issue a show-cause notice to former president Arif Alvi if it was proven that he had approved controversial canals."
            }
        ]
    };

    // Display last updated time
    const updateTime = new Date(newsData.last_updated);
    const updateTimeElement = document.getElementById('update-time');
    if (updateTimeElement) {
        updateTimeElement.textContent = updateTime.toLocaleString();
    }

    // Render news articles
    const newsContainer = document.getElementById('news-container');
    if (!newsContainer) {
        console.error("news-container not found in the DOM");
        return;
    }

    newsData.articles.forEach(article => {
        const articleElement = document.createElement('div');
        articleElement.className = 'news-article';

        articleElement.innerHTML = `
            <div class="article-header">
                <h3><a href="${article.url}" target="_blank">${article.headline}</a></h3>
                <p class="article-source">Source: <a href="${newsData.source}" target="_blank">Dawn News</a></p>
            </div>
            <div class="article-content" style="display: none;">
                <p class="article-summary">${article.summary}</p>
            </div>
        `;

        newsContainer.appendChild(articleElement);
    });

    // Toggle article content on click
    const articleHeaders = document.querySelectorAll('.article-header');
    articleHeaders.forEach(header => {
        header.addEventListener('click', function () {
            const content = this.nextElementSibling;
            if (content) {
                content.style.display = content.style.display === 'none' ? 'block' : 'none';
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // AI-generated script section (disabled/commented)
    /*
    fetch("/latest-news-script", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.script) {
            const scriptSection = document.createElement("div");
            scriptSection.className = "generated-script";
            scriptSection.innerHTML = `
                <h2>🎤 Anchor Script</h2>
                <p>${data.script.replace(/\n/g, "<br>")}</p>
            `;
            document.querySelector('.headlines-section').appendChild(scriptSection);
        } else {
            console.warn("Script generation failed:", data);
        }
    })
    .catch(err => console.error("Error fetching script:", err));
    */
});
