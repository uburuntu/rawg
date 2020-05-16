# rawg.GenresApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genres_list**](GenresApi.md#genres_list) | **GET** /genres | Get a list of video game genres.
[**genres_read**](GenresApi.md#genres_read) | **GET** /genres/{id} | Get details of the genre.


# **genres_list**
> InlineResponse2008 genres_list(ordering=ordering, page=page, page_size=page_size)

Get a list of video game genres.

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
    api_instance = rawg.GenresApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of video game genres.
        api_response = api_instance.genres_list(ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenresApi->genres_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

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

# **genres_read**
> GenreSingle genres_read(id)

Get details of the genre.

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
    api_instance = rawg.GenresApi(api_client)
    id = 56 # int | A unique integer value identifying this Genre.

    try:
        # Get details of the genre.
        api_response = api_instance.genres_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GenresApi->genres_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Genre. | 

### Return type

[**GenreSingle**](GenreSingle.md)

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

