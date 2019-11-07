# spio.PageAccessGroupsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_page_access_groups_page_access_group_id**](PageAccessGroupsApi.md#delete_pages_page_id_page_access_groups_page_access_group_id) | **DELETE** /pages/{page_id}/page_access_groups/{page_access_group_id} | Remove a page access group
[**get_pages_page_id_page_access_groups**](PageAccessGroupsApi.md#get_pages_page_id_page_access_groups) | **GET** /pages/{page_id}/page_access_groups | Get a list of page access groups
[**get_pages_page_id_page_access_groups_page_access_group_id**](PageAccessGroupsApi.md#get_pages_page_id_page_access_groups_page_access_group_id) | **GET** /pages/{page_id}/page_access_groups/{page_access_group_id} | Get a page access group
[**patch_pages_page_id_page_access_groups_page_access_group_id**](PageAccessGroupsApi.md#patch_pages_page_id_page_access_groups_page_access_group_id) | **PATCH** /pages/{page_id}/page_access_groups/{page_access_group_id} | Update a page access group
[**post_pages_page_id_page_access_groups**](PageAccessGroupsApi.md#post_pages_page_id_page_access_groups) | **POST** /pages/{page_id}/page_access_groups | Create a page access group
[**put_pages_page_id_page_access_groups_page_access_group_id**](PageAccessGroupsApi.md#put_pages_page_id_page_access_groups_page_access_group_id) | **PUT** /pages/{page_id}/page_access_groups/{page_access_group_id} | Update a page access group


# **delete_pages_page_id_page_access_groups_page_access_group_id**
> PageAccessGroup delete_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id)

Remove a page access group

Remove a page access group

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier

try:
    # Remove a page access group
    api_response = api_instance.delete_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->delete_pages_page_id_page_access_groups_page_access_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 

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
**200** | Remove a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_groups**
> list[PageAccessGroup] get_pages_page_id_page_access_groups(page_id)

Get a list of page access groups

Get a list of page access groups

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a list of page access groups
    api_response = api_instance.get_pages_page_id_page_access_groups(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->get_pages_page_id_page_access_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**list[PageAccessGroup]**](PageAccessGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of page access groups |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_groups_page_access_group_id**
> PageAccessGroup get_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id)

Get a page access group

Get a page access group

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier

try:
    # Get a page access group
    api_response = api_instance.get_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->get_pages_page_id_page_access_groups_page_access_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 

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
**200** | Get a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_page_access_groups_page_access_group_id**
> PageAccessGroup patch_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id, patch_pages_page_id_page_access_groups)

Update a page access group

Update a page access group

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
patch_pages_page_id_page_access_groups = spio.PatchPagesPageIdPageAccessGroups() # PatchPagesPageIdPageAccessGroups | 

try:
    # Update a page access group
    api_response = api_instance.patch_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id, patch_pages_page_id_page_access_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->patch_pages_page_id_page_access_groups_page_access_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **patch_pages_page_id_page_access_groups** | [**PatchPagesPageIdPageAccessGroups**](PatchPagesPageIdPageAccessGroups.md)|  | 

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
**200** | Update a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_page_access_groups**
> PageAccessGroup post_pages_page_id_page_access_groups(page_id, post_pages_page_id_page_access_groups)

Create a page access group

Create a page access group

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_page_access_groups = spio.PostPagesPageIdPageAccessGroups() # PostPagesPageIdPageAccessGroups | 

try:
    # Create a page access group
    api_response = api_instance.post_pages_page_id_page_access_groups(page_id, post_pages_page_id_page_access_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->post_pages_page_id_page_access_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_page_access_groups** | [**PostPagesPageIdPageAccessGroups**](PostPagesPageIdPageAccessGroups.md)|  | 

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
**201** | Create a page access group |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_page_access_groups_page_access_group_id**
> PageAccessGroup put_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id, put_pages_page_id_page_access_groups)

Update a page access group

Update a page access group

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
api_instance = spio.PageAccessGroupsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_group_id = 'page_access_group_id_example' # str | Page Access Group Identifier
put_pages_page_id_page_access_groups = spio.PutPagesPageIdPageAccessGroups() # PutPagesPageIdPageAccessGroups | 

try:
    # Update a page access group
    api_response = api_instance.put_pages_page_id_page_access_groups_page_access_group_id(page_id, page_access_group_id, put_pages_page_id_page_access_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessGroupsApi->put_pages_page_id_page_access_groups_page_access_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_group_id** | **str**| Page Access Group Identifier | 
 **put_pages_page_id_page_access_groups** | [**PutPagesPageIdPageAccessGroups**](PutPagesPageIdPageAccessGroups.md)|  | 

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
**200** | Update a page access group |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

