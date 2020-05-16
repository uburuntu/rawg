# rawg.PlatformsApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**platforms_list**](PlatformsApi.md#platforms_list) | **GET** /platforms | Get a list of video game platforms.
[**platforms_lists_parents_list**](PlatformsApi.md#platforms_lists_parents_list) | **GET** /platforms/lists/parents | Get a list of parent platforms.
[**platforms_read**](PlatformsApi.md#platforms_read) | **GET** /platforms/{id} | Get details of the platform.


# **platforms_list**
> InlineResponse2009 platforms_list(ordering=ordering, page=page, page_size=page_size)

Get a list of video game platforms.

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
    api_instance = rawg.PlatformsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of video game platforms.
        api_response = api_instance.platforms_list(ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlatformsApi->platforms_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

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

# **platforms_lists_parents_list**
> InlineResponse20010 platforms_lists_parents_list(ordering=ordering, page=page, page_size=page_size)

Get a list of parent platforms.

For instance, for PS2 and PS4 the “parent platform” is PlayStation.

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
    api_instance = rawg.PlatformsApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of parent platforms.
        api_response = api_instance.platforms_lists_parents_list(ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlatformsApi->platforms_lists_parents_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **platforms_read**
> PlatformSingle platforms_read(id)

Get details of the platform.

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
    api_instance = rawg.PlatformsApi(api_client)
    id = 56 # int | A unique integer value identifying this Platform.

    try:
        # Get details of the platform.
        api_response = api_instance.platforms_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlatformsApi->platforms_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Platform. | 

### Return type

[**PlatformSingle**](PlatformSingle.md)

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

