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
    ])
    async def test_types_by_search(self, keyword):
        await self.rawg.search(keyword, page_size=10)

    @pytest.mark.parametrize('slug', [
        'grand-theft-auto-v',
        'minecraft',
        'metal-gear-solid-v-the-phantom-pain',
        'dark-souls',
    ])
    async def test_search(self, slug):
        await self.rawg.info(slug)

    @pytest.mark.parametrize('slug', [
        'grand-theft-auto-v',
        'minecraft',
        'metal-gear-solid-v-the-phantom-pain',
        'dark-souls',
    ])
    async def test_search(self, slug):
        await self.rawg.suggested(slug)
