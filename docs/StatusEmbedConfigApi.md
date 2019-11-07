# spio.StatusEmbedConfigApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pages_page_id_status_embed_config**](StatusEmbedConfigApi.md#get_pages_page_id_status_embed_config) | **GET** /pages/{page_id}/status_embed_config | Get status embed config settings
[**patch_pages_page_id_status_embed_config**](StatusEmbedConfigApi.md#patch_pages_page_id_status_embed_config) | **PATCH** /pages/{page_id}/status_embed_config | Update status embed config settings
[**put_pages_page_id_status_embed_config**](StatusEmbedConfigApi.md#put_pages_page_id_status_embed_config) | **PUT** /pages/{page_id}/status_embed_config | Update status embed config settings


# **get_pages_page_id_status_embed_config**
> StatusEmbedConfig get_pages_page_id_status_embed_config(page_id)

Get status embed config settings

Get status embed config settings

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
api_instance = spio.StatusEmbedConfigApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get status embed config settings
    api_response = api_instance.get_pages_page_id_status_embed_config(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEmbedConfigApi->get_pages_page_id_status_embed_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**StatusEmbedConfig**](StatusEmbedConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status embed config settings |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_status_embed_config**
> StatusEmbedConfig patch_pages_page_id_status_embed_config(page_id, patch_pages_page_id_status_embed_config)

Update status embed config settings

Update status embed config settings

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
api_instance = spio.StatusEmbedConfigApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
patch_pages_page_id_status_embed_config = spio.PatchPagesPageIdStatusEmbedConfig() # PatchPagesPageIdStatusEmbedConfig | 

try:
    # Update status embed config settings
    api_response = api_instance.patch_pages_page_id_status_embed_config(page_id, patch_pages_page_id_status_embed_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEmbedConfigApi->patch_pages_page_id_status_embed_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **patch_pages_page_id_status_embed_config** | [**PatchPagesPageIdStatusEmbedConfig**](PatchPagesPageIdStatusEmbedConfig.md)|  | 

### Return type

[**StatusEmbedConfig**](StatusEmbedConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update status embed config settings |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_status_embed_config**
> StatusEmbedConfig put_pages_page_id_status_embed_config(page_id, put_pages_page_id_status_embed_config)

Update status embed config settings

Update status embed config settings

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
api_instance = spio.StatusEmbedConfigApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
put_pages_page_id_status_embed_config = spio.PutPagesPageIdStatusEmbedConfig() # PutPagesPageIdStatusEmbedConfig | 

try:
    # Update status embed config settings
    api_response = api_instance.put_pages_page_id_status_embed_config(page_id, put_pages_page_id_status_embed_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusEmbedConfigApi->put_pages_page_id_status_embed_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **put_pages_page_id_status_embed_config** | [**PutPagesPageIdStatusEmbedConfig**](PutPagesPageIdStatusEmbedConfig.md)|  | 

### Return type

[**StatusEmbedConfig**](StatusEmbedConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update status embed config settings |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

