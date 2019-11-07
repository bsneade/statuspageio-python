# spio.PageAccessGroupComponentsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_page_access_groups_page_access_group_id_components**](PageAccessGroupComponentsApi.md#delete_pages_page_id_page_access_groups_page_access_group_id_components) | **DELETE** /pages/{page_id}/page_access_groups/{page_access_group_id}/components | Delete components for a page access group
[**delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id**](PageAccessGroupComponentsApi.md#delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id) | **DELETE** /pages/{page_id}/page_access_groups/{page_access_group_id}/components/{component_id} | Remove a component from a page access group
[**get_pages_page_id_page_access_groups_page_access_group_id_components**](PageAccessGroupComponentsApi.md#get_pages_page_id_page_access_groups_page_access_group_id_components) | **GET** /pages/{page_id}/page_access_groups/{page_access_group_id}/components | List components for a page access group
[**patch_pages_page_id_page_access_groups_page_access_group_id_components**](PageAccessGroupComponentsApi.md#patch_pages_page_id_page_access_groups_page_access_group_id_components) | **PATCH** /pages/{page_id}/page_access_groups/{page_access_group_id}/components | Add components to page access group
[**post_pages_page_id_page_access_groups_page_access_group_id_components**](PageAccessGroupComponentsApi.md#post_pages_page_id_page_access_groups_page_access_group_id_components) | **POST** /pages/{page_id}/page_access_groups/{page_access_group_id}/components | Replace components for a page access group
[**put_pages_page_id_page_access_groups_page_access_group_id_components**](PageAccessGroupComponentsApi.md#put_pages_page_id_page_access_groups_page_access_group_id_components) | **PUT** /pages/{page_id}/page_access_groups/{page_access_group_id}/components | Add components to page access group


# **delete_pages_page_id_page_access_groups_page_access_group_id_components**
> PageAccessGroup delete_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, delete_pages_page_id_page_access_groups_page_access_group_id_components)

Delete components for a page access group

Delete components for a page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
delete_pages_page_id_page_access_groups_page_access_group_id_components = spio.DeletePagesPageIdPageAccessGroupsPageAccessGroupIdComponents() # DeletePagesPageIdPageAccessGroupsPageAccessGroupIdComponents | 

try:
    # Delete components for a page access group
    api_response = api_instance.delete_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, delete_pages_page_id_page_access_groups_page_access_group_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->delete_pages_page_id_page_access_groups_page_access_group_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **delete_pages_page_id_page_access_groups_page_access_group_id_components** | [**DeletePagesPageIdPageAccessGroupsPageAccessGroupIdComponents**](DeletePagesPageIdPageAccessGroupsPageAccessGroupIdComponents.md)|  | 

### Return type

[**PageAccessGroup**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete components for a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id**
> PageAccessGroup delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id(page_id, page_access_group_id, component_id)

Remove a component from a page access group

Remove a component from a page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
component_id = 'component_id_example' # str | Component identifier

try:
    # Remove a component from a page access group
    api_response = api_instance.delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id(page_id, page_access_group_id, component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->delete_pages_page_id_page_access_groups_page_access_group_id_components_component_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **component_id** | **str**| Component identifier | 

### Return type

[**PageAccessGroup**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remove a component from a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_groups_page_access_group_id_components**
> list[Component] get_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id)

List components for a page access group

List components for a page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier

try:
    # List components for a page access group
    api_response = api_instance.get_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->get_pages_page_id_page_access_groups_page_access_group_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 

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
**200** | List components for a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_page_access_groups_page_access_group_id_components**
> PageAccessGroup patch_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, patch_pages_page_id_page_access_groups_page_access_group_id_components)

Add components to page access group

Add components to page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
patch_pages_page_id_page_access_groups_page_access_group_id_components = spio.PatchPagesPageIdPageAccessGroupsPageAccessGroupIdComponents() # PatchPagesPageIdPageAccessGroupsPageAccessGroupIdComponents | 

try:
    # Add components to page access group
    api_response = api_instance.patch_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, patch_pages_page_id_page_access_groups_page_access_group_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->patch_pages_page_id_page_access_groups_page_access_group_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **patch_pages_page_id_page_access_groups_page_access_group_id_components** | [**PatchPagesPageIdPageAccessGroupsPageAccessGroupIdComponents**](PatchPagesPageIdPageAccessGroupsPageAccessGroupIdComponents.md)|  | 

### Return type

[**PageAccessGroup**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add components to page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_page_access_groups_page_access_group_id_components**
> PageAccessGroup post_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, post_pages_page_id_page_access_groups_page_access_group_id_components)

Replace components for a page access group

Replace components for a page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
post_pages_page_id_page_access_groups_page_access_group_id_components = spio.PostPagesPageIdPageAccessGroupsPageAccessGroupIdComponents() # PostPagesPageIdPageAccessGroupsPageAccessGroupIdComponents | 

try:
    # Replace components for a page access group
    api_response = api_instance.post_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, post_pages_page_id_page_access_groups_page_access_group_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->post_pages_page_id_page_access_groups_page_access_group_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **post_pages_page_id_page_access_groups_page_access_group_id_components** | [**PostPagesPageIdPageAccessGroupsPageAccessGroupIdComponents**](PostPagesPageIdPageAccessGroupsPageAccessGroupIdComponents.md)|  | 

### Return type

[**PageAccessGroup**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Replace components for a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_page_access_groups_page_access_group_id_components**
> PageAccessGroup put_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, put_pages_page_id_page_access_groups_page_access_group_id_components)

Add components to page access group

Add components to page access group

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
api_instance = spio.PageAccessGroupComponentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
put_pages_page_id_page_access_groups_page_access_group_id_components = spio.PutPagesPageIdPageAccessGroupsPageAccessGroupIdComponents() # PutPagesPageIdPageAccessGroupsPageAccessGroupIdComponents | 

try:
    # Add components to page access group
    api_response = api_instance.put_pages_page_id_page_access_groups_page_access_group_id_components(page_id, page_access_group_id, put_pages_page_id_page_access_groups_page_access_group_id_components)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupComponentsApi->put_pages_page_id_page_access_groups_page_access_group_id_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **put_pages_page_id_page_access_groups_page_access_group_id_components** | [**PutPagesPageIdPageAccessGroupsPageAccessGroupIdComponents**](PutPagesPageIdPageAccessGroupsPageAccessGroupIdComponents.md)|  | 

### Return type

[**PageAccessGroup**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add components to page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

