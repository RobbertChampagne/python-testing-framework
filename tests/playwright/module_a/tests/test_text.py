# pytest tests/playwright/module_a/tests/test_text.py

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os

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
        # python-testing-framework/tests/playwright/traces/module_a
        trace_path = os.path.join(os.path.dirname(__file__), '..', '..', 'traces', 'module_a', 'trace_example.zip')
        os.makedirs(os.path.dirname(trace_path), exist_ok=True)
        context.tracing.stop(path=trace_path)