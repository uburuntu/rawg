import asyncio

import rawg


async def requests():
    async with rawg.ApiClient(rawg.Configuration(api_key={'key': 'YOUR_API_KEY'})) as api_client:
        # Create an instance of the API class
        api = rawg.GamesApi(api_client)

        # Making requests
        coros = [api.games_read(id=name) for name in ['grand-theft-auto-v', 'minecraft']]

        # Waiting for requests
        for coro in asyncio.as_completed(coros):
            game: rawg.GameSingle = await coro
            print('——————————————————————————————————————————————')
            print('        Name |', game.name)
            print('    Released |', game.released)
            print('      Rating |', game.rating)
            print('Achievements |', game.achievements_count)
            print('     Website |', game.website)
            print('  Metacritic |', game.metacritic)
            print('——————————————————————————————————————————————')
            print()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(requests())
