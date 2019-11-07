# spio.MetricProvidersApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_metrics_providers_metrics_provider_id**](MetricProvidersApi.md#delete_pages_page_id_metrics_providers_metrics_provider_id) | **DELETE** /pages/{page_id}/metrics_providers/{metrics_provider_id} | Delete a metric provider
[**get_pages_page_id_metrics_providers**](MetricProvidersApi.md#get_pages_page_id_metrics_providers) | **GET** /pages/{page_id}/metrics_providers | Get a list of metric providers
[**get_pages_page_id_metrics_providers_metrics_provider_id**](MetricProvidersApi.md#get_pages_page_id_metrics_providers_metrics_provider_id) | **GET** /pages/{page_id}/metrics_providers/{metrics_provider_id} | Get a metric provider
[**get_pages_page_id_metrics_providers_metrics_provider_id_metrics**](MetricProvidersApi.md#get_pages_page_id_metrics_providers_metrics_provider_id_metrics) | **GET** /pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics | List metrics for a metric provider
[**patch_pages_page_id_metrics_providers_metrics_provider_id**](MetricProvidersApi.md#patch_pages_page_id_metrics_providers_metrics_provider_id) | **PATCH** /pages/{page_id}/metrics_providers/{metrics_provider_id} | Update a metric provider
[**post_pages_page_id_metrics_providers**](MetricProvidersApi.md#post_pages_page_id_metrics_providers) | **POST** /pages/{page_id}/metrics_providers | Create a metric provider
[**post_pages_page_id_metrics_providers_metrics_provider_id_metrics**](MetricProvidersApi.md#post_pages_page_id_metrics_providers_metrics_provider_id_metrics) | **POST** /pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics | Create a metric for a metric provider
[**put_pages_page_id_metrics_providers_metrics_provider_id**](MetricProvidersApi.md#put_pages_page_id_metrics_providers_metrics_provider_id) | **PUT** /pages/{page_id}/metrics_providers/{metrics_provider_id} | Update a metric provider


# **delete_pages_page_id_metrics_providers_metrics_provider_id**
> MetricsProvider delete_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id)

Delete a metric provider

Delete a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier

try:
    # Delete a metric provider
    api_response = api_instance.delete_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->delete_pages_page_id_metrics_providers_metrics_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 

### Return type

[**MetricsProvider**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a metric provider |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_metrics_providers**
> list[MetricsProvider] get_pages_page_id_metrics_providers(page_id)

Get a list of metric providers

Get a list of metric providers

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a list of metric providers
    api_response = api_instance.get_pages_page_id_metrics_providers(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->get_pages_page_id_metrics_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**list[MetricsProvider]**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of metric providers |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_metrics_providers_metrics_provider_id**
> MetricsProvider get_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id)

Get a metric provider

Get a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier

try:
    # Get a metric provider
    api_response = api_instance.get_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->get_pages_page_id_metrics_providers_metrics_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 

### Return type

[**MetricsProvider**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a metric provider |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_metrics_providers_metrics_provider_id_metrics**
> Metric get_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id)

List metrics for a metric provider

List metrics for a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier

try:
    # List metrics for a metric provider
    api_response = api_instance.get_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->get_pages_page_id_metrics_providers_metrics_provider_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 

### Return type

[**Metric**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List metrics for a metric provider |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_metrics_providers_metrics_provider_id**
> MetricsProvider patch_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id, patch_pages_page_id_metrics_providers)

Update a metric provider

Update a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier
patch_pages_page_id_metrics_providers = spio.PatchPagesPageIdMetricsProviders() # PatchPagesPageIdMetricsProviders | 

try:
    # Update a metric provider
    api_response = api_instance.patch_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id, patch_pages_page_id_metrics_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->patch_pages_page_id_metrics_providers_metrics_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 
 **patch_pages_page_id_metrics_providers** | [**PatchPagesPageIdMetricsProviders**](PatchPagesPageIdMetricsProviders.md)|  | 

### Return type

[**MetricsProvider**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a metric provider |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_metrics_providers**
> MetricsProvider post_pages_page_id_metrics_providers(page_id, post_pages_page_id_metrics_providers)

Create a metric provider

Create a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_metrics_providers = spio.PostPagesPageIdMetricsProviders() # PostPagesPageIdMetricsProviders | 

try:
    # Create a metric provider
    api_response = api_instance.post_pages_page_id_metrics_providers(page_id, post_pages_page_id_metrics_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->post_pages_page_id_metrics_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_metrics_providers** | [**PostPagesPageIdMetricsProviders**](PostPagesPageIdMetricsProviders.md)|  | 

### Return type

[**MetricsProvider**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a metric provider |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_metrics_providers_metrics_provider_id_metrics**
> Metric post_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id, post_pages_page_id_metrics_providers_metrics_provider_id_metrics)

Create a metric for a metric provider

Create a metric for a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier
post_pages_page_id_metrics_providers_metrics_provider_id_metrics = spio.PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics() # PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics | 

try:
    # Create a metric for a metric provider
    api_response = api_instance.post_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id, post_pages_page_id_metrics_providers_metrics_provider_id_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->post_pages_page_id_metrics_providers_metrics_provider_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 
 **post_pages_page_id_metrics_providers_metrics_provider_id_metrics** | [**PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics**](PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics.md)|  | 

### Return type

[**Metric**](Metric.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a metric for a metric provider |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_metrics_providers_metrics_provider_id**
> MetricsProvider put_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id, put_pages_page_id_metrics_providers)

Update a metric provider

Update a metric provider

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
api_instance = spio.MetricProvidersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier
put_pages_page_id_metrics_providers = spio.PutPagesPageIdMetricsProviders() # PutPagesPageIdMetricsProviders | 

try:
    # Update a metric provider
    api_response = api_instance.put_pages_page_id_metrics_providers_metrics_provider_id(page_id, metrics_provider_id, put_pages_page_id_metrics_providers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricProvidersApi->put_pages_page_id_metrics_providers_metrics_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metrics_provider_id** | **str**| Metric Provider Identifier | 
 **put_pages_page_id_metrics_providers** | [**PutPagesPageIdMetricsProviders**](PutPagesPageIdMetricsProviders.md)|  | 

### Return type

[**MetricsProvider**](MetricsProvider.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a metric provider |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

