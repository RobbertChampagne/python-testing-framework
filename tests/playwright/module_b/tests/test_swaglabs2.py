# pytest tests/playwright/module_b/tests/test_swaglabs2.py
# pytest tests/playwright/module_b/tests/test_swaglabs2.py --device="iPhone 13"
# pytest tests/playwright/module_b/tests/test_swaglabs2.py --device="Galaxy S9+"
# pytest tests/playwright/module_b/tests/test_swaglabs2.py::test_example --device="Galaxy S9+"

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os
from ...core.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Module B")

def test_example3(page_context):
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page = page_context
        
        # Perform assertions on the page content
        page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()
        
    finally:
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/module_b/trace_test_example3.zip")
        
        
        