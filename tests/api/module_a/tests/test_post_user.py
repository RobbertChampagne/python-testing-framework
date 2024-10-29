# pytest -s api_integration_testing/module_a/tests/test_post_user.py

import httpx
import pytest
from jsonschema import validate
from ...core.apis_info import ApiAbbreviation, apiUrls

user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"},
    },
    "required": ["name", "email", "id", "createdAt"],
}

@pytest.mark.asyncio
async def test_post_user():
    async with httpx.AsyncClient() as client:
        url = apiUrls[ApiAbbreviation.Reqres] + "/users"
        data = {"name": "John Doe", "email": "john.doe@example.com"}
        response = await client.post(url, json=data)
        assert response.status_code == 201
        user = response.json()
        assert user["name"] == "John Doe"
        assert user["email"] == "john.doe@example.com"
        
        # In JavaScript, this kind of data structure is called an "object", and in Python, it's called a "dictionary".
        assert isinstance(user, dict)

        # Check that the user has the required fields
        validate(instance=user, schema=user_schema)
