# spio.ComponentGroupsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_component_groups_id**](ComponentGroupsApi.md#delete_pages_page_id_component_groups_id) | **DELETE** /pages/{page_id}/component-groups/{id} | Delete a component group
[**get_pages_page_id_component_groups**](ComponentGroupsApi.md#get_pages_page_id_component_groups) | **GET** /pages/{page_id}/component-groups | Get a list of component groups
[**get_pages_page_id_component_groups_id**](ComponentGroupsApi.md#get_pages_page_id_component_groups_id) | **GET** /pages/{page_id}/component-groups/{id} | Get a component group
[**patch_pages_page_id_component_groups_id**](ComponentGroupsApi.md#patch_pages_page_id_component_groups_id) | **PATCH** /pages/{page_id}/component-groups/{id} | Update a component group
[**post_pages_page_id_component_groups**](ComponentGroupsApi.md#post_pages_page_id_component_groups) | **POST** /pages/{page_id}/component-groups | Create a component group
[**put_pages_page_id_component_groups_id**](ComponentGroupsApi.md#put_pages_page_id_component_groups_id) | **PUT** /pages/{page_id}/component-groups/{id} | Update a component group


# **delete_pages_page_id_component_groups_id**
> GroupComponent delete_pages_page_id_component_groups_id(page_id, id)

Delete a component group

Delete a component group

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
id = 56 # int | 

try:
    # Delete a component group
    api_response = api_instance.delete_pages_page_id_component_groups_id(page_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->delete_pages_page_id_component_groups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **id** | **int**|  | 

### Return type

[**GroupComponent**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a component group |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_component_groups**
> list[GroupComponent] get_pages_page_id_component_groups(page_id)

Get a list of component groups

Get a list of component groups

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a list of component groups
    api_response = api_instance.get_pages_page_id_component_groups(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->get_pages_page_id_component_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**list[GroupComponent]**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of component groups |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_component_groups_id**
> GroupComponent get_pages_page_id_component_groups_id(page_id, id)

Get a component group

Get a component group

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
id = 56 # int | 

try:
    # Get a component group
    api_response = api_instance.get_pages_page_id_component_groups_id(page_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->get_pages_page_id_component_groups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **id** | **int**|  | 

### Return type

[**GroupComponent**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a component group |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_component_groups_id**
> GroupComponent patch_pages_page_id_component_groups_id(page_id, id, patch_pages_page_id_component_groups)

Update a component group

Update a component group

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
id = 56 # int | 
patch_pages_page_id_component_groups = spio.PatchPagesPageIdComponentGroups() # PatchPagesPageIdComponentGroups | 

try:
    # Update a component group
    api_response = api_instance.patch_pages_page_id_component_groups_id(page_id, id, patch_pages_page_id_component_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->patch_pages_page_id_component_groups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **id** | **int**|  | 
 **patch_pages_page_id_component_groups** | [**PatchPagesPageIdComponentGroups**](PatchPagesPageIdComponentGroups.md)|  | 

### Return type

[**GroupComponent**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a component group |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_component_groups**
> GroupComponent post_pages_page_id_component_groups(page_id, post_pages_page_id_component_groups)

Create a component group

Create a component group

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_component_groups = spio.PostPagesPageIdComponentGroups() # PostPagesPageIdComponentGroups | 

try:
    # Create a component group
    api_response = api_instance.post_pages_page_id_component_groups(page_id, post_pages_page_id_component_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->post_pages_page_id_component_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_component_groups** | [**PostPagesPageIdComponentGroups**](PostPagesPageIdComponentGroups.md)|  | 

### Return type

[**GroupComponent**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a component group |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_component_groups_id**
> GroupComponent put_pages_page_id_component_groups_id(page_id, id, put_pages_page_id_component_groups)

Update a component group

Update a component group

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
api_instance = spio.ComponentGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
id = 56 # int | 
put_pages_page_id_component_groups = spio.PutPagesPageIdComponentGroups() # PutPagesPageIdComponentGroups | 

try:
    # Update a component group
    api_response = api_instance.put_pages_page_id_component_groups_id(page_id, id, put_pages_page_id_component_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentGroupsApi->put_pages_page_id_component_groups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **id** | **int**|  | 
 **put_pages_page_id_component_groups** | [**PutPagesPageIdComponentGroups**](PutPagesPageIdComponentGroups.md)|  | 

### Return type

[**GroupComponent**](GroupComponent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a component group |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

