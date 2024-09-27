# pip install firecrawl-py
from firecrawl.firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-63a773d85a934306a0cdd82c584a51e2")

# Crawl a website:
crawl_result = app.crawl_url(
    'mendable.ai', {
    'crawlerOptions': {
        'excludes': ['blog/*'],
    }
    },
    2,
    )
print(crawl_result)
