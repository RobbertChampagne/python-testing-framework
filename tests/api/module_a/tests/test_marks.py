# pytest -s tests/api/module_a
# pytest tests/api/module_a/tests/test_marks.py 
# pytest -k test_get_user_parametrize tests/api/module_a/tests/test_marks.py 

import httpx
import pytest
import logging
from ...core.apis_info import ApiAbbreviation, apiUrls

# Configure the logger
logger = logging.getLogger(__name__) # __name__ is set to the module's name when it is executed

userIds = [1, 2]

@pytest.mark.asyncio
@pytest.mark.parametrize('userId', userIds)
async def test_get_user_parametrize(userId, statusCode, caplog):
    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        # Construct the URL for the API endpoint
        url = apiUrls[ApiAbbreviation.Reqres] + f"/users/{userId}"
        
        # Make an asynchronous GET request to the API
        response = await client.get(url)
        
        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200

        # Extract the user data from the JSON response
        user = response.json()["data"]
        
        # Log the user data (for capturing in the HTML report)
        logger.info(f"User data: {user}")
        
@pytest.mark.asyncio
@pytest.mark.parametrize("userId, statusCode", [
    (1, 200),
    (2, 200),
    ('x', 400)
])
async def test_get_user_parametrize_two(userId, statusCode, caplog):
    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        # Construct the URL for the API endpoint
        url = apiUrls[ApiAbbreviation.Reqres] + f"/users/{userId}"
        
        # Make an asynchronous GET request to the API
        response = await client.get(url)
        
        # Assert that the response status code is 200 (OK)
        assert response.status_code == statusCode

        # Extract the user data from the JSON response
        user = response.json()["data"]
        
        # Log the user data (for capturing in the HTML report)
        logger.info(f"User data: {user}")

@pytest.mark.asyncio
@pytest.mark.xfail(reason="This test is expected to fail due to bug #123")
async def test_get_user_fail():
    async with httpx.AsyncClient() as client:
        # This test is expected to fail
        assert 0
        
@pytest.mark.asyncio
@pytest.mark.skip(reason="This test is skipped because feature #456 is not yet implemented")
async def test_get_user_skip():
    async with httpx.AsyncClient() as client:
        # This test is skipped
        pass

# pytest tests/api/module_a/tests/test_marks.py -m custom_mark
@pytest.mark.asyncio
@pytest.mark.custom_mark(reason="This is a custom mark with a message")
async def test_get_user_custom_mark():
    async with httpx.AsyncClient() as client:
        # This test has a custom mark
        print()
        pass