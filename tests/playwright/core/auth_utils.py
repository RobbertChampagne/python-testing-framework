import os
import logging
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, expect
from .browser_utils import select_browser

def ensure_auth_state(playwright: Playwright, browser_name: str, headless: bool, url: str, username: str, password: str, state_path: str) -> BrowserContext:
    """
    Ensure the authentication state is valid. If not, re-login and save the state.

    Args:
        playwright (Playwright): The Playwright instance.
        browser_name (str): The name of the browser to launch (chromium, firefox, webkit).
        headless (bool): Whether to launch the browser in headless mode.
        url (str): The URL to navigate to.
        username (str): The username for login.
        password (str): The password for login.
        state_path (str): The path to the state.json file.

    Returns:
        BrowserContext: The browser context with the valid authentication state.
    """
    # Create a headless browser for the authentication check
    headless_browser = select_browser(playwright, browser_name, True)
    
    # To override the browser selection from the pytest.ini file and launch a specific browser, 
    # use the following code:
    # browser = p.chromium.launch(headless=True)
        
    try:
        # Use the saved state.json for the browser context
        context = headless_browser.new_context(storage_state=state_path)
        page = context.new_page()
        page.goto(url)
        # Perform a simple check to ensure the state is valid
        expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
        page.close()  # Close the initial page after the check
        context.close()  # Close the headless context
        headless_browser.close()  # Close the headless browser
        # Create a new context for the actual test
        browser = select_browser(playwright, browser_name, headless)
        return browser.new_context(storage_state=state_path)  # Return the context immediately if the state is valid
           
    except Exception as e:
        logging.warning(f"State is invalid or expired: {e}. Recreating state.json.")
        # If an exception occurs, delete the state.json file and perform login steps
        if os.path.exists(state_path):
            os.remove(state_path)
            
        browser = select_browser(playwright, browser_name, headless)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.locator("[data-test=\"username\"]").fill(username)
        page.locator("[data-test=\"password\"]").fill(password)
        page.locator("[data-test=\"login-button\"]").click()

        # Save the logged-in state to state.json
        context.storage_state(path=state_path)
        page.close()  # Close the initial page after the check
    
    return context