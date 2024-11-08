# pytest -n 4 tests/api/module_c
# pytest tests/api/module_c/tests/test_post_vote2.py

import httpx
import pytest
import logging
from ..setup.get_image_id import get_image_id
from ..setup.cognito_token import get_cognito_token
from ...core.apis_info import ApiAbbreviation, apiUrls

# Setup logging configuration
logger = logging.getLogger("post vote 2") 

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
        url = apiUrls[ApiAbbreviation.TheCatApi] + "/votes"
        response = await client.post(url, headers=headers, json=data)
        assert response.status_code == 201
        logger.info("This is an info log message.")