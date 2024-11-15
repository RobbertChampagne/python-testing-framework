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
from ..core.browser_utils import select_browser
from ..core.utils import save_trace

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

@pytest.fixture(scope="session")
def browser_context(pytestconfig):
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
        
        # Select and launch the specified browser
        browser = select_browser(p, browser_name, headless)
            
        # Ensure the authentication state is valid
        context = ensure_auth_state(p, browser_name, headless, url, user, password, state_path)
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name in ["chromium", "webkit"]:
            device_config = p.devices[device]
            context = browser.new_context(**device_config, storage_state=state_path)
            
        logger.info(f"Launching {browser_name} browser")
        
        # Yield the context to the test functions
        yield context
        
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()
        
@pytest.fixture(scope="function")
def page_context(browser_context, request):
    # Create a new page in the browser context
    page = browser_context.new_page()
    
    # Start tracing to capture screenshots, snapshots, and sources
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    # Navigate to the specified URL
    page.goto(url)
    
    # Yield the page to the test function
    yield page
    
    # Stop tracing and save the trace
    test_name = request.node.name
    save_trace(browser_context, "module_b", f"trace_{test_name}.zip")
    
    # Close the page after the test function is done
    page.close()

# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Playwright Module B Tests"
    