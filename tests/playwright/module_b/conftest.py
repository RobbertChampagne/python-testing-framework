import html
import pytest
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
import os
import logging
import sys
from pytest_html import extras
from ..core.html_summary import pytest_html_results_summary
from ..core.loggingSetup import setup_logging
from ..core.auth_utils import ensure_auth_state

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Playwright Module B")

# Load environment variables from .env file
load_dotenv()
user = os.getenv('SWAGLABS_USER_ONE')
password = os.getenv('SWAGLABS_PASSWORD')
url = os.getenv('SWAGLABS_URL')

# Define the path for state.json file
state_path = os.path.join(os.path.dirname(__file__), 'setup', 'state.json')

@pytest.fixture(scope="function")
def page_context(pytestconfig):
    # Log the start of the session
    logger.info("Starting session")
    
    # Get browser name and headless option from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Ensure the authentication state is valid
        context = ensure_auth_state(p, browser_name, headless, url, user, password, state_path)
        page = context.new_page()
        
        # Start tracing to capture screenshots, snapshots, and sources
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page.goto(url)
        
        # Yield the page and context to the test function
        yield page, context
        
        # Close the browser context and browser after the test is done
        context.close()
        context.browser.close()
        
# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Playwright Module A Tests"
    