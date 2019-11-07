# spio.PageAccessUsersApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_page_access_users_page_access_user_id**](PageAccessUsersApi.md#delete_pages_page_id_page_access_users_page_access_user_id) | **DELETE** /pages/{page_id}/page_access_users/{page_access_user_id} | Delete page access user
[**get_pages_page_id_page_access_users**](PageAccessUsersApi.md#get_pages_page_id_page_access_users) | **GET** /pages/{page_id}/page_access_users | Get a list of page access users
[**get_pages_page_id_page_access_users_page_access_user_id**](PageAccessUsersApi.md#get_pages_page_id_page_access_users_page_access_user_id) | **GET** /pages/{page_id}/page_access_users/{page_access_user_id} | Get page access user
[**patch_pages_page_id_page_access_users_page_access_user_id**](PageAccessUsersApi.md#patch_pages_page_id_page_access_users_page_access_user_id) | **PATCH** /pages/{page_id}/page_access_users/{page_access_user_id} | Update page access user
[**post_pages_page_id_page_access_users**](PageAccessUsersApi.md#post_pages_page_id_page_access_users) | **POST** /pages/{page_id}/page_access_users | Add a page access user
[**put_pages_page_id_page_access_users_page_access_user_id**](PageAccessUsersApi.md#put_pages_page_id_page_access_users_page_access_user_id) | **PUT** /pages/{page_id}/page_access_users/{page_access_user_id} | Update page access user


# **delete_pages_page_id_page_access_users_page_access_user_id**
> delete_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)

Delete page access user

Delete page access user

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Delete page access user
    api_instance.delete_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->delete_pages_page_id_page_access_users_page_access_user_id: %s\n" % e)
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
**204** | Delete page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_users**
> list[PageAccessUser] get_pages_page_id_page_access_users(page_id, email=email)

Get a list of page access users

Get a list of page access users

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
email = 'email_example' # str | Email address to search for (optional)

try:
    # Get a list of page access users
    api_response = api_instance.get_pages_page_id_page_access_users(page_id, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->get_pages_page_id_page_access_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **email** | **str**| Email address to search for | [optional] 

### Return type

[**list[PageAccessUser]**](PageAccessUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of page access users |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_users_page_access_user_id**
> PageAccessUser get_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)

Get page access user

Get page access user

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Get page access user
    api_response = api_instance.get_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->get_pages_page_id_page_access_users_page_access_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 

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
**200** | Get page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_page_access_users_page_access_user_id**
> PageAccessUser patch_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)

Update page access user

Update page access user

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Update page access user
    api_response = api_instance.patch_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->patch_pages_page_id_page_access_users_page_access_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 

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
**200** | Update page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_page_access_users**
> PageAccessUser post_pages_page_id_page_access_users(page_id, post_pages_page_id_page_access_users)

Add a page access user

Add a page access user

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_page_access_users = spio.PostPagesPageIdPageAccessUsers() # PostPagesPageIdPageAccessUsers | 

try:
    # Add a page access user
    api_response = api_instance.post_pages_page_id_page_access_users(page_id, post_pages_page_id_page_access_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->post_pages_page_id_page_access_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_page_access_users** | [**PostPagesPageIdPageAccessUsers**](PostPagesPageIdPageAccessUsers.md)|  | 

### Return type

[**PageAccessUser**](PageAccessUser.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add a page access user |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**409** | The request could not be processed due to a conflict in resource state. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_page_access_users_page_access_user_id**
> PageAccessUser put_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)

Update page access user

Update page access user

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
api_instance = spio.PageAccessUsersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Update page access user
    api_response = api_instance.put_pages_page_id_page_access_users_page_access_user_id(page_id, page_access_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PageAccessUsersApi->put_pages_page_id_page_access_users_page_access_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 

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
**200** | Update page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

