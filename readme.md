# RAWG.io API Wrapper

Simple example:
```python
import asyncio

from rawg import AIORawg


async def main():
    r = AIORawg()

    keyword = 'metal gear'
    search = await r.search(keyword, page_size=3)

    print('Found:', search.count)
    for game in search.results:
        print('--', game.name)
        print('----', 'Rating:', game.rating)
        for genre in game.genres:
            print('----', genre.name)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

Result:
```
Found: 1841
-- Metal Gear
---- Rating: 4.0
-- METAL GEAR RISING: REVENGEANCE
---- Rating: 4.13
---- Action
-- Metal Gear Solid
---- Rating: 4.22
---- Shooter
---- Adventure
---- Action
```
