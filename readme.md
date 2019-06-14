# RAWG.io API Wrapper

[![Python ⩾ 3.6](https://img.shields.io/badge/Python-⩾_3.6-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/rawg.svg)](https://pypi.python.org/pypi/rawg)

Pretty simple API wrapper for RAWG.io with typings.

You can use both sync and async realizations. 

_Contributions are welcome!_

## API Usage

### Installation
Just
```
pip install rawg
``` 
or maybe `pip3`.

### Simple example
```python
from rawg import Rawg

r = Rawg()
s = r.search('half life 3')

result = s.results[0]
print(result.name, result.released)
```

### Async example

```python
import asyncio

from rawg import AioRawg
from rawg.types import RawgGame


async def main():
    rawg = AioRawg()

    search = await rawg.search('metal gear', page_size=3)
    requests = [rawg.info(game) for game in search.results]

    print('Search results:', search.count)
    for request in asyncio.as_completed(requests):
        game: RawgGame = await request
        print(game.name)
        print('--', 'Released:', game.released)
        print('--', 'Rating:', game.rating)
        print('--', 'Genres:', ', '.join(genre.name for genre in game.genres))
        print('--', 'Available on:', ', '.join(p.platform.name for p in game.platforms))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

Result:
```
Search results: 1846
Metal Gear Solid
-- Released: 1998-09-03
-- Rating: 4.23
-- Genres: Action, Shooter, Adventure
-- Available on: PlayStation, PS Vita, PC, PSP, PlayStation 3
Metal Gear
-- Released: 1987-07-07
-- Rating: 3.95
-- Genres: 
-- Available on: PC, Wii, NES, Commodore / Amiga
METAL GEAR RISING: REVENGEANCE
-- Released: 2013-02-19
-- Rating: 4.14
-- Genres: Action
-- Available on: Xbox 360, PlayStation 3, PC
```

### Manual

#### Methods
API have 3 methods:
* `search` — search for a game by name, return type: `RawgSearch`
  * `RawgSearch` have attribute `results` of type `List[RawgGameSearch]`
* `suggested` — find more similar games via RAWG ML, return type: `RawgSuggested`
  * `RawgSuggested` have attribute `results` of type `List[RawgGameSuggested]`
* `info` — detailed information about the game, return type: `RawgGame`
  * `RawgGame` is more detailed than `RawgGameSearch` and `RawgGameSuggested`

#### Types
This library uses [pydantic](https://github.com/samuelcolvin/pydantic/) for parsing API responses.
Main types are: `RawgPlatformData`, `RawgPlatform`, `RawgStoreData`, `RawgStore`, `RawgRating`, `RawgAddedByStatus`, `RawgChartYear`, `RawgCharts`, `RawgClips`, `RawgClip`, `RawgScreenshot`, `RawgGenre`, `RawgGameBase`, `RawgGame`, `RawgGameSearch`, `RawgGameSuggested`, `RawgSearch`. And declared in [rawg/types.py](rawg/types.py).


### In case of unsupported types
API results can change and the library may not parse the new result. So you can use parameter `raw_results` for requesting «raw» dicts: 
```python
r = AioRawg(raw_results=True)
# Or
r = Rawg(raw_results=True)
```

## API Docs

**Link**: https://rawg.io/apidocs

#### API Rules
* every API request should have a `User-Agent` header with your app name
  * You can set your app name through argument `app_name`: `Rawg(app_name='Meduza')` or `AioRawg(app_name='Rawg.io Telegram Bot')` 
* no mass extraction & no cloning RAWG


## Another libraries

**Python**: laundmo/[rawgpy](https://pypi.org/project/rawgpy)

**Node.js**: orels1/[rawger](https://github.com/orels1/rawger)
