# spio.PageAccessUserComponentsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_page_access_users_page_access_user_id_components**](PageAccessUserComponentsApi.md#delete_pages_page_id_page_access_users_page_access_user_id_components) | **DELETE** /pages/{page_id}/page_access_users/{page_access_user_id}/components | Remove components for page access user
[**delete_pages_page_id_page_access_users_page_access_user_id_components_component_id**](PageAccessUserComponentsApi.md#delete_pages_page_id_page_access_users_page_access_user_id_components_component_id) | **DELETE** /pages/{page_id}/page_access_users/{page_access_user_id}/components/{component_id} | Remove component for page access user
[**get_pages_page_id_page_access_users_page_access_user_id_components**](PageAccessUserComponentsApi.md#get_pages_page_id_page_access_users_page_access_user_id_components) | **GET** /pages/{page_id}/page_access_users/{page_access_user_id}/components | Get components for page access user
[**patch_pages_page_id_page_access_users_page_access_user_id_components**](PageAccessUserComponentsApi.md#patch_pages_page_id_page_access_users_page_access_user_id_components) | **PATCH** /pages/{page_id}/page_access_users/{page_access_user_id}/components | Add components for page access user
[**post_pages_page_id_page_access_users_page_access_user_id_components**](PageAccessUserComponentsApi.md#post_pages_page_id_page_access_users_page_access_user_id_components) | **POST** /pages/{page_id}/page_access_users/{page_access_user_id}/components | Replace components for page access user
[**put_pages_page_id_page_access_users_page_access_user_id_components**](PageAccessUserComponentsApi.md#put_pages_page_id_page_access_users_page_access_user_id_components) | **PUT** /pages/{page_id}/page_access_users/{page_access_user_id}/components | Add components for page access user


# **delete_pages_page_id_page_access_users_page_access_user_id_components**
> delete_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, component_ids=component_ids)

Remove components for page access user

Remove components for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
component_ids = 'component_ids_example' # list[str] | List of components codes to remove.  If omitted, all components will be removed. (optional)

try:
    # Remove components for page access user
    api_instance.delete_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, component_ids=component_ids)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->delete_pages_page_id_page_access_users_page_access_user_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **component_ids** | [**list[str]**](str.md)| List of components codes to remove.  If omitted, all components will be removed. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Remove components for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_page_access_users_page_access_user_id_components_component_id**
> PageAccessUser delete_pages_page_id_page_access_users_page_access_user_id_components_component_id(page_id, page_access_user_id, component_id)

Remove component for page access user

Remove component for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
component_id = 'component_id_example' # str | Component identifier

try:
    # Remove component for page access user
    api_response = api_instance.delete_pages_page_id_page_access_users_page_access_user_id_components_component_id(page_id, page_access_user_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->delete_pages_page_id_page_access_users_page_access_user_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **component_id** | **str**| Component identifier | 

### Return type

[**PageAccessUser**](PageAccessUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remove component for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_users_page_access_user_id_components**
> get_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id)

Get components for page access user

Get components for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Get components for page access user
    api_instance.get_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->get_pages_page_id_page_access_users_page_access_user_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get components for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_page_access_users_page_access_user_id_components**
> patch_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)

Add components for page access user

Add components for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
unknown_base_type = spio.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Add components for page access user
    api_instance.patch_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->patch_pages_page_id_page_access_users_page_access_user_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add components for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_page_access_users_page_access_user_id_components**
> post_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)

Replace components for page access user

Replace components for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
unknown_base_type = spio.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Replace components for page access user
    api_instance.post_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->post_pages_page_id_page_access_users_page_access_user_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Replace components for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_page_access_users_page_access_user_id_components**
> put_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)

Add components for page access user

Add components for page access user

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
api_instance = spio.PageAccessUserComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
unknown_base_type = spio.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE |  (optional)

try:
    # Add components for page access user
    api_instance.put_pages_page_id_page_access_users_page_access_user_id_components(page_id, page_access_user_id, unknown_base_type=unknown_base_type)
except ApiException as e:
    print("Exception when calling PageAccessUserComponentsApi->put_pages_page_id_page_access_users_page_access_user_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add components for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

