import pytest

from rawg import Rawg


class TestApi:
    def setup_class(self):
        self.rawg = Rawg()

    @pytest.mark.parametrize('keyword', [
        'gta v',
        'minecraft',
        'metal gear',
        'dark souls',
        'half life',
    ])
    def test_search(self, keyword):
        self.rawg.search(keyword, page_size=10)

    @pytest.mark.parametrize('slug', [
        'grand-theft-auto-v',
        'minecraft',
        'metal-gear-solid-v-the-phantom-pain',
        'dark-souls',
        'half-life-2',
    ])
    def test_search(self, slug):
        self.rawg.info(slug)

    @pytest.mark.parametrize('slug', [
        'grand-theft-auto-v',
        'minecraft',
        'metal-gear-solid-v-the-phantom-pain',
        'dark-souls',
        'half-life-2',
    ])
    def test_search(self, slug):
        self.rawg.suggested(slug)
