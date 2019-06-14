import asyncio

from rawg import AioRawg
from rawg.types import RawgGame


async def main():
    rawg = AioRawg()

    search = await rawg.search('metal gear', page_size=3)
    requests = [rawg.info(game) for game in search.results]

    print('Search results:', search.count)
    for request in asyncio.as_completed(requests):
        # Explicit typing usage cause of asyncio
        game: RawgGame = await request
        print(game.name)
        print('--', 'Released:', game.released)
        print('--', 'Rating:', game.rating)
        print('--', 'Genres:', ', '.join(genre.name for genre in game.genres))
        print('--', 'Available on:', ', '.join(p.platform.name for p in game.platforms))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
