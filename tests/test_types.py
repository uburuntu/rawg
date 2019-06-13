import pytest

from rawg import AIORawg

pytestmark = pytest.mark.asyncio


class TestTypes:
    def setup_class(self):
        self.rawg = AIORawg()

    @pytest.mark.parametrize('keyword', [
        'gta v',
        'minecraft',
        'metal gear',
        'dark souls',
    ])
    async def test_types_by_search(self, keyword):
        await self.rawg.search(keyword, page_size=1000)
