import json
import httpx
from .cognito_token import get_cognito_token
from ...core.apis_info import ApiAbbreviation, apiUrls

async def get_image_id():
    headers = {
        'x-api-key': await get_cognito_token(),
        'Accept': 'application/json'
    }
    async with httpx.AsyncClient() as client:
        url = apiUrls[ApiAbbreviation.TheCatApi] + "/breeds?limit=2&page=0"
        response = await client.get(url, headers=headers)

    breeds  = response.json()
    image_id = breeds[0]["image"]["id"]
    print(json.dumps(breeds, indent=4))
    return image_id
    
