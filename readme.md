# RAWG.io API Wrapper

[![Python ⩾ 3.6](https://img.shields.io/badge/Python-⩾_3.6-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/rawg.svg)](https://pypi.python.org/pypi/rawg)

## Simple example

```python
import asyncio

from rawg import AioRawg


async def main():
    r = AioRawg()

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
