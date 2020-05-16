# rawg.DevelopersApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developers_list**](DevelopersApi.md#developers_list) | **GET** /developers | Get a list of game developers.
[**developers_read**](DevelopersApi.md#developers_read) | **GET** /developers/{id} | Get details of the developer.


# **developers_list**
> InlineResponse2002 developers_list(page=page, page_size=page_size)

Get a list of game developers.

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
    api_instance = rawg.DevelopersApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of game developers.
        api_response = api_instance.developers_list(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevelopersApi->developers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **developers_read**
> DeveloperSingle developers_read(id)

Get details of the developer.

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
    api_instance = rawg.DevelopersApi(api_client)
    id = 56 # int | A unique integer value identifying this Developer.

    try:
        # Get details of the developer.
        api_response = api_instance.developers_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevelopersApi->developers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Developer. | 

### Return type

[**DeveloperSingle**](DeveloperSingle.md)

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

