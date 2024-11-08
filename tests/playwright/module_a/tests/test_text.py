# pytest tests/playwright/module_a/tests/test_text.py

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os
from ...core.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Module A")

def test_example(page_context: Page, jobtitle):
    try:
        logger.info("Starting test")
        
        page, context = page_context
        expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
        expect(page.locator("#header-container")).to_contain_text(jobtitle) # Use the jobtitle fixture
        expect(page.locator("#header-container")).to_contain_text("Ensuring Software Quality Through Automation, Communication, and Process Improvement.")
        expect(page.locator("#skills-section")).to_contain_text("Always a Student, Never a Master: Embracing Never Ending Learning.")
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'trace_example.zip'
        trace_dir_name = 'module_a'
        save_trace(context, trace_dir_name, trace_name)
        logger.info(f"Open trace: python -m playwright show-trace tests/playwright/traces/{trace_dir_name}/{trace_name}")
        
        
        