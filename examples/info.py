import asyncio

from rawg import AioRawg


async def main():
    r = AioRawg()

    slug = 'grand-theft-auto-v'
    game = await r.info(slug)

    print(game.name, game.reddit_url)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
