# spio.UsersApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_organizations_organization_id_users_user_id**](UsersApi.md#delete_organizations_organization_id_users_user_id) | **DELETE** /organizations/{organization_id}/users/{user_id} | Delete a user
[**get_organizations_organization_id_users**](UsersApi.md#get_organizations_organization_id_users) | **GET** /organizations/{organization_id}/users | Get a list of users
[**post_organizations_organization_id_users**](UsersApi.md#post_organizations_organization_id_users) | **POST** /organizations/{organization_id}/users | Create a user


# **delete_organizations_organization_id_users_user_id**
> User delete_organizations_organization_id_users_user_id(organization_id, user_id)

Delete a user

Delete a user

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
api_instance = spio.UsersApi(spio.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization Identifier
user_id = 'user_id_example' # str | User Identifier

try:
    # Delete a user
    api_response = api_instance.delete_organizations_organization_id_users_user_id(organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_organizations_organization_id_users_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization Identifier | 
 **user_id** | **str**| User Identifier | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_organization_id_users**
> list[User] get_organizations_organization_id_users(organization_id)

Get a list of users

Get a list of users

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
api_instance = spio.UsersApi(spio.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization Identifier

try:
    # Get a list of users
    api_response = api_instance.get_organizations_organization_id_users(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_organizations_organization_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization Identifier | 

### Return type

[**list[User]**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of users |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_organization_id_users**
> User post_organizations_organization_id_users(organization_id, post_organizations_organization_id_users)

Create a user

Create a user

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
api_instance = spio.UsersApi(spio.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization Identifier
post_organizations_organization_id_users = spio.PostOrganizationsOrganizationIdUsers() # PostOrganizationsOrganizationIdUsers | 

try:
    # Create a user
    api_response = api_instance.post_organizations_organization_id_users(organization_id, post_organizations_organization_id_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->post_organizations_organization_id_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization Identifier | 
 **post_organizations_organization_id_users** | [**PostOrganizationsOrganizationIdUsers**](PostOrganizationsOrganizationIdUsers.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a user |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

