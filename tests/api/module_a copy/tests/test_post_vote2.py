# pytest -n 4 -s api_integration_testing/module_b --html=report.html
# pytest -s --log-cli-level=INFO api_integration_testing/module_b/tests/test_post_vote.py --html=report.html

import httpx
import pytest
import logging
from ..setup.get_image_id import get_image_id
from ..setup.cognito_token import get_cognito_token

@pytest.mark.asyncio
async def test_post_vote():
    image_id = await get_image_id()
    
    headers = {
        'x-api-key': await get_cognito_token(),
        'Accept': 'application/json'
    }
    
    data = {
        "image_id": image_id,
        "sub_id": "my-user-1234",
        "value":2
    }
    
    async with httpx.AsyncClient() as client:
        url = "https://api.thecatapi.com/v1/votes"
        response = await client.post(url, headers=headers, json=data)
        assert response.status_code == 201
        logging.info("This is an info log message.")