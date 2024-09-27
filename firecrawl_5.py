from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))


# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev',
    params={
        'formats': ['markdown', 'html'],
        'actions': [
            {"type": "wait", "milliseconds": 2000},
            {"type": "click", "selector": "button[type=\"submit\"]"},
            {"type": "wait", "milliseconds": 2000},
            {"type": "write", "text": "firecrawl"},
            {"type": "wait", "milliseconds": 2000},
            {"type": "press", "key": "ENTER"},
            {"type": "wait", "milliseconds": 3000},
            {"type": "click", "selector": "h3"},
            {"type": "wait", "milliseconds": 3000},
            {"type": "screenshot"}
        ]
    }
)
print(scrape_result)
