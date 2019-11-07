# spio.PagesApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pages**](PagesApi.md#get_pages) | **GET** /pages | Get a list of pages
[**get_pages_page_id**](PagesApi.md#get_pages_page_id) | **GET** /pages/{page_id} | Get a page
[**patch_pages_page_id**](PagesApi.md#patch_pages_page_id) | **PATCH** /pages/{page_id} | Update a page
[**put_pages_page_id**](PagesApi.md#put_pages_page_id) | **PUT** /pages/{page_id} | Update a page


# **get_pages**
> list[Page] get_pages()

Get a list of pages

Get a list of pages

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import spio
from spio.rest import ApiException
from pprint import pprint
configuration = spio.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.statuspage.io/v1
configuration.host = "https://api.statuspage.io/v1"
# Create an instance of the API class
api_instance = spio.PagesApi(spio.ApiClient(configuration))

try:
    # Get a list of pages
    api_response = api_instance.get_pages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagesApi->get_pages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Page]**](Page.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of pages |  -  |
**401** | Could not authenticate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id**
> Page get_pages_page_id(page_id)

Get a page

Get a page

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import spio
from spio.rest import ApiException
from pprint import pprint
configuration = spio.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.statuspage.io/v1
configuration.host = "https://api.statuspage.io/v1"
# Create an instance of the API class
api_instance = spio.PagesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a page
    api_response = api_instance.get_pages_page_id(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagesApi->get_pages_page_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**Page**](Page.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a page |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id**
> Page patch_pages_page_id(page_id, patch_pages)

Update a page

Update a page

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import spio
from spio.rest import ApiException
from pprint import pprint
configuration = spio.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.statuspage.io/v1
configuration.host = "https://api.statuspage.io/v1"
# Create an instance of the API class
api_instance = spio.PagesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
patch_pages = spio.PatchPages() # PatchPages | 

try:
    # Update a page
    api_response = api_instance.patch_pages_page_id(page_id, patch_pages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagesApi->patch_pages_page_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **patch_pages** | [**PatchPages**](PatchPages.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a page |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id**
> Page put_pages_page_id(page_id, put_pages)

Update a page

Update a page

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import spio
from spio.rest import ApiException
from pprint import pprint
configuration = spio.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.statuspage.io/v1
configuration.host = "https://api.statuspage.io/v1"
# Create an instance of the API class
api_instance = spio.PagesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
put_pages = spio.PutPages() # PutPages | 

try:
    # Update a page
    api_response = api_instance.put_pages_page_id(page_id, put_pages)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PagesApi->put_pages_page_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **put_pages** | [**PutPages**](PutPages.md)|  | 

### Return type

[**Page**](Page.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a page |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

