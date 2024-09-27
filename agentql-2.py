import agentql
from playwright.sync_api import sync_playwright

# Initialise the browser
with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
    page = agentql.wrap(browser.new_page())
    page.goto("https://www.tapflo.com.pl/elektryczne-pompy-membranowe")

    # Find "Search" button using Smart Locator
    contact_button = page.get_by_prompt("contact button")
    # Interact with the button
    contact_button.click()

    # Define a query for modal dialog's search input
    SEARCH_BOX_QUERY = """
    {
        modal {
            search_box
        }
    }
    """

    # Get the modal's search input and fill it with "Quick Start"
    response = page.query_elements(SEARCH_BOX_QUERY)
    response.modal.search_box.type("Quick Start")

    # Define a query for the search results
    SEARCH_RESULTS_QUERY = """
    {
        modal {
            search_box
            search_results {
                items[]
            }
        }
    }
    """

    # Execute the query after the results have returned then click on the first one
    response = page.query_elements(SEARCH_RESULTS_QUERY)
    response.modal.search_results.items[0].click()

    # Used only for demo purposes. It allows you to see the effect of the script.
    page.wait_for_timeout(10000)