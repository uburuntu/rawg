# rawg

[![PyPI](https://img.shields.io/pypi/v/rawg.svg)](https://pypi.python.org/pypi/rawg)

API wrapper for RAWG.io

This Python package is **generated** by the [OpenAPI Generator](https://openapi-generator.tech) project.

Latest update: November 2022

## Installation & Usage
### pip install

Install via PyPI:

```sh
pip install rawg
```

## Getting Started

#### Example
```python
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

```
#### Output

```text
——————————————————————————————————————————————
        Name | Grand Theft Auto V
    Released | 2013-09-17
      Rating | 4.47
Achievements | 539
     Website | http://www.rockstargames.com/V/
  Metacritic | 91
——————————————————————————————————————————————
        Name | Minecraft
    Released | 2009-05-10
      Rating | 4.42
Achievements | 744
     Website | https://classic.minecraft.net/
  Metacritic | 83
——————————————————————————————————————————————
```

## API Docs and API Key

**Link**: https://rawg.io/apidocs

## Another libraries

**R**: rabiibouhestine/[Rawg](https://github.com/rabiibouhestine/Rawg)

**Python**: laundmo/[rawgpy](https://pypi.org/project/rawgpy)

**Node.js**: orels1/[rawger](https://github.com/orels1/rawger)

## Contact

[![](https://img.shields.io/badge/Telegram-@rm__bk-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAEbklEQVQ4y62US2xUdRjFf%2F%2F%2FfUynnXaGKW15FHnVKm8SRCFB3ZhYRVQSISHKBhKjK2JiTIyuXJC40oUrY%2BJGTZSABomiC0kUFYEIFRWrQi1tmXb6mE7be%2BfOvf%2F7%2F1z0Ydh71t93vpPz5RxlUoujFSOB4dxQQGKFUs2AFRIr9%2FRVzdO%2FVZNVvqPsjqL31%2BYl3icNjh4dDAyNrsPzm%2FL4riZOhRbfwWUeAohAe9ZhrG6af6mYF27X0gPVRHZ6jsYquDxpGAjSJ7rz3om2jHqv2VOLuwtQCwpHA8NvExEXx6JnTg6Eb0%2FU7UpPK3Kewp3bI05hOrEIkHPV1aPduRePbStesAKhseQ8B63V3HRHk8t3o9HLx3unTlRju7KjQVPwFM68chHwNLRlNB0NmtlEtr%2FZO%2FXjlwNBj1aKxM4rjJKUjKv5ZijY2%2FPF8JmuvE%2Fe%2B29gAVqBo6CeCkOBoT3rkFgo14y8%2B%2FCy9bs6sv2rci66HCZcG69lX%2Fq%2B%2FEGrr2lxFbERxAoiggY0Qjk0XB6NGJpN2NORZU3Oo8lRiBX14Z%2FVjypROnc46zqcvRUe7avEhVVNLnVjAcHVEBnL9cmIa%2BMRSzzNqzuWcvrxTk49tpINBZ8%2FKnW6WjzOl2q7LowEewDci6Nh57nh4Lmcq0itRaMYDQ3DMwltjR777sqxv6uFA13Nd1jQOx6R1aAEYmO5Ol5%2FFjjvfnZz5sDgdPJAq68RC4OzCe1ZhyP3t3Ho7jwbij4ApUrITJKybmmOSpRyqxpT8B2SVCj6Dr3j9e0A7ve3wy6FwtOKG1N1jm1v5Y3d7YtKarHhymCVfKPHpuUtAFwZrzMwk7A%2B72OskPcUlZopzHnoaJOKYK2lkHG4NBJy%2FKcxfh2LCGoxlwerrCg0LJIB9FfrRIkFmXtcnFpEJAXQPaubfnQgmK6nFD3FlXLEa%2BdK7Pn4Jt%2FerLCxNcua1qY7%2FLtYqqERsIISYSwwrGh0RwD00c3Fk1taM1%2BVZhJiKyzJaDYub6CaCH8HQjBW4cyv5TsIf5%2BIaHQUqVhEhGpk6Mr75wF0aTZJugv%2Bu1YEY4XUWlIrNHmKn8s1zo7E7Ds1yJMn%2BxcJ%2ByYjChmNFZiqGVobHJ5Y1%2Fw%2BgDsaGnrWNn91qRRe%2BLp%2Feld3a5bEWFY0aM4N1zg9AJ3LGvm8b4pHT9xkdYsHVshqhSPC7Yk6h7YW3%2BlZ2zwAoH4ph6xo9vhhKOg8cmbgulEq197kYUWI5%2BPna%2FAcRX81JjLChmIGC%2FSVa%2BzszPV9un%2FNFoRkZbOHrqfCWJiitRp6ZH1%2Bj68YuTFVJ04FX4GrhNQKUWLpzHl0F3wmaoYbkxH3Lm24%2Bvru9gcLvpPUzHz0FoI%2FW7fE1vYe3lK8b%2B%2FalhNBnFIOEyZDgxXBpEJ5NqE0m5BxVPpQZ%2B6tV3a17xAYGw0NC621WLBKwXQ9pcV3hw9vzh3M%2BWr74ExyMDGy7XaQLHM1srUt2681l5%2Fqyn9shH8mohTf0TgK0vmWVSLC%2F4l%2FAXWxRtaDbtHIAAAAAElFTkSuQmCC)](https://t.me/rm_bk)

---

# Generated README below

The largest open video games database.

### Why build on RAWG
- More than 350,000 games for 50 platforms including mobiles.
- Rich metadata: tags, genres, developers, publishers, individual creators, official websites, release dates,
Metacritic ratings.
- Where to buy: links to digital distribution services
- Similar games based on visual similarity.
- Player activity data: Steam average playtime and RAWG player counts and ratings.
- Actively developing and constantly getting better by user contribution and our algorithms.

### Terms of Use
- Free for personal use as long as you attribute RAWG as the source of the data and/or images and add an active
hyperlink from every page where the data of RAWG is used.
- Free for commercial use for startups and hobby projects with not more than 100,000 monthly active users or 500,000
page views per month. If your project is larger than that, email us at [api@rawg.io](mailto:api@rawg.io) for
commercial terms.
- No cloning. It would not be cool if you used our API to launch a clone of RAWG. We know it is not always easy
to say what is a duplicate and what isn't. Drop us a line at [api@rawg.io](mailto:api@rawg.io) if you are in doubt,
and we will talk it through.
- You must include an API key with every request. The key can be obtained at https://rawg.io/apidocs.
If you don’t provide it, we may ban your requests.

__[Read more](https://rawg.io/apidocs)__.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.0
- Package version: 1.2.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/uburuntu/rawg.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/uburuntu/rawg.git`)

Then import the package:
```python
import rawg
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rawg
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import rawg
from rawg.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rawg.io/api
# See configuration.py for a list of all supported configuration parameters.
configuration = rawg.Configuration(
    host = "https://api.rawg.io/api"
)



# Enter a context with an instance of the API client
with rawg.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rawg.CreatorRolesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of creator positions (jobs).
        api_response = api_instance.creator_roles_list(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CreatorRolesApi->creator_roles_list: %s\n" % e)
    
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
*GamesApi* | [**games_stores_list**](docs/GamesApi.md#games_stores_list) | **GET** /games/{game_pk}/stores | Get links to the stores that sell the game.
*GamesApi* | [**games_suggested_read**](docs/GamesApi.md#games_suggested_read) | **GET** /games/{id}/suggested | Get a list of visually similar games, available only for business and enterprise API users.
*GamesApi* | [**games_twitch_read**](docs/GamesApi.md#games_twitch_read) | **GET** /games/{id}/twitch | Get streams on Twitch associated with the game, available only for business and enterprise API users.
*GamesApi* | [**games_youtube_read**](docs/GamesApi.md#games_youtube_read) | **GET** /games/{id}/youtube | Get videos from YouTube associated with the game, available only for business and enterprise API users.
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

 - [CreatorRolesList200Response](docs/CreatorRolesList200Response.md)
 - [CreatorsList200Response](docs/CreatorsList200Response.md)
 - [Developer](docs/Developer.md)
 - [DeveloperSingle](docs/DeveloperSingle.md)
 - [DevelopersList200Response](docs/DevelopersList200Response.md)
 - [Game](docs/Game.md)
 - [GameEsrbRating](docs/GameEsrbRating.md)
 - [GamePersonList](docs/GamePersonList.md)
 - [GamePlatformMetacritic](docs/GamePlatformMetacritic.md)
 - [GamePlatformsInner](docs/GamePlatformsInner.md)
 - [GamePlatformsInnerPlatform](docs/GamePlatformsInnerPlatform.md)
 - [GamePlatformsInnerRequirements](docs/GamePlatformsInnerRequirements.md)
 - [GameSingle](docs/GameSingle.md)
 - [GameStoreFull](docs/GameStoreFull.md)
 - [GamesDevelopmentTeamList200Response](docs/GamesDevelopmentTeamList200Response.md)
 - [GamesList200Response](docs/GamesList200Response.md)
 - [GamesScreenshotsList200Response](docs/GamesScreenshotsList200Response.md)
 - [GamesStoresList200Response](docs/GamesStoresList200Response.md)
 - [Genre](docs/Genre.md)
 - [GenreSingle](docs/GenreSingle.md)
 - [GenresList200Response](docs/GenresList200Response.md)
 - [Movie](docs/Movie.md)
 - [ParentAchievement](docs/ParentAchievement.md)
 - [Person](docs/Person.md)
 - [PersonSingle](docs/PersonSingle.md)
 - [Platform](docs/Platform.md)
 - [PlatformParentSingle](docs/PlatformParentSingle.md)
 - [PlatformSingle](docs/PlatformSingle.md)
 - [PlatformsList200Response](docs/PlatformsList200Response.md)
 - [PlatformsListsParentsList200Response](docs/PlatformsListsParentsList200Response.md)
 - [Position](docs/Position.md)
 - [Publisher](docs/Publisher.md)
 - [PublisherSingle](docs/PublisherSingle.md)
 - [PublishersList200Response](docs/PublishersList200Response.md)
 - [Reddit](docs/Reddit.md)
 - [ScreenShot](docs/ScreenShot.md)
 - [Store](docs/Store.md)
 - [StoreSingle](docs/StoreSingle.md)
 - [StoresList200Response](docs/StoresList200Response.md)
 - [Tag](docs/Tag.md)
 - [TagSingle](docs/TagSingle.md)
 - [TagsList200Response](docs/TagsList200Response.md)
 - [Twitch](docs/Twitch.md)
 - [Youtube](docs/Youtube.md)
