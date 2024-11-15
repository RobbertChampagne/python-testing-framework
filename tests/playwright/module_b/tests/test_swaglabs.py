# pytest tests/playwright/module_b/tests/test_swaglabs.py
# pytest tests/playwright/module_b/tests/test_swaglabs.py --device="iPhone 13"
# pytest tests/playwright/module_b/tests/test_swaglabs.py --device="Galaxy S9+"
# pytest tests/playwright/module_b/tests/test_swaglabs.py::test_example --device="Galaxy S9+"

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os
from ...core.utils import save_trace
import pytest

# Setup logging configuration
logger = logging.getLogger("Module B")

def test_example(page_context):
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page = page_context
        
        # Perform assertions on the page content
        expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        
    finally:
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/module_b/trace_test_example.zip")

        
        
def test_example2(page_context, pytestconfig):
    
    device = pytestconfig.getoption("--device")
    if device == "Galaxy S9+":
        pytest.skip("Skipping test for Galaxy S9+")
       
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page = page_context
        
        # Perform assertions on the page content
        expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
        page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        
    finally:
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/module_b/trace_test_example2.zip")
     