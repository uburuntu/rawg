# rawg

[![Python](https://img.shields.io/badge/Python-2.7%20%7C%203.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue.svg?longCache=true)]()
[![PyPI](https://img.shields.io/pypi/v/rawg.svg)](https://pypi.python.org/pypi/rawg)
[![Build Status](https://travis-ci.org/uburuntu/rawg.svg?branch=master)](https://travis-ci.org/uburuntu/rawg)

API wrapper for RAWG.io

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

## Installation & Usage
### pip install

Install via PyPI (recommended):

```sh
pip install rawg
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

## Getting Started

#### Example
```python
import asyncio

import rawg


async def requests():
    async with rawg.ApiClient() as api_client:
        # Create an instance of the API class
        api = rawg.GamesApi(api_client)

        # Making requests
        coros = [api.games_read(id=name) for name in ['grand-theft-auto-v', 'minecraft']]

        # Waiting for requests
        for coro in asyncio.as_completed(coros):
            game: rawg.GameSingle = await coro
            print('        Name |', game.name)
            print('    Released |', game.released)
            print('      Rating |', game.rating)
            print('Achievements |', game.achievements_count)
            print('     Website |', game.website)
            print('  Metacritic |', game.metacritic)
            print('——————————————————————————————————————————————')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(requests())

```
#### Output

```text
        Name | Grand Theft Auto V
    Released | 2013-09-17
      Rating | 4.48
Achievements | 369
     Website | http://www.rockstargames.com/V/
  Metacritic | 97
——————————————————————————————————————————————
        Name | Minecraft
    Released | 2009-05-10
      Rating | 4.38
Achievements | 288
     Website | https://minecraft.net
  Metacritic | 83
——————————————————————————————————————————————
```

## Documentation for API Endpoints

All URIs are relative to *https://api.rawg.io/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CreatorRolesApi* | [**creator_roles_list**](docs/CreatorRolesApi.md#creator_roles_list) | **GET** /creator-roles | Get a list of creator positions (jobs).
*CreatorsApi* | [**creators_list**](docs/CreatorsApi.md#creators_list) | **GET** /creators | Get a list of game creators.
*CreatorsApi* | [**creators_read**](docs/CreatorsApi.md#creators_read) | **GET** /creators/{id} | Get details of the creator.
*DevelopersApi* | [**developers_list**](docs/DevelopersApi.md#developers_list) | **GET** /developers | Get a list of game developers.
*DevelopersApi* | [**developers_read**](docs/DevelopersApi.md#developers_read) | **GET** /developers/{id} | Get details of the developer.
*GamesApi* | [**games_achievements_read**](docs/GamesApi.md#games_achievements_read) | **GET** /games/{id}/achievements | Get a list of game achievements.
*GamesApi* | [**games_additions_list**](docs/GamesApi.md#games_additions_list) | **GET** /games/{game_pk}/additions | Get a list of DLC&#39;s for the game, GOTY and other editions, companion apps, etc.
*GamesApi* | [**games_development_team_list**](docs/GamesApi.md#games_development_team_list) | **GET** /games/{game_pk}/development-team | Get a list of individual creators that were part of the development team.
*GamesApi* | [**games_game_series_list**](docs/GamesApi.md#games_game_series_list) | **GET** /games/{game_pk}/game-series | Get a list of games that are part of the same series.
*GamesApi* | [**games_list**](docs/GamesApi.md#games_list) | **GET** /games | Get a list of games.
*GamesApi* | [**games_movies_read**](docs/GamesApi.md#games_movies_read) | **GET** /games/{id}/movies | Get a list of game trailers.
*GamesApi* | [**games_parent_games_list**](docs/GamesApi.md#games_parent_games_list) | **GET** /games/{game_pk}/parent-games | Get a list of parent games for DLC&#39;s and editions.
*GamesApi* | [**games_read**](docs/GamesApi.md#games_read) | **GET** /games/{id} | Get details of the game.
*GamesApi* | [**games_reddit_read**](docs/GamesApi.md#games_reddit_read) | **GET** /games/{id}/reddit | Get a list of most recent posts from the game&#39;s subreddit.
*GamesApi* | [**games_screenshots_list**](docs/GamesApi.md#games_screenshots_list) | **GET** /games/{game_pk}/screenshots | Get screenshots for the game.
*GamesApi* | [**games_sitemap_read**](docs/GamesApi.md#games_sitemap_read) | **GET** /games/sitemap | Get The Sitemap Games list.
*GamesApi* | [**games_stores_list**](docs/GamesApi.md#games_stores_list) | **GET** /games/{game_pk}/stores | Get links to the stores that sell the game.
*GamesApi* | [**games_suggested_read**](docs/GamesApi.md#games_suggested_read) | **GET** /games/{id}/suggested | Get a list of visually similar games.
*GamesApi* | [**games_twitch_read**](docs/GamesApi.md#games_twitch_read) | **GET** /games/{id}/twitch | Get streams on Twitch associated with the game .
*GamesApi* | [**games_youtube_read**](docs/GamesApi.md#games_youtube_read) | **GET** /games/{id}/youtube | Get videos from YouTube associated with the game.
*GenresApi* | [**genres_list**](docs/GenresApi.md#genres_list) | **GET** /genres | Get a list of video game genres.
*GenresApi* | [**genres_read**](docs/GenresApi.md#genres_read) | **GET** /genres/{id} | Get details of the genre.
*PlatformsApi* | [**platforms_list**](docs/PlatformsApi.md#platforms_list) | **GET** /platforms | Get a list of video game platforms.
*PlatformsApi* | [**platforms_lists_parents_list**](docs/PlatformsApi.md#platforms_lists_parents_list) | **GET** /platforms/lists/parents | Get a list of parent platforms.
*PlatformsApi* | [**platforms_read**](docs/PlatformsApi.md#platforms_read) | **GET** /platforms/{id} | Get details of the platform.
*PublishersApi* | [**publishers_list**](docs/PublishersApi.md#publishers_list) | **GET** /publishers | Get a list of video game publishers.
*PublishersApi* | [**publishers_read**](docs/PublishersApi.md#publishers_read) | **GET** /publishers/{id} | Get details of the publisher.
*StoresApi* | [**stores_list**](docs/StoresApi.md#stores_list) | **GET** /stores | Get a list of video game storefronts.
*StoresApi* | [**stores_read**](docs/StoresApi.md#stores_read) | **GET** /stores/{id} | Get details of the store.
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags | Get a list of tags.
*TagsApi* | [**tags_read**](docs/TagsApi.md#tags_read) | **GET** /tags/{id} | Get details of the tag.


## Documentation For Models

 - [Developer](docs/Developer.md)
 - [DeveloperSingle](docs/DeveloperSingle.md)
 - [Game](docs/Game.md)
 - [GamePersonList](docs/GamePersonList.md)
 - [GamePlatformMetacritic](docs/GamePlatformMetacritic.md)
 - [GameSingle](docs/GameSingle.md)
 - [GameStoreFull](docs/GameStoreFull.md)
 - [Genre](docs/Genre.md)
 - [GenreSingle](docs/GenreSingle.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Movie](docs/Movie.md)
 - [ParentAchievement](docs/ParentAchievement.md)
 - [Person](docs/Person.md)
 - [PersonSingle](docs/PersonSingle.md)
 - [Platform](docs/Platform.md)
 - [PlatformParentSingle](docs/PlatformParentSingle.md)
 - [PlatformSingle](docs/PlatformSingle.md)
 - [Position](docs/Position.md)
 - [Publisher](docs/Publisher.md)
 - [PublisherSingle](docs/PublisherSingle.md)
 - [Reddit](docs/Reddit.md)
 - [ScreenShot](docs/ScreenShot.md)
 - [Store](docs/Store.md)
 - [StoreSingle](docs/StoreSingle.md)
 - [Tag](docs/Tag.md)
 - [TagSingle](docs/TagSingle.md)
 - [Twitch](docs/Twitch.md)
 - [Youtube](docs/Youtube.md)


## API Docs

**Link**: https://rawg.io/apidocs

## Documentation For Authorization

Every API request should have a `User-Agent` header with your app name.

## Another libraries

**Python**: laundmo/[rawgpy](https://pypi.org/project/rawgpy)

**Node.js**: orels1/[rawger](https://github.com/orels1/rawger)

## Contact

[![](https://img.shields.io/badge/Telegram-@rm__bk-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAEbklEQVQ4y62US2xUdRjFf%2F%2F%2FfUynnXaGKW15FHnVKm8SRCFB3ZhYRVQSISHKBhKjK2JiTIyuXJC40oUrY%2BJGTZSABomiC0kUFYEIFRWrQi1tmXb6mE7be%2BfOvf%2F7%2F1z0Ydh71t93vpPz5RxlUoujFSOB4dxQQGKFUs2AFRIr9%2FRVzdO%2FVZNVvqPsjqL31%2BYl3icNjh4dDAyNrsPzm%2FL4riZOhRbfwWUeAohAe9ZhrG6af6mYF27X0gPVRHZ6jsYquDxpGAjSJ7rz3om2jHqv2VOLuwtQCwpHA8NvExEXx6JnTg6Eb0%2FU7UpPK3Kewp3bI05hOrEIkHPV1aPduRePbStesAKhseQ8B63V3HRHk8t3o9HLx3unTlRju7KjQVPwFM68chHwNLRlNB0NmtlEtr%2FZO%2FXjlwNBj1aKxM4rjJKUjKv5ZijY2%2FPF8JmuvE%2Fe%2B29gAVqBo6CeCkOBoT3rkFgo14y8%2B%2FCy9bs6sv2rci66HCZcG69lX%2Fq%2B%2FEGrr2lxFbERxAoiggY0Qjk0XB6NGJpN2NORZU3Oo8lRiBX14Z%2FVjypROnc46zqcvRUe7avEhVVNLnVjAcHVEBnL9cmIa%2BMRSzzNqzuWcvrxTk49tpINBZ8%2FKnW6WjzOl2q7LowEewDci6Nh57nh4Lmcq0itRaMYDQ3DMwltjR777sqxv6uFA13Nd1jQOx6R1aAEYmO5Ol5%2FFjjvfnZz5sDgdPJAq68RC4OzCe1ZhyP3t3Ho7jwbij4ApUrITJKybmmOSpRyqxpT8B2SVCj6Dr3j9e0A7ve3wy6FwtOKG1N1jm1v5Y3d7YtKarHhymCVfKPHpuUtAFwZrzMwk7A%2B72OskPcUlZopzHnoaJOKYK2lkHG4NBJy%2FKcxfh2LCGoxlwerrCg0LJIB9FfrRIkFmXtcnFpEJAXQPaubfnQgmK6nFD3FlXLEa%2BdK7Pn4Jt%2FerLCxNcua1qY7%2FLtYqqERsIISYSwwrGh0RwD00c3Fk1taM1%2BVZhJiKyzJaDYub6CaCH8HQjBW4cyv5TsIf5%2BIaHQUqVhEhGpk6Mr75wF0aTZJugv%2Bu1YEY4XUWlIrNHmKn8s1zo7E7Ds1yJMn%2BxcJ%2ByYjChmNFZiqGVobHJ5Y1%2Fw%2BgDsaGnrWNn91qRRe%2BLp%2Feld3a5bEWFY0aM4N1zg9AJ3LGvm8b4pHT9xkdYsHVshqhSPC7Yk6h7YW3%2BlZ2zwAoH4ph6xo9vhhKOg8cmbgulEq197kYUWI5%2BPna%2FAcRX81JjLChmIGC%2FSVa%2BzszPV9un%2FNFoRkZbOHrqfCWJiitRp6ZH1%2Bj68YuTFVJ04FX4GrhNQKUWLpzHl0F3wmaoYbkxH3Lm24%2Bvru9gcLvpPUzHz0FoI%2FW7fE1vYe3lK8b%2B%2FalhNBnFIOEyZDgxXBpEJ5NqE0m5BxVPpQZ%2B6tV3a17xAYGw0NC621WLBKwXQ9pcV3hw9vzh3M%2BWr74ExyMDGy7XaQLHM1srUt2681l5%2Fqyn9shH8mohTf0TgK0vmWVSLC%2F4l%2FAXWxRtaDbtHIAAAAAElFTkSuQmCC)](https://t.me/rm_bk)