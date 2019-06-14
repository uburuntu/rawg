from typing import Union

import aiohttp
import requests

from rawg.types import RawgGame, RawgGameBase, RawgSearch, RawgSuggested


class BaseRawg:
    api_url = 'https://api.rawg.io/api/'

    class Endpoints:
        search = 'games'
        info = 'games/{slug}'
        suggested = 'games/{slug}/suggested'

    def __init__(self, app_info: str = 'github.com/uburuntu/rawg', raw_results: bool = False):
        self.app_info = app_info
        self.raw_results = raw_results
        self._headers: dict = {'User-Agent': self.app_info}

    @staticmethod
    def extract_slug(game: Union[str, dict, RawgGameBase]):
        if isinstance(game, dict):
            return game.get('slug')
        if isinstance(game, RawgGameBase):
            return game.slug
        return game


class AioRawg(BaseRawg):
    async def request(self, endpoint, **params) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url + endpoint, params=params, headers=self._headers) as response:
                if response.status == 200:
                    return await response.json()
                response.raise_for_status()

    async def search(self, keyword: str, page_size: int = 5) -> Union[dict, RawgSearch]:
        endpoint = self.Endpoints.search
        result = await self.request(endpoint, search=keyword, page_size=page_size)
        return result if self.raw_results else RawgSearch(**result)

    async def info(self, game: Union[str, dict, RawgGameBase]) -> Union[dict, RawgGame]:
        endpoint = self.Endpoints.info
        result = await self.request(endpoint.format(slug=self.extract_slug(game)))
        return result if self.raw_results else RawgGame(**result)

    async def suggested(self, game: Union[str, dict, RawgGameBase], page_size: int = 5) -> Union[dict, RawgSuggested]:
        endpoint = self.Endpoints.suggested
        result = await self.request(endpoint.format(slug=self.extract_slug(game)), page_size=page_size)
        return result if self.raw_results else RawgSuggested(**result)


class Rawg(BaseRawg):
    @property
    def session(self) -> requests.Session:
        session = getattr(self, '_session', None)
        if session is None:
            session = requests.Session()
            setattr(self, '_session', session)
        return session

    def request(self, endpoint, **params) -> dict:
        response = self.session.get(self.api_url + endpoint, params=params, headers=self._headers)
        if response.ok:
            return response.json()
        response.raise_for_status()

    def search(self, keyword: str, page_size: int = 5) -> Union[dict, RawgSearch]:
        endpoint = self.Endpoints.search
        result = self.request(endpoint, search=keyword, page_size=page_size)
        return result if self.raw_results else RawgSearch(**result)

    def info(self, game: Union[str, dict, RawgGameBase]) -> Union[dict, RawgGame]:
        endpoint = self.Endpoints.info
        result = self.request(endpoint.format(slug=self.extract_slug(game)))
        return result if self.raw_results else RawgGame(**result)

    def suggested(self, game: Union[str, dict, RawgGameBase], page_size: int = 5) -> Union[dict, RawgSuggested]:
        endpoint = self.Endpoints.suggested
        result = self.request(endpoint.format(slug=self.extract_slug(game)), page_size=page_size)
        return result if self.raw_results else RawgSuggested(**result)
