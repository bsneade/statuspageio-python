# spio.IncidentPostmortemApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_incidents_incident_id_postmortem**](IncidentPostmortemApi.md#delete_pages_page_id_incidents_incident_id_postmortem) | **DELETE** /pages/{page_id}/incidents/{incident_id}/postmortem | Delete Postmortem
[**get_pages_page_id_incidents_incident_id_postmortem**](IncidentPostmortemApi.md#get_pages_page_id_incidents_incident_id_postmortem) | **GET** /pages/{page_id}/incidents/{incident_id}/postmortem | Get Postmortem
[**put_pages_page_id_incidents_incident_id_postmortem**](IncidentPostmortemApi.md#put_pages_page_id_incidents_incident_id_postmortem) | **PUT** /pages/{page_id}/incidents/{incident_id}/postmortem | Create Postmortem
[**put_pages_page_id_incidents_incident_id_postmortem_publish**](IncidentPostmortemApi.md#put_pages_page_id_incidents_incident_id_postmortem_publish) | **PUT** /pages/{page_id}/incidents/{incident_id}/postmortem/publish | Publish Postmortem
[**put_pages_page_id_incidents_incident_id_postmortem_revert**](IncidentPostmortemApi.md#put_pages_page_id_incidents_incident_id_postmortem_revert) | **PUT** /pages/{page_id}/incidents/{incident_id}/postmortem/revert | Revert Postmortem


# **delete_pages_page_id_incidents_incident_id_postmortem**
> delete_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id)

Delete Postmortem

Delete Postmortem

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
api_instance = spio.IncidentPostmortemApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Delete Postmortem
    api_instance.delete_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id)
except ApiException as e:
    print("Exception when calling IncidentPostmortemApi->delete_pages_page_id_incidents_incident_id_postmortem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

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
**204** | Delete Postmortem |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_incident_id_postmortem**
> Postmortem get_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id)

Get Postmortem

Get Postmortem

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
api_instance = spio.IncidentPostmortemApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Get Postmortem
    api_response = api_instance.get_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentPostmortemApi->get_pages_page_id_incidents_incident_id_postmortem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

### Return type

[**Postmortem**](Postmortem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Postmortem |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_incidents_incident_id_postmortem**
> Postmortem put_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id, put_pages_page_id_incidents_incident_id_postmortem)

Create Postmortem

Create Postmortem

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
api_instance = spio.IncidentPostmortemApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
put_pages_page_id_incidents_incident_id_postmortem = spio.PutPagesPageIdIncidentsIncidentIdPostmortem() # PutPagesPageIdIncidentsIncidentIdPostmortem | 

try:
    # Create Postmortem
    api_response = api_instance.put_pages_page_id_incidents_incident_id_postmortem(page_id, incident_id, put_pages_page_id_incidents_incident_id_postmortem)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentPostmortemApi->put_pages_page_id_incidents_incident_id_postmortem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **put_pages_page_id_incidents_incident_id_postmortem** | [**PutPagesPageIdIncidentsIncidentIdPostmortem**](PutPagesPageIdIncidentsIncidentIdPostmortem.md)|  | 

### Return type

[**Postmortem**](Postmortem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Postmortem |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_incidents_incident_id_postmortem_publish**
> Postmortem put_pages_page_id_incidents_incident_id_postmortem_publish(page_id, incident_id, put_pages_page_id_incidents_incident_id_postmortem_publish)

Publish Postmortem

Publish Postmortem

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
api_instance = spio.IncidentPostmortemApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
put_pages_page_id_incidents_incident_id_postmortem_publish = spio.PutPagesPageIdIncidentsIncidentIdPostmortemPublish() # PutPagesPageIdIncidentsIncidentIdPostmortemPublish | 

try:
    # Publish Postmortem
    api_response = api_instance.put_pages_page_id_incidents_incident_id_postmortem_publish(page_id, incident_id, put_pages_page_id_incidents_incident_id_postmortem_publish)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentPostmortemApi->put_pages_page_id_incidents_incident_id_postmortem_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **put_pages_page_id_incidents_incident_id_postmortem_publish** | [**PutPagesPageIdIncidentsIncidentIdPostmortemPublish**](PutPagesPageIdIncidentsIncidentIdPostmortemPublish.md)|  | 

### Return type

[**Postmortem**](Postmortem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publish Postmortem |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_incidents_incident_id_postmortem_revert**
> Postmortem put_pages_page_id_incidents_incident_id_postmortem_revert(page_id, incident_id)

Revert Postmortem

Revert Postmortem

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
api_instance = spio.IncidentPostmortemApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Revert Postmortem
    api_response = api_instance.put_pages_page_id_incidents_incident_id_postmortem_revert(page_id, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentPostmortemApi->put_pages_page_id_incidents_incident_id_postmortem_revert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

### Return type

[**Postmortem**](Postmortem.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Revert Postmortem |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

