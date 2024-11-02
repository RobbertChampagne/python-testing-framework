# python tests/api/module_b/setup/get_images.py

import httpx
from .cognito_token import get_cognito_token

async def get_image_id():
    headers = {
        'x-api-key': await get_cognito_token(),
        'Accept': 'application/json'
    }
    async with httpx.AsyncClient() as client:
        url = "https://api.thecatapi.com/v1/breeds?limit=2&page=0"
        response = await client.get(url, headers=headers)

    breeds  = response.json()
    image_id = breeds[0]["image"]["id"]
    #print(json.dumps(breeds, indent=4))
    return image_id
    
