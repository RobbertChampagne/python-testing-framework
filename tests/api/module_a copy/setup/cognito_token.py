import os
from dotenv import load_dotenv
import aiofiles

# Load environment variables from .env file
load_dotenv()

token_file = "TEMP_TOKEN"

async def get_cognito_token():
    async with aiofiles.open(token_file, mode="r") as f:
        return await f.read()

async def write_cognito_token():
    token = await generate_cognito_token()
    async with aiofiles.open(token_file, mode="w") as f:
        if token is not None:
            await f.write(token)
        else:
            # Handle the case where token is None, e.g., log an error or raise an exception
            print("Token is None. Cannot write to file.")

async def unlink_cognito_token():
    if os.path.exists(token_file):
        os.remove(token_file)  # Delete the file
    else:
        print(f"File {token_file} does not exist.")

async def generate_cognito_token():
    # Your call to get the token here
    # ...
    # access_token = await response_token.json()
    # return f"bearer {access_token}"
    #
    # (For now get the token from the environment variables)
    token = os.getenv("CATAPIKEY")
    return token
