# spio.IncidentSubscribersApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id**](IncidentSubscribersApi.md#delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id) | **DELETE** /pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id} | Unsubscribe an incident subscriber
[**get_pages_page_id_incidents_incident_id_subscribers**](IncidentSubscribersApi.md#get_pages_page_id_incidents_incident_id_subscribers) | **GET** /pages/{page_id}/incidents/{incident_id}/subscribers | Get a list of incident subscribers
[**get_pages_page_id_incidents_incident_id_subscribers_subscriber_id**](IncidentSubscribersApi.md#get_pages_page_id_incidents_incident_id_subscribers_subscriber_id) | **GET** /pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id} | Get an incident subscriber
[**post_pages_page_id_incidents_incident_id_subscribers**](IncidentSubscribersApi.md#post_pages_page_id_incidents_incident_id_subscribers) | **POST** /pages/{page_id}/incidents/{incident_id}/subscribers | Create an incident subscriber
[**post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation**](IncidentSubscribersApi.md#post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation) | **POST** /pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id}/resend_confirmation | Resend confirmation to an incident subscriber


# **delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id**
> Subscriber delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id)

Unsubscribe an incident subscriber

Unsubscribe an incident subscriber

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
api_instance = spio.IncidentSubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier

try:
    # Unsubscribe an incident subscriber
    api_response = api_instance.delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentSubscribersApi->delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **subscriber_id** | **str**| Subscriber Identifier | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsubscribe an incident subscriber |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_incident_id_subscribers**
> list[Subscriber] get_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id)

Get a list of incident subscribers

Get a list of incident subscribers

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
api_instance = spio.IncidentSubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Get a list of incident subscribers
    api_response = api_instance.get_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentSubscribersApi->get_pages_page_id_incidents_incident_id_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

### Return type

[**list[Subscriber]**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of incident subscribers |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_incident_id_subscribers_subscriber_id**
> Subscriber get_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id)

Get an incident subscriber

Get an incident subscriber

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
api_instance = spio.IncidentSubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier

try:
    # Get an incident subscriber
    api_response = api_instance.get_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentSubscribersApi->get_pages_page_id_incidents_incident_id_subscribers_subscriber_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **subscriber_id** | **str**| Subscriber Identifier | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get an incident subscriber |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_incidents_incident_id_subscribers**
> Subscriber post_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers)

Create an incident subscriber

Create an incident subscriber

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
api_instance = spio.IncidentSubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
post_pages_page_id_incidents_incident_id_subscribers = spio.PostPagesPageIdIncidentsIncidentIdSubscribers() # PostPagesPageIdIncidentsIncidentIdSubscribers | 

try:
    # Create an incident subscriber
    api_response = api_instance.post_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentSubscribersApi->post_pages_page_id_incidents_incident_id_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **post_pages_page_id_incidents_incident_id_subscribers** | [**PostPagesPageIdIncidentsIncidentIdSubscribers**](PostPagesPageIdIncidentsIncidentIdSubscribers.md)|  | 

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create an incident subscriber |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation**
> post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation(page_id, incident_id, subscriber_id)

Resend confirmation to an incident subscriber

Resend confirmation to an incident subscriber

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
api_instance = spio.IncidentSubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier

try:
    # Resend confirmation to an incident subscriber
    api_instance.post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation(page_id, incident_id, subscriber_id)
except ApiException as e:
    print("Exception when calling IncidentSubscribersApi->post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **subscriber_id** | **str**| Subscriber Identifier | 

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
**201** | Resend confirmation to an incident subscriber |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

