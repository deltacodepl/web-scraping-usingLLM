from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='fc-63a773d85a934306a0cdd82c584a51e2')

class ExtractSchema(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

data = app.scrape_url('https://www.tapflo.com.pl/elektryczne-pompy-membranowe', {
    'formats': ['extract'],
    'extract': {
        'schema': ExtractSchema.model_json_schema(),
    }
})
print(data["extract"])
