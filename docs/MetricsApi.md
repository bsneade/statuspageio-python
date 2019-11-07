# spio.MetricsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_metrics_metric_id**](MetricsApi.md#delete_pages_page_id_metrics_metric_id) | **DELETE** /pages/{page_id}/metrics/{metric_id} | Delete a metric
[**delete_pages_page_id_metrics_metric_id_data**](MetricsApi.md#delete_pages_page_id_metrics_metric_id_data) | **DELETE** /pages/{page_id}/metrics/{metric_id}/data | Reset data for a metric
[**get_pages_page_id_metrics**](MetricsApi.md#get_pages_page_id_metrics) | **GET** /pages/{page_id}/metrics | Get a list of metrics
[**get_pages_page_id_metrics_metric_id**](MetricsApi.md#get_pages_page_id_metrics_metric_id) | **GET** /pages/{page_id}/metrics/{metric_id} | Get a metric
[**get_pages_page_id_metrics_providers_metrics_provider_id_metrics**](MetricsApi.md#get_pages_page_id_metrics_providers_metrics_provider_id_metrics) | **GET** /pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics | List metrics for a metric provider
[**patch_pages_page_id_metrics_metric_id**](MetricsApi.md#patch_pages_page_id_metrics_metric_id) | **PATCH** /pages/{page_id}/metrics/{metric_id} | Update a metric
[**post_pages_page_id_metrics_data**](MetricsApi.md#post_pages_page_id_metrics_data) | **POST** /pages/{page_id}/metrics/data | Add data points to metrics
[**post_pages_page_id_metrics_metric_id_data**](MetricsApi.md#post_pages_page_id_metrics_metric_id_data) | **POST** /pages/{page_id}/metrics/{metric_id}/data | Add data to a metric
[**post_pages_page_id_metrics_providers_metrics_provider_id_metrics**](MetricsApi.md#post_pages_page_id_metrics_providers_metrics_provider_id_metrics) | **POST** /pages/{page_id}/metrics_providers/{metrics_provider_id}/metrics | Create a metric for a metric provider
[**put_pages_page_id_metrics_metric_id**](MetricsApi.md#put_pages_page_id_metrics_metric_id) | **PUT** /pages/{page_id}/metrics/{metric_id} | Update a metric


# **delete_pages_page_id_metrics_metric_id**
> Metric delete_pages_page_id_metrics_metric_id(page_id, metric_id)

Delete a metric

Delete a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier

try:
    # Delete a metric
    api_response = api_instance.delete_pages_page_id_metrics_metric_id(page_id, metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->delete_pages_page_id_metrics_metric_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 

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
**200** | Delete a metric |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pages_page_id_metrics_metric_id_data**
> Metric delete_pages_page_id_metrics_metric_id_data(page_id, metric_id)

Reset data for a metric

Reset data for a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier

try:
    # Reset data for a metric
    api_response = api_instance.delete_pages_page_id_metrics_metric_id_data(page_id, metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->delete_pages_page_id_metrics_metric_id_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 

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
**200** | Reset data for a metric |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_metrics**
> Metric get_pages_page_id_metrics(page_id)

Get a list of metrics

Get a list of metrics

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a list of metrics
    api_response = api_instance.get_pages_page_id_metrics(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_pages_page_id_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

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
**200** | Get a list of metrics |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_metrics_metric_id**
> Metric get_pages_page_id_metrics_metric_id(page_id, metric_id)

Get a metric

Get a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier

try:
    # Get a metric
    api_response = api_instance.get_pages_page_id_metrics_metric_id(page_id, metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_pages_page_id_metrics_metric_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 

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
**200** | Get a metric |  -  |
**401** | Could not authenticate |  -  |
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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier

try:
    # List metrics for a metric provider
    api_response = api_instance.get_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_pages_page_id_metrics_providers_metrics_provider_id_metrics: %s\n" % e)
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

# **patch_pages_page_id_metrics_metric_id**
> Metric patch_pages_page_id_metrics_metric_id(page_id, metric_id, patch_pages_page_id_metrics)

Update a metric

Update a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier
patch_pages_page_id_metrics = spio.PatchPagesPageIdMetrics() # PatchPagesPageIdMetrics | 

try:
    # Update a metric
    api_response = api_instance.patch_pages_page_id_metrics_metric_id(page_id, metric_id, patch_pages_page_id_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->patch_pages_page_id_metrics_metric_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 
 **patch_pages_page_id_metrics** | [**PatchPagesPageIdMetrics**](PatchPagesPageIdMetrics.md)|  | 

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
**200** | Update a metric |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_metrics_data**
> MetricAddResponse post_pages_page_id_metrics_data(page_id, post_pages_page_id_metrics_data)

Add data points to metrics

Add data points to metrics

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_metrics_data = spio.PostPagesPageIdMetricsData() # PostPagesPageIdMetricsData | 

try:
    # Add data points to metrics
    api_response = api_instance.post_pages_page_id_metrics_data(page_id, post_pages_page_id_metrics_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->post_pages_page_id_metrics_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_metrics_data** | [**PostPagesPageIdMetricsData**](PostPagesPageIdMetricsData.md)|  | 

### Return type

[**MetricAddResponse**](MetricAddResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add data points to metrics |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**405** | Method not allowed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_metrics_metric_id_data**
> SingleMetricAddResponse post_pages_page_id_metrics_metric_id_data(page_id, metric_id, post_pages_page_id_metrics_metric_id_data)

Add data to a metric

Add data to a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier
post_pages_page_id_metrics_metric_id_data = spio.PostPagesPageIdMetricsMetricIdData() # PostPagesPageIdMetricsMetricIdData | 

try:
    # Add data to a metric
    api_response = api_instance.post_pages_page_id_metrics_metric_id_data(page_id, metric_id, post_pages_page_id_metrics_metric_id_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->post_pages_page_id_metrics_metric_id_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 
 **post_pages_page_id_metrics_metric_id_data** | [**PostPagesPageIdMetricsMetricIdData**](PostPagesPageIdMetricsMetricIdData.md)|  | 

### Return type

[**SingleMetricAddResponse**](SingleMetricAddResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add data to a metric |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**405** | Method not allowed. |  -  |
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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metrics_provider_id = 'metrics_provider_id_example' # str | Metric Provider Identifier
post_pages_page_id_metrics_providers_metrics_provider_id_metrics = spio.PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics() # PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics | 

try:
    # Create a metric for a metric provider
    api_response = api_instance.post_pages_page_id_metrics_providers_metrics_provider_id_metrics(page_id, metrics_provider_id, post_pages_page_id_metrics_providers_metrics_provider_id_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->post_pages_page_id_metrics_providers_metrics_provider_id_metrics: %s\n" % e)
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

# **put_pages_page_id_metrics_metric_id**
> Metric put_pages_page_id_metrics_metric_id(page_id, metric_id, put_pages_page_id_metrics)

Update a metric

Update a metric

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
api_instance = spio.MetricsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
metric_id = 'metric_id_example' # str | Metric Identifier
put_pages_page_id_metrics = spio.PutPagesPageIdMetrics() # PutPagesPageIdMetrics | 

try:
    # Update a metric
    api_response = api_instance.put_pages_page_id_metrics_metric_id(page_id, metric_id, put_pages_page_id_metrics)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->put_pages_page_id_metrics_metric_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **metric_id** | **str**| Metric Identifier | 
 **put_pages_page_id_metrics** | [**PutPagesPageIdMetrics**](PutPagesPageIdMetrics.md)|  | 

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
**200** | Update a metric |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

