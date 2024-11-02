# pytest -n 4 -s tests/api/module_a
# pytest -s tests/api/module_a/tests/test_mocking.py
# pytest tests/api/module_a/tests/test_mocking.py::test_get_user_mock 

import httpx
import pytest
import logging
import asyncio
from ...core.apis_info import ApiAbbreviation, apiUrls
from unittest.mock import AsyncMock, patch

# Configure the logger
logger = logging.getLogger(__name__) # __name__ is set to the module's name when it is executed

# Construct the URL for the API endpoint
url = apiUrls[ApiAbbreviation.Reqres] + "/users/8"
        
# Real API call
@pytest.mark.asyncio
async def test_get_user(caplog):
    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        
        # Make an asynchronous GET request to the API
        response = await client.get(url)
        
        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200

        # Extract the user data from the JSON response
        user = response.json()["data"]
 
        # Log the user data (for capturing in the HTML report)
        logger.info(f"User data: {user}")

# Mocking an API response
@pytest.mark.asyncio
async def test_get_user_mock():
    async def mock_get(*args, **kwargs): # Takes any arguments and keyword arguments.
        return httpx.Response( # Returns a mocked httpx.Response object
            status_code=200,
            json={"data": {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "avatar": "https://example.com/avatar.jpg"}}
        )

    # Uses the patch function from the unittest.mock module 
    # to replace the get method of httpx.AsyncClient with the mock_get function. 
    # This ensures that any calls to httpx.AsyncClient.get 
    # within this context will use the mocked response.
    with patch("httpx.AsyncClient.get", new=mock_get):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            assert response.status_code == 200
            user = response.json()["data"]
            logger.info(f"User data: {user}")

# Mocking an API Response with a Delay
# In this example, we'll mock an API response that includes a delay to simulate a slow network.
@pytest.mark.asyncio
async def test_get_user_with_delay():
    async def mock_get(*args, **kwargs):
        await asyncio.sleep(4)  # Simulate network delay
        return httpx.Response(
            status_code=200,
            json={"data": {"id": 1, "first_name": "John", "last_name": "Doe"}}
        )

    with patch("httpx.AsyncClient.get", new=mock_get):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            assert response.status_code == 200
            user = response.json()["data"]
            assert user["first_name"] == "John"
            logger.info(f"User data: {user}")

# Mocking an API response with different status codes
@pytest.mark.asyncio
async def test_get_user_not_found():
    async def mock_get(*args, **kwargs):
        return httpx.Response(status_code=404, json={"error": "User not found"})

    with patch("httpx.AsyncClient.get", new=mock_get):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            assert response.status_code == 404
            error = response.json()["error"]
            assert error == "User not found"


# Mocking a POST Request
@pytest.mark.asyncio
async def test_create_user():
    async def mock_post(*args, **kwargs):
        return httpx.Response(
            status_code=201,
            json={"name": "Jeff", "email": "jeff.doe@example.com"}
        )

    with patch("httpx.AsyncClient.post", new=mock_post):
        async with httpx.AsyncClient() as client:
            data = {"name": "John Doe", "email": "john.doe@example.com"}
            response = await client.post("https://reqres.in/api/users", json=data)
            assert response.status_code == 201
            user = response.json()
            assert user["name"] == "Jeff"
            assert user["email"] == "jeff.doe@example.com"
            logger.info(f"User data: {user}")
            




