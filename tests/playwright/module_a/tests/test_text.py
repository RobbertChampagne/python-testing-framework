# pytest tests/playwright/module_a/tests/test_text.py
import pytest
from playwright.sync_api import Page, expect
import re
from dotenv import load_dotenv
import os
import logging

def test_example(page_context: Page, get_logger):
    logger = get_logger
    
    logger.info("Starting test")
    
    page = page_context
    expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
    expect(page.locator("#header-container")).to_contain_text("QA Engineer")
    expect(page.locator("#header-container")).to_contain_text("Ensuring Software Quality Through Automation, Communication, and Process Improvement.")
    expect(page.locator("#skills-section")).to_contain_text("Always a Student, Never a Master: Embracing Never Ending Learning.")
    expect(page.locator("#header-container").get_by_role("img", name="Profile image")).to_be_visible()