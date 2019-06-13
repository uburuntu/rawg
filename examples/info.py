import asyncio

from rawg import AIORawg


async def main():
    r = AIORawg()

    slug = 'grand-theft-auto-v'
    game = await r.info(slug)

    print(game.name, game.reddit_url)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
