# spio.ComponentsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_components_component_id**](ComponentsApi.md#delete_pages_page_id_components_component_id) | **DELETE** /pages/{page_id}/components/{component_id} | Delete a component
[**delete_pages_page_id_components_component_id_page_access_groups**](ComponentsApi.md#delete_pages_page_id_components_component_id_page_access_groups) | **DELETE** /pages/{page_id}/components/{component_id}/page_access_groups | Remove page access groups from a component
[**delete_pages_page_id_components_component_id_page_access_users**](ComponentsApi.md#delete_pages_page_id_components_component_id_page_access_users) | **DELETE** /pages/{page_id}/components/{component_id}/page_access_users | Remove page access users from component
[**get_pages_page_id_components**](ComponentsApi.md#get_pages_page_id_components) | **GET** /pages/{page_id}/components | Get a list of components
[**get_pages_page_id_components_component_id**](ComponentsApi.md#get_pages_page_id_components_component_id) | **GET** /pages/{page_id}/components/{component_id} | Get a component
[**patch_pages_page_id_components_component_id**](ComponentsApi.md#patch_pages_page_id_components_component_id) | **PATCH** /pages/{page_id}/components/{component_id} | Update a component
[**post_pages_page_id_components**](ComponentsApi.md#post_pages_page_id_components) | **POST** /pages/{page_id}/components | Create a component
[**post_pages_page_id_components_component_id_page_access_groups**](ComponentsApi.md#post_pages_page_id_components_component_id_page_access_groups) | **POST** /pages/{page_id}/components/{component_id}/page_access_groups | Add page access groups to a component
[**post_pages_page_id_components_component_id_page_access_users**](ComponentsApi.md#post_pages_page_id_components_component_id_page_access_users) | **POST** /pages/{page_id}/components/{component_id}/page_access_users | Add page access users to a component
[**put_pages_page_id_components_component_id**](ComponentsApi.md#put_pages_page_id_components_component_id) | **PUT** /pages/{page_id}/components/{component_id} | Update a component


# **delete_pages_page_id_components_component_id**
> delete_pages_page_id_components_component_id(page_id, component_id)

Delete a component

Delete a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier

try:
    # Delete a component
    api_instance.delete_pages_page_id_components_component_id(page_id, component_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_pages_page_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 

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
**204** | Delete a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_components_component_id_page_access_groups**
> Component delete_pages_page_id_components_component_id_page_access_groups(page_id, component_id)

Remove page access groups from a component

Remove page access groups from a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier

try:
    # Remove page access groups from a component
    api_response = api_instance.delete_pages_page_id_components_component_id_page_access_groups(page_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_pages_page_id_components_component_id_page_access_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remove page access groups from a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_components_component_id_page_access_users**
> Component delete_pages_page_id_components_component_id_page_access_users(page_id, component_id)

Remove page access users from component

Remove page access users from component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier

try:
    # Remove page access users from component
    api_response = api_instance.delete_pages_page_id_components_component_id_page_access_users(page_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_pages_page_id_components_component_id_page_access_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remove page access users from component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_components**
> list[Component] get_pages_page_id_components(page_id, page=page, per_page=per_page)

Get a list of components

Get a list of components

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 56 # int | Page offset to fetch. (optional)
per_page = 56 # int | Number of results to return per page. (optional)

try:
    # Get a list of components
    api_response = api_instance.get_pages_page_id_components(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_pages_page_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] 
 **per_page** | **int**| Number of results to return per page. | [optional] 

### Return type

[**list[Component]**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of components |  -  |
**401** | Could not authenticate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_components_component_id**
> Component get_pages_page_id_components_component_id(page_id, component_id)

Get a component

Get a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier

try:
    # Get a component
    api_response = api_instance.get_pages_page_id_components_component_id(page_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_pages_page_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_components_component_id**
> Component patch_pages_page_id_components_component_id(page_id, component_id, patch_pages_page_id_components)

Update a component

Update a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier
patch_pages_page_id_components = spio.PatchPagesPageIdComponents() # PatchPagesPageIdComponents | 

try:
    # Update a component
    api_response = api_instance.patch_pages_page_id_components_component_id(page_id, component_id, patch_pages_page_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->patch_pages_page_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 
 **patch_pages_page_id_components** | [**PatchPagesPageIdComponents**](PatchPagesPageIdComponents.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_components**
> Component post_pages_page_id_components(page_id, post_pages_page_id_components)

Create a component

Create a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_components = spio.PostPagesPageIdComponents() # PostPagesPageIdComponents | 

try:
    # Create a component
    api_response = api_instance.post_pages_page_id_components(page_id, post_pages_page_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->post_pages_page_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_components** | [**PostPagesPageIdComponents**](PostPagesPageIdComponents.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a component |  -  |
**401** | Could not authenticate |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_components_component_id_page_access_groups**
> Component post_pages_page_id_components_component_id_page_access_groups(page_id, component_id)

Add page access groups to a component

Add page access groups to a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier

try:
    # Add page access groups to a component
    api_response = api_instance.post_pages_page_id_components_component_id_page_access_groups(page_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->post_pages_page_id_components_component_id_page_access_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add page access groups to a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_components_component_id_page_access_users**
> Component post_pages_page_id_components_component_id_page_access_users(page_id, component_id, page_access_user_ids)

Add page access users to a component

Add page access users to a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier
page_access_user_ids = 'page_access_user_ids_example' # list[str] | List of page access users to add to compponent

try:
    # Add page access users to a component
    api_response = api_instance.post_pages_page_id_components_component_id_page_access_users(page_id, component_id, page_access_user_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->post_pages_page_id_components_component_id_page_access_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 
 **page_access_user_ids** | [**list[str]**](str.md)| List of page access users to add to compponent | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add page access users to a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_components_component_id**
> Component put_pages_page_id_components_component_id(page_id, component_id, put_pages_page_id_components)

Update a component

Update a component

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
api_instance = spio.ComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
component_id = 'component_id_example' # str | Component Identifier
put_pages_page_id_components = spio.PutPagesPageIdComponents() # PutPagesPageIdComponents | 

try:
    # Update a component
    api_response = api_instance.put_pages_page_id_components_component_id(page_id, component_id, put_pages_page_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->put_pages_page_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **component_id** | **str**| Component Identifier | 
 **put_pages_page_id_components** | [**PutPagesPageIdComponents**](PutPagesPageIdComponents.md)|  | 

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a component |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

