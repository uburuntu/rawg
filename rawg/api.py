import asyncio
from typing import Optional

import aiohttp

from rawg.types import RawgGame, RawgSearch


class AIORawg:
    api_url = 'https://api.rawg.io/api/'

    def __init__(self, app_name: str = 'aiorawg'):
        self.app_name = app_name

        self._headers: dict = {'User-Agent': self.app_name}
        self._session: Optional[aiohttp.ClientSession] = None

    async def request(self, endpoint, **params):
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, params=params, headers=self._headers) as response:
                if response.status == 200:
                    return await response.json()
                response.raise_for_status()

    async def search(self, keyword: str, page_size: int = 5) -> RawgSearch:
        endpoint = self.api_url + f'games'
        result = await self.request(endpoint, search=keyword, page_size=page_size)
        return RawgSearch(**result)

    async def info(self, game) -> RawgGame:
        endpoint = self.api_url + f'games/{game}'
        result = await self.request(endpoint)
        return RawgGame(**result)

    async def suggested(self, game, page_size: int = 5):
        endpoint = self.api_url + f'games/{game}/suggested'
        result = await self.request(endpoint, page_size=page_size)
        return result
