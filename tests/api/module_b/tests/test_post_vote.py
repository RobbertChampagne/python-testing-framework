# pytest -n 4 tests/api/module_b
# pytest -s tests/api/module_b/tests/test_post_vote.py 

import httpx
import pytest
import logging
from ..setup.get_image_id import get_image_id
from ..setup.cognito_token import get_cognito_token
from ...core.apis_info import ApiAbbreviation, apiUrls

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
        "value":1
    }
    
    async with httpx.AsyncClient() as client:
        url = apiUrls[ApiAbbreviation.TheCatApi] + "/votes"
        response = await client.post(url, headers=headers, json=data)
        assert response.status_code == 201
        logging.info("This is an info log message.")