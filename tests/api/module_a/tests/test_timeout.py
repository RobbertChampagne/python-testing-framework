# pytest -s tests/api/module_a
# pytest tests/api/module_a/tests/test_timeout.py 
# pytest tests/api/module_a/tests/test_timeout.py::test_get_user_parametrize 

import httpx
import pytest
import logging
import asyncio
from ...core.apis_info import ApiAbbreviation, apiUrls

# Configure the logger
logger = logging.getLogger(__name__) # __name__ is set to the module's name when it is executed

@pytest.mark.asyncio
async def test_sleep():
    try:
        # Create an asynchronous HTTP client
        async with httpx.AsyncClient() as client:
            # Construct the URL for the API endpoint
            url = apiUrls[ApiAbbreviation.Reqres] + "/users?delay=3"
            
            # Make an asynchronous GET request to the API with a timeout
            response = await asyncio.wait_for(client.get(url), timeout=1)
                
            # Assert that the response status code is 200 (OK)
            assert response.status_code == 200

            # Extract the user data from the JSON response
            user = response.json()["data"]
                
            # Log the user data (for capturing in the HTML report)
            logger.info(f"User data: {user}")
    except asyncio.TimeoutError:
        logger.error("Timeout occurred during the request")
        raise
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e  # Re-raise the exception to ensure the test fails

