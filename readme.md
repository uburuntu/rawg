# RAWG.io API Wrapper

[![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/rawg.svg)](https://pypi.python.org/pypi/rawg)

[![Build Status](https://travis-ci.org/uburuntu/rawg.svg?branch=master)](https://travis-ci.org/uburuntu/rawg)
[![codecov](https://codecov.io/gh/uburuntu/rawg/branch/master/graph/badge.svg)](https://codecov.io/gh/uburuntu/rawg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aaf685a78dbf4377b8f36b401a5ccda1)](https://www.codacy.com/app/uburuntu/rawg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=uburuntu/rawg&amp;utm_campaign=Badge_Grade)

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

## Contact

[![](https://img.shields.io/badge/Telegram-@rm__bk-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAEbklEQVQ4y62US2xUdRjFf%2F%2F%2FfUynnXaGKW15FHnVKm8SRCFB3ZhYRVQSISHKBhKjK2JiTIyuXJC40oUrY%2BJGTZSABomiC0kUFYEIFRWrQi1tmXb6mE7be%2BfOvf%2F7%2F1z0Ydh71t93vpPz5RxlUoujFSOB4dxQQGKFUs2AFRIr9%2FRVzdO%2FVZNVvqPsjqL31%2BYl3icNjh4dDAyNrsPzm%2FL4riZOhRbfwWUeAohAe9ZhrG6af6mYF27X0gPVRHZ6jsYquDxpGAjSJ7rz3om2jHqv2VOLuwtQCwpHA8NvExEXx6JnTg6Eb0%2FU7UpPK3Kewp3bI05hOrEIkHPV1aPduRePbStesAKhseQ8B63V3HRHk8t3o9HLx3unTlRju7KjQVPwFM68chHwNLRlNB0NmtlEtr%2FZO%2FXjlwNBj1aKxM4rjJKUjKv5ZijY2%2FPF8JmuvE%2Fe%2B29gAVqBo6CeCkOBoT3rkFgo14y8%2B%2FCy9bs6sv2rci66HCZcG69lX%2Fq%2B%2FEGrr2lxFbERxAoiggY0Qjk0XB6NGJpN2NORZU3Oo8lRiBX14Z%2FVjypROnc46zqcvRUe7avEhVVNLnVjAcHVEBnL9cmIa%2BMRSzzNqzuWcvrxTk49tpINBZ8%2FKnW6WjzOl2q7LowEewDci6Nh57nh4Lmcq0itRaMYDQ3DMwltjR777sqxv6uFA13Nd1jQOx6R1aAEYmO5Ol5%2FFjjvfnZz5sDgdPJAq68RC4OzCe1ZhyP3t3Ho7jwbij4ApUrITJKybmmOSpRyqxpT8B2SVCj6Dr3j9e0A7ve3wy6FwtOKG1N1jm1v5Y3d7YtKarHhymCVfKPHpuUtAFwZrzMwk7A%2B72OskPcUlZopzHnoaJOKYK2lkHG4NBJy%2FKcxfh2LCGoxlwerrCg0LJIB9FfrRIkFmXtcnFpEJAXQPaubfnQgmK6nFD3FlXLEa%2BdK7Pn4Jt%2FerLCxNcua1qY7%2FLtYqqERsIISYSwwrGh0RwD00c3Fk1taM1%2BVZhJiKyzJaDYub6CaCH8HQjBW4cyv5TsIf5%2BIaHQUqVhEhGpk6Mr75wF0aTZJugv%2Bu1YEY4XUWlIrNHmKn8s1zo7E7Ds1yJMn%2BxcJ%2ByYjChmNFZiqGVobHJ5Y1%2Fw%2BgDsaGnrWNn91qRRe%2BLp%2Feld3a5bEWFY0aM4N1zg9AJ3LGvm8b4pHT9xkdYsHVshqhSPC7Yk6h7YW3%2BlZ2zwAoH4ph6xo9vhhKOg8cmbgulEq197kYUWI5%2BPna%2FAcRX81JjLChmIGC%2FSVa%2BzszPV9un%2FNFoRkZbOHrqfCWJiitRp6ZH1%2Bj68YuTFVJ04FX4GrhNQKUWLpzHl0F3wmaoYbkxH3Lm24%2Bvru9gcLvpPUzHz0FoI%2FW7fE1vYe3lK8b%2B%2FalhNBnFIOEyZDgxXBpEJ5NqE0m5BxVPpQZ%2B6tV3a17xAYGw0NC621WLBKwXQ9pcV3hw9vzh3M%2BWr74ExyMDGy7XaQLHM1srUt2681l5%2Fqyn9shH8mohTf0TgK0vmWVSLC%2F4l%2FAXWxRtaDbtHIAAAAAElFTkSuQmCC)](https://t.me/rm_bk)
