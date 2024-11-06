import html
import pytest
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv
import os
import logging
import sys
from pytest_html import extras
from ..core.loggingSetup import setup_logging

# Load environment variables from .env file
load_dotenv()

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Module A")

@pytest.fixture(scope='session')
def get_logger():
    return logger

@pytest.fixture(scope="function")
def page_context(get_logger):
    
    url = os.getenv('URL_ONE', '')
    
    logger = get_logger
    logger.info("Starting test_example")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        
        yield page
        
        context.close()
        browser.close()
        
# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Module A Tests"
    