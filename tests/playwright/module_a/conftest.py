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

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Playwright Module A")

# Load environment variables from .env file
load_dotenv()
url = os.getenv('URL_ONE', '')

@pytest.fixture(scope="session")
def jobtitle():
    return os.getenv("JOBTITLE")

@pytest.fixture(scope="function")
def page_context():
    
    logger.info("Starting session")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        # Start tracing
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page = context.new_page()
        page.goto(url)
        
        yield page, context
        
        context.close()
        browser.close()
        
# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Playwright Module A Tests"
    