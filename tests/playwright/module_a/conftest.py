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
from ..core.browser_utils import select_browser

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
def page_context(pytestconfig):
    # Log the start of the session
    logger.info("Starting session")
    
    # Get options from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    device = pytestconfig.getoption("--device")
    
    # Use the last specified browser so that command line options take precedence over pytest.ini
    browser_name = browser_name[-1]
    
    logger.info(f"Browser specified: {browser_name}")
    logger.info(f"Headless mode: {headless}")
    logger.info(f"Device specified: {device}")
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name == "firefox":
            logger.info("Firefox does not support mobile emulation. Switching to Chromium.")
            browser_name = "chromium"
            browser = p.chromium.launch(headless=headless)
        else:
            # Select and launch the specified browser
            browser = select_browser(p, browser_name, headless)
        
        # To override the browser selection from the pytest.ini file and launch a specific browser, 
        # use the following code:
        # browser = p.chromium.launch(headless=False)
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name in ["chromium", "webkit"]:
            device_config = p.devices[device]
            context = browser.new_context(**device_config)
        else:
            # Create a new browser context (similar to a new incognito window)
            context = browser.new_context()
        
        logger.info(f"Launching {browser_name} browser")
        
        # Start tracing to capture screenshots, snapshots, and sources
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # Create a new page (tab) in the browser context
        page = context.new_page()
        
        # Navigate to the specified URL
        page.goto(url)
        
        # Yield the page and context to the test function
        yield page, context
        
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()
        
# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Playwright Module A Tests"
    