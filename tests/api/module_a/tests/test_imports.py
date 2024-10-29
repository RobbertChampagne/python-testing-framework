# pytest -s api_integration_testing/module_a/tests/test_imports.py
  
import pytest
from ...core.apis_info import ApiAbbreviation, apiUrls
import asyncio
from ..setup.get_user import get_user
from ..setup.cognito_token import get_cognito_token

@pytest.mark.asyncio
async def test_get_user():
    url = apiUrls[ApiAbbreviation.Reqres] + "/users/8"
    status_code, user = await get_user(url)
    assert status_code == 200
    print(user)
    
@pytest.mark.asyncio
async def test_fetch_cognito():
    cognito_token = await get_cognito_token()  # Call the get_cognito_token function asynchronously
    print(cognito_token)
    
# Example of using fixtures directly in a test function
@pytest.mark.asyncio
async def test_fetch_env_vars(env, base_url):
    # env & base_url are automatically provided by the fixtures inside module_a\conftest.py
    print(env)
    print(base_url)
