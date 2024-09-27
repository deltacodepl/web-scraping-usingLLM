from firecrawl import FirecrawlApp
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

# Scrape a website:
scrape_status = app.scrape_url(
  'https://www.tapflo.com.pl/elektryczne-pompy-membranowe',
  params={'formats': ['markdown']}
)

if scrape_status:
  with open('eodd.html', 'w') as html_file:
    html_file.write(json.dumps(scrape_status))

# Crawl a website:
# crawl_status = app.crawl_url(
#   'https://firecrawl.dev',
#   params={
#     'limit': 100,
#     'scrapeOptions': {'formats': ['markdown', 'html']}
#   }
# )
# print(crawl_status)
