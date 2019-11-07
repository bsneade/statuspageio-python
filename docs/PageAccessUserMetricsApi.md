# spio.PageAccessUserMetricsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_page_access_users_page_access_user_id_metrics**](PageAccessUserMetricsApi.md#delete_pages_page_id_page_access_users_page_access_user_id_metrics) | **DELETE** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics | Delete metrics for page access user
[**delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id**](PageAccessUserMetricsApi.md#delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id) | **DELETE** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics/{metric_id} | Delete metric for page access user
[**get_pages_page_id_page_access_users_page_access_user_id_metrics**](PageAccessUserMetricsApi.md#get_pages_page_id_page_access_users_page_access_user_id_metrics) | **GET** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics | Get metrics for page access user
[**patch_pages_page_id_page_access_users_page_access_user_id_metrics**](PageAccessUserMetricsApi.md#patch_pages_page_id_page_access_users_page_access_user_id_metrics) | **PATCH** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics | Add metrics for page access user
[**post_pages_page_id_page_access_users_page_access_user_id_metrics**](PageAccessUserMetricsApi.md#post_pages_page_id_page_access_users_page_access_user_id_metrics) | **POST** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics | Replace metrics for page access user
[**put_pages_page_id_page_access_users_page_access_user_id_metrics**](PageAccessUserMetricsApi.md#put_pages_page_id_page_access_users_page_access_user_id_metrics) | **PUT** /pages/{page_id}/page_access_users/{page_access_user_id}/metrics | Add metrics for page access user


# **delete_pages_page_id_page_access_users_page_access_user_id_metrics**
> delete_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, delete_pages_page_id_page_access_users_page_access_user_id_metrics)

Delete metrics for page access user

Delete metrics for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
delete_pages_page_id_page_access_users_page_access_user_id_metrics = spio.DeletePagesPageIdPageAccessUsersPageAccessUserIdMetrics() # DeletePagesPageIdPageAccessUsersPageAccessUserIdMetrics | 

try:
    # Delete metrics for page access user
    api_instance.delete_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, delete_pages_page_id_page_access_users_page_access_user_id_metrics)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->delete_pages_page_id_page_access_users_page_access_user_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **delete_pages_page_id_page_access_users_page_access_user_id_metrics** | [**DeletePagesPageIdPageAccessUsersPageAccessUserIdMetrics**](DeletePagesPageIdPageAccessUsersPageAccessUserIdMetrics.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete metrics for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id**
> delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id(page_id, page_access_user_id, metric_id)

Delete metric for page access user

Delete metric for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
metric_id = 'metric_id_example' # str | Identifier of metric requested

try:
    # Delete metric for page access user
    api_instance.delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id(page_id, page_access_user_id, metric_id)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->delete_pages_page_id_page_access_users_page_access_user_id_metrics_metric_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **metric_id** | **str**| Identifier of metric requested | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Delete metric for page access user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_page_access_users_page_access_user_id_metrics**
> get_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id)

Get metrics for page access user

Get metrics for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier

try:
    # Get metrics for page access user
    api_instance.get_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->get_pages_page_id_page_access_users_page_access_user_id_metrics: %s\n" % e)
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
**200** | Get metrics for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_page_access_users_page_access_user_id_metrics**
> patch_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, patch_pages_page_id_page_access_users_page_access_user_id_metrics)

Add metrics for page access user

Add metrics for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
patch_pages_page_id_page_access_users_page_access_user_id_metrics = spio.PatchPagesPageIdPageAccessUsersPageAccessUserIdMetrics() # PatchPagesPageIdPageAccessUsersPageAccessUserIdMetrics | 

try:
    # Add metrics for page access user
    api_instance.patch_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, patch_pages_page_id_page_access_users_page_access_user_id_metrics)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->patch_pages_page_id_page_access_users_page_access_user_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **patch_pages_page_id_page_access_users_page_access_user_id_metrics** | [**PatchPagesPageIdPageAccessUsersPageAccessUserIdMetrics**](PatchPagesPageIdPageAccessUsersPageAccessUserIdMetrics.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add metrics for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_page_access_users_page_access_user_id_metrics**
> post_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, post_pages_page_id_page_access_users_page_access_user_id_metrics)

Replace metrics for page access user

Replace metrics for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
post_pages_page_id_page_access_users_page_access_user_id_metrics = spio.PostPagesPageIdPageAccessUsersPageAccessUserIdMetrics() # PostPagesPageIdPageAccessUsersPageAccessUserIdMetrics | 

try:
    # Replace metrics for page access user
    api_instance.post_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, post_pages_page_id_page_access_users_page_access_user_id_metrics)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->post_pages_page_id_page_access_users_page_access_user_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **post_pages_page_id_page_access_users_page_access_user_id_metrics** | [**PostPagesPageIdPageAccessUsersPageAccessUserIdMetrics**](PostPagesPageIdPageAccessUsersPageAccessUserIdMetrics.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Replace metrics for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_page_access_users_page_access_user_id_metrics**
> put_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, put_pages_page_id_page_access_users_page_access_user_id_metrics)

Add metrics for page access user

Add metrics for page access user

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
api_instance = spio.PageAccessUserMetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page_access_user_id = 'page_access_user_id_example' # str | Page Access User Identifier
put_pages_page_id_page_access_users_page_access_user_id_metrics = spio.PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics() # PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics | 

try:
    # Add metrics for page access user
    api_instance.put_pages_page_id_page_access_users_page_access_user_id_metrics(page_id, page_access_user_id, put_pages_page_id_page_access_users_page_access_user_id_metrics)
except ApiException as e:
    print("Exception when calling PageAccessUserMetricsApi->put_pages_page_id_page_access_users_page_access_user_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page_access_user_id** | **str**| Page Access User Identifier | 
 **put_pages_page_id_page_access_users_page_access_user_id_metrics** | [**PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics**](PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add metrics for page access user |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

