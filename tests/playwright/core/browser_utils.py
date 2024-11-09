from playwright.sync_api import Playwright

def select_browser(playwright: Playwright, browser_name: str, headless: bool):
    """
    Select and launch the specified browser.

    Args:
        playwright (Playwright): The Playwright instance.
        browser_name (str): The name of the browser to launch (chromium, firefox, webkit).
        headless (bool): Whether to launch the browser in headless mode.

    Returns:
        Browser: The launched browser instance.
    """
    if browser_name == "firefox":
        return playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        return playwright.webkit.launch(headless=headless)
    else:
        return playwright.chromium.launch(headless=headless)