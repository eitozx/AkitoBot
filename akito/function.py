import aiohttp

async def nsfw(query : str):
    async with aiohttp.ClientSession() as session:
        url = f"http://api.nekos.fun:8080/api/{query}"
        response = await session.get(url)
        result = await response.json()
        return result