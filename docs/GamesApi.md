# rawg.GamesApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**games_achievements_read**](GamesApi.md#games_achievements_read) | **GET** /games/{id}/achievements | Get a list of game achievements.
[**games_additions_list**](GamesApi.md#games_additions_list) | **GET** /games/{game_pk}/additions | Get a list of DLC&#39;s for the game, GOTY and other editions, companion apps, etc.
[**games_development_team_list**](GamesApi.md#games_development_team_list) | **GET** /games/{game_pk}/development-team | Get a list of individual creators that were part of the development team.
[**games_game_series_list**](GamesApi.md#games_game_series_list) | **GET** /games/{game_pk}/game-series | Get a list of games that are part of the same series.
[**games_list**](GamesApi.md#games_list) | **GET** /games | Get a list of games.
[**games_movies_read**](GamesApi.md#games_movies_read) | **GET** /games/{id}/movies | Get a list of game trailers.
[**games_parent_games_list**](GamesApi.md#games_parent_games_list) | **GET** /games/{game_pk}/parent-games | Get a list of parent games for DLC&#39;s and editions.
[**games_read**](GamesApi.md#games_read) | **GET** /games/{id} | Get details of the game.
[**games_reddit_read**](GamesApi.md#games_reddit_read) | **GET** /games/{id}/reddit | Get a list of most recent posts from the game&#39;s subreddit.
[**games_screenshots_list**](GamesApi.md#games_screenshots_list) | **GET** /games/{game_pk}/screenshots | Get screenshots for the game.
[**games_sitemap_read**](GamesApi.md#games_sitemap_read) | **GET** /games/sitemap | Get The Sitemap Games list.
[**games_stores_list**](GamesApi.md#games_stores_list) | **GET** /games/{game_pk}/stores | Get links to the stores that sell the game.
[**games_suggested_read**](GamesApi.md#games_suggested_read) | **GET** /games/{id}/suggested | Get a list of visually similar games.
[**games_twitch_read**](GamesApi.md#games_twitch_read) | **GET** /games/{id}/twitch | Get streams on Twitch associated with the game .
[**games_youtube_read**](GamesApi.md#games_youtube_read) | **GET** /games/{id}/youtube | Get videos from YouTube associated with the game.


# **games_achievements_read**
> ParentAchievement games_achievements_read(id)

Get a list of game achievements.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get a list of game achievements.
        api_response = api_instance.games_achievements_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_achievements_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**ParentAchievement**](ParentAchievement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_additions_list**
> InlineResponse2003 games_additions_list(game_pk, page=page, page_size=page_size)

Get a list of DLC's for the game, GOTY and other editions, companion apps, etc.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of DLC's for the game, GOTY and other editions, companion apps, etc.
        api_response = api_instance.games_additions_list(game_pk, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_additions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_development_team_list**
> InlineResponse2005 games_development_team_list(game_pk, ordering=ordering, page=page, page_size=page_size)

Get a list of individual creators that were part of the development team.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of individual creators that were part of the development team.
        api_response = api_instance.games_development_team_list(game_pk, ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_development_team_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_game_series_list**
> InlineResponse2003 games_game_series_list(game_pk, page=page, page_size=page_size)

Get a list of games that are part of the same series.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of games that are part of the same series.
        api_response = api_instance.games_game_series_list(game_pk, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_game_series_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_list**
> InlineResponse2003 games_list(page=page, page_size=page_size, search=search, parent_platforms=parent_platforms, platforms=platforms, stores=stores, developers=developers, publishers=publishers, genres=genres, tags=tags, creators=creators, dates=dates, platforms_count=platforms_count, exclude_collection=exclude_collection, exclude_additions=exclude_additions, exclude_parents=exclude_parents, exclude_game_series=exclude_game_series, ordering=ordering)

Get a list of games.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
search = 'search_example' # str | Search query. (optional)
parent_platforms = 'parent_platforms_example' # str | Filter by parent platforms, for example: `1,2,3`. (optional)
platforms = 'platforms_example' # str | Filter by platforms, for example: `4,5`. (optional)
stores = 'stores_example' # str | Filter by stores, for example: `5,6`. (optional)
developers = 'developers_example' # str | Filter by developers, for example: `1612,18893` or `valve-software,feral-interactive`. (optional)
publishers = 'publishers_example' # str | Filter by publishers, for example: `354,20987` or `electronic-arts,microsoft-studios`. (optional)
genres = 'genres_example' # str | Filter by genres, for example: `4,51` or `action,indie`. (optional)
tags = 'tags_example' # str | Filter by tags, for example: `31,7` or `singleplayer,multiplayer`. (optional)
creators = 'creators_example' # str | Filter by creators, for example: `78,28` or `cris-velasco,mike-morasky`. (optional)
dates = 'dates_example' # str | Filter by a release date, for example: `2010-01-01,2018-12-31.1960-01-01,1969-12-31`. (optional)
platforms_count = 56 # int | Filter by platforms count, for example: `1`. (optional)
exclude_collection = 56 # int | Exclude games from a particular collection, for example: `123`. (optional)
exclude_additions = True # bool | Exclude additions. (optional)
exclude_parents = True # bool | Exclude games which have additions. (optional)
exclude_game_series = True # bool | Exclude games which included in a game series. (optional)
ordering = 'ordering_example' # str | Available fields: `name`, `released`, `added`, `created`, `rating`. You can reverse the sort order adding a hyphen, for example: `-released`. (optional)

    try:
        # Get a list of games.
        api_response = api_instance.games_list(page=page, page_size=page_size, search=search, parent_platforms=parent_platforms, platforms=platforms, stores=stores, developers=developers, publishers=publishers, genres=genres, tags=tags, creators=creators, dates=dates, platforms_count=platforms_count, exclude_collection=exclude_collection, exclude_additions=exclude_additions, exclude_parents=exclude_parents, exclude_game_series=exclude_game_series, ordering=ordering)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| Search query. | [optional] 
 **parent_platforms** | **str**| Filter by parent platforms, for example: &#x60;1,2,3&#x60;. | [optional] 
 **platforms** | **str**| Filter by platforms, for example: &#x60;4,5&#x60;. | [optional] 
 **stores** | **str**| Filter by stores, for example: &#x60;5,6&#x60;. | [optional] 
 **developers** | **str**| Filter by developers, for example: &#x60;1612,18893&#x60; or &#x60;valve-software,feral-interactive&#x60;. | [optional] 
 **publishers** | **str**| Filter by publishers, for example: &#x60;354,20987&#x60; or &#x60;electronic-arts,microsoft-studios&#x60;. | [optional] 
 **genres** | **str**| Filter by genres, for example: &#x60;4,51&#x60; or &#x60;action,indie&#x60;. | [optional] 
 **tags** | **str**| Filter by tags, for example: &#x60;31,7&#x60; or &#x60;singleplayer,multiplayer&#x60;. | [optional] 
 **creators** | **str**| Filter by creators, for example: &#x60;78,28&#x60; or &#x60;cris-velasco,mike-morasky&#x60;. | [optional] 
 **dates** | **str**| Filter by a release date, for example: &#x60;2010-01-01,2018-12-31.1960-01-01,1969-12-31&#x60;. | [optional] 
 **platforms_count** | **int**| Filter by platforms count, for example: &#x60;1&#x60;. | [optional] 
 **exclude_collection** | **int**| Exclude games from a particular collection, for example: &#x60;123&#x60;. | [optional] 
 **exclude_additions** | **bool**| Exclude additions. | [optional] 
 **exclude_parents** | **bool**| Exclude games which have additions. | [optional] 
 **exclude_game_series** | **bool**| Exclude games which included in a game series. | [optional] 
 **ordering** | **str**| Available fields: &#x60;name&#x60;, &#x60;released&#x60;, &#x60;added&#x60;, &#x60;created&#x60;, &#x60;rating&#x60;. You can reverse the sort order adding a hyphen, for example: &#x60;-released&#x60;. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_movies_read**
> Movie games_movies_read(id)

Get a list of game trailers.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get a list of game trailers.
        api_response = api_instance.games_movies_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_movies_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**Movie**](Movie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_parent_games_list**
> InlineResponse2003 games_parent_games_list(game_pk, page=page, page_size=page_size)

Get a list of parent games for DLC's and editions.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of parent games for DLC's and editions.
        api_response = api_instance.games_parent_games_list(game_pk, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_parent_games_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_read**
> GameSingle games_read(id)

Get details of the game.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get details of the game.
        api_response = api_instance.games_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**GameSingle**](GameSingle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_reddit_read**
> Reddit games_reddit_read(id)

Get a list of most recent posts from the game's subreddit.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get a list of most recent posts from the game's subreddit.
        api_response = api_instance.games_reddit_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_reddit_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**Reddit**](Reddit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_screenshots_list**
> InlineResponse2006 games_screenshots_list(game_pk, ordering=ordering, page=page, page_size=page_size)

Get screenshots for the game.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get screenshots for the game.
        api_response = api_instance.games_screenshots_list(game_pk, ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_screenshots_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_sitemap_read**
> InlineResponse2004 games_sitemap_read(page=page, page_size=page_size)

Get The Sitemap Games list.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get The Sitemap Games list.
        api_response = api_instance.games_sitemap_read(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_sitemap_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_stores_list**
> InlineResponse2007 games_stores_list(game_pk, ordering=ordering, page=page, page_size=page_size)

Get links to the stores that sell the game.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    game_pk = 'game_pk_example' # str | 
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get links to the stores that sell the game.
        api_response = api_instance.games_stores_list(game_pk, ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_stores_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_pk** | **str**|  | 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_suggested_read**
> GameSingle games_suggested_read(id)

Get a list of visually similar games.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get a list of visually similar games.
        api_response = api_instance.games_suggested_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_suggested_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**GameSingle**](GameSingle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_twitch_read**
> Twitch games_twitch_read(id)

Get streams on Twitch associated with the game .

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get streams on Twitch associated with the game .
        api_response = api_instance.games_twitch_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_twitch_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**Twitch**](Twitch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_youtube_read**
> Youtube games_youtube_read(id)

Get videos from YouTube associated with the game.

### Example

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
with rawg.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = rawg.GamesApi(api_client)
    id = 'id_example' # str | An ID or a slug identifying this Game.

    try:
        # Get videos from YouTube associated with the game.
        api_response = api_instance.games_youtube_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GamesApi->games_youtube_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID or a slug identifying this Game. | 

### Return type

[**Youtube**](Youtube.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

