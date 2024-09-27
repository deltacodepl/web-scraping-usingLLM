# pip install firecrawl-py
from firecrawl.firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-63a773d85a934306a0cdd82c584a51e2")

# Scrape a website:
# scrape_result = app.scrape_url('https://tapflo.com.pl',
#                                params={
#                                    'limit': 100,
#                                    'scrapeOptions': {'formats': ['markdown', 'html']}
#                                    })
# print(scrape_result['markdown'])
crawl_status = app.crawl_url(
  'https://firecrawl.dev',
  params={
    'limit': 100,
    'scrapeOptions': {'formats': ['markdown', 'html']}
  },
  poll_interval=30)
print(crawl_status)