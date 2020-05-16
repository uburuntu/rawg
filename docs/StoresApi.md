# rawg.StoresApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stores_list**](StoresApi.md#stores_list) | **GET** /stores | Get a list of video game storefronts.
[**stores_read**](StoresApi.md#stores_read) | **GET** /stores/{id} | Get details of the store.


# **stores_list**
> InlineResponse20012 stores_list(ordering=ordering, page=page, page_size=page_size)

Get a list of video game storefronts.

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
    api_instance = rawg.StoresApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # Get a list of video game storefronts.
        api_response = api_instance.stores_list(ordering=ordering, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoresApi->stores_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

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

# **stores_read**
> StoreSingle stores_read(id)

Get details of the store.

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
    api_instance = rawg.StoresApi(api_client)
    id = 56 # int | A unique integer value identifying this Store.

    try:
        # Get details of the store.
        api_response = api_instance.stores_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StoresApi->stores_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Store. | 

### Return type

[**StoreSingle**](StoreSingle.md)

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

