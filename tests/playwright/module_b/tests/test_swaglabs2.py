# pytest tests/playwright/module_b/tests/test_swaglabs.py

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os
from ...core.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Module B")

def test_example(page_context):
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page, context = page_context
        
        # Perform assertions on the page content
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'trace_example2.zip'
        trace_dir_name = 'module_b'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/{trace_dir_name}/{trace_name}")
        
        
        