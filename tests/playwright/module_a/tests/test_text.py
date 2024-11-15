# pytest tests/playwright/module_a/tests/test_text.py

from playwright.sync_api import Page, expect
from ...core.loggingSetup import setup_logging
import logging
import os
from ...core.utils import save_trace
import pytest

# Setup logging configuration
logger = logging.getLogger("Module A")

def test_example(page_context: Page, jobtitle):
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page, context = page_context
        
        # Perform assertions on the page content
        expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
        expect(page.locator("#header-container")).to_contain_text(jobtitle) # Use the jobtitle fixture
        expect(page.locator("#header-container")).to_contain_text("Ensuring Software Quality Through Automation, Communication, and Process Improvement.")
        expect(page.locator("#skills-section")).to_contain_text("Always a Student, Never a Master: Embracing Never Ending Learning.")
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'trace_example.zip'
        trace_dir_name = 'module_a'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/{trace_dir_name}/{trace_name}")
        
        
def test_example_2(page_context: Page, pytestconfig):
    
    device = pytestconfig.getoption("--device")
    if device == "Galaxy S9+":
        pytest.skip("Skipping test for Galaxy S9+")
        
    try:
        # Log the start of the test
        logger.info("Starting test")
        
        # Unpack the page and context from the fixture
        page, context = page_context
        
        # Perform assertions on the page content
        expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'example_skip.zip'
        trace_dir_name = 'module_a'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/{trace_dir_name}/{trace_name}")
        
        