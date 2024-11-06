import asyncio
import pytest
import os
from dotenv import load_dotenv
from .setup.cognito_token import unlink_cognito_token, write_cognito_token
from ..core.html_summary import pytest_html_results_summary
from ..core.loggingSetup import setup_logging 

# Load environment variables from .env file
load_dotenv()

# Setup logging configuration
setup_logging()

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="session")
def env():
    return os.getenv("ENVIRONMENT")

@pytest.fixture(scope="session")
def base_url(env):
    return f"https://{env}.website123.be"

# Hook to add a title to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Module A Tests"

@pytest.fixture(scope="session", autouse=True)
async def setup_temp_token():
    # Setup code: runs before any tests
    print("Session started")
    await write_cognito_token()
    
    yield  # This is where the test code runs
    
    # Teardown code: runs after all tests
    print("Session finished")
    await unlink_cognito_token()

'''
# Pytest hooks like pytest_sessionstart and pytest_sessionfinish do not support asynchronous functions directly.
# You need to run the coroutine in the event loop manually.
def run_async(async_func):
    # Run the asynchronous function in the event loop
    asyncio.get_event_loop().run_until_complete(async_func)
    
def pytest_sessionstart(session):
    # Hook that runs at the start of the test session
    print("Session started")
    # Run the asynchronous function to write the Cognito token
    run_async(write_cognito_token())

def pytest_sessionfinish(session, exitstatus):
    # Hook that runs at the end of the test session
    print("Session finished")
    # Run the asynchronous function to unlink the Cognito token
    run_async(unlink_cognito_token())
'''