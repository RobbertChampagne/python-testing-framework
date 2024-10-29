import httpx

async def get_user(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.status_code, response.json()['data']