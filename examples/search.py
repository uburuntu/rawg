import asyncio

from rawg import AioRawg


async def main():
    rawg = AioRawg()

    keyword = 'metal gear'
    search = await rawg.search(keyword, page_size=3)

    print('Found:', search.count)
    for game in search.results:
        print('--', game.name)
        print('----', 'Rating:', game.rating)
        for genre in game.genres:
            print('----', genre.name)

    search = await rawg.search(keyword, page_size=1000)
    coros = [rawg.info(game) for game in search.results]
    await asyncio.gather(*coros)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
