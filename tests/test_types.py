import asyncio

import pytest

from rawg import AioRawg

pytestmark = pytest.mark.asyncio


class TestTypes:
    def setup_class(self):
        self.rawg = AioRawg()

    @pytest.mark.parametrize('keyword', [
        'gta v',
        'minecraft',
        'metal gear',
        'dark souls',
        'half life',
    ])
    async def test_types_by_search(self, keyword):
        search = await self.rawg.search(keyword, page_size=1000)
        coros = [self.rawg.info(game) for game in search.results]
        await asyncio.gather(*coros)

    @pytest.mark.parametrize('slug', [
        'grand-theft-auto-v',
        'minecraft',
        'metal-gear-solid-v-the-phantom-pain',
        'dark-souls',
        'half-life-2',
    ])
    async def test_types_by_suggested(self, slug):
        search = await self.rawg.suggested(slug, page_size=1000)
        coros = [self.rawg.info(game) for game in search.results]
        await asyncio.gather(*coros)
