# spio.IncidentsApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_incidents_incident_id**](IncidentsApi.md#delete_pages_page_id_incidents_incident_id) | **DELETE** /pages/{page_id}/incidents/{incident_id} | Delete an incident
[**get_pages_page_id_incidents**](IncidentsApi.md#get_pages_page_id_incidents) | **GET** /pages/{page_id}/incidents | Get a list of incidents
[**get_pages_page_id_incidents_active_maintenance**](IncidentsApi.md#get_pages_page_id_incidents_active_maintenance) | **GET** /pages/{page_id}/incidents/active_maintenance | Get a list of active maintenances
[**get_pages_page_id_incidents_incident_id**](IncidentsApi.md#get_pages_page_id_incidents_incident_id) | **GET** /pages/{page_id}/incidents/{incident_id} | Get an incident
[**get_pages_page_id_incidents_scheduled**](IncidentsApi.md#get_pages_page_id_incidents_scheduled) | **GET** /pages/{page_id}/incidents/scheduled | Get a list of scheduled incidents
[**get_pages_page_id_incidents_unresolved**](IncidentsApi.md#get_pages_page_id_incidents_unresolved) | **GET** /pages/{page_id}/incidents/unresolved | Get a list of unresolved incidents
[**get_pages_page_id_incidents_upcoming**](IncidentsApi.md#get_pages_page_id_incidents_upcoming) | **GET** /pages/{page_id}/incidents/upcoming | Get a list of upcoming incidents
[**patch_pages_page_id_incidents_incident_id**](IncidentsApi.md#patch_pages_page_id_incidents_incident_id) | **PATCH** /pages/{page_id}/incidents/{incident_id} | Update an incident
[**post_pages_page_id_incidents**](IncidentsApi.md#post_pages_page_id_incidents) | **POST** /pages/{page_id}/incidents | Create an incident
[**put_pages_page_id_incidents_incident_id**](IncidentsApi.md#put_pages_page_id_incidents_incident_id) | **PUT** /pages/{page_id}/incidents/{incident_id} | Update an incident


# **delete_pages_page_id_incidents_incident_id**
> Incident delete_pages_page_id_incidents_incident_id(page_id, incident_id)

Delete an incident

Delete an incident

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Delete an incident
    api_response = api_instance.delete_pages_page_id_incidents_incident_id(page_id, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->delete_pages_page_id_incidents_incident_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

### Return type

[**Incident**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete an incident |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents**
> list[Incident] get_pages_page_id_incidents(page_id, q=q, limit=limit, page=page)

Get a list of incidents

Get a list of incidents

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
q = 'q_example' # str | If this is specified, search for the text query string in the incidents' name, status, postmortem_body, and incident_updates fields. (optional)
limit = 56 # int | The maximum number of rows to return per page. The default and maximum limit is 100. (optional)
page = 56 # int | Page offset to fetch. (optional)

try:
    # Get a list of incidents
    api_response = api_instance.get_pages_page_id_incidents(page_id, q=q, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **q** | **str**| If this is specified, search for the text query string in the incidents&#39; name, status, postmortem_body, and incident_updates fields. | [optional] 
 **limit** | **int**| The maximum number of rows to return per page. The default and maximum limit is 100. | [optional] 
 **page** | **int**| Page offset to fetch. | [optional] 

### Return type

[**list[Incident]**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of incidents |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_active_maintenance**
> list[Incident] get_pages_page_id_incidents_active_maintenance(page_id, page=page, per_page=per_page)

Get a list of active maintenances

Get a list of active maintenances

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 1 # int | Page offset to fetch. (optional) (default to 1)
per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

try:
    # Get a list of active maintenances
    api_response = api_instance.get_pages_page_id_incidents_active_maintenance(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents_active_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**list[Incident]**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of active maintenances |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_incident_id**
> Incident get_pages_page_id_incidents_incident_id(page_id, incident_id)

Get an incident

Get an incident

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier

try:
    # Get an incident
    api_response = api_instance.get_pages_page_id_incidents_incident_id(page_id, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents_incident_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 

### Return type

[**Incident**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get an incident |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_scheduled**
> list[Incident] get_pages_page_id_incidents_scheduled(page_id, page=page, per_page=per_page)

Get a list of scheduled incidents

Get a list of scheduled incidents

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 1 # int | Page offset to fetch. (optional) (default to 1)
per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

try:
    # Get a list of scheduled incidents
    api_response = api_instance.get_pages_page_id_incidents_scheduled(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents_scheduled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**list[Incident]**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of scheduled incidents |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_unresolved**
> list[Incident] get_pages_page_id_incidents_unresolved(page_id, page=page, per_page=per_page)

Get a list of unresolved incidents

Get a list of unresolved incidents

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 1 # int | Page offset to fetch. (optional) (default to 1)
per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

try:
    # Get a list of unresolved incidents
    api_response = api_instance.get_pages_page_id_incidents_unresolved(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents_unresolved: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**list[Incident]**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of unresolved incidents |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_incidents_upcoming**
> list[Incident] get_pages_page_id_incidents_upcoming(page_id, page=page, per_page=per_page)

Get a list of upcoming incidents

Get a list of upcoming incidents

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 1 # int | Page offset to fetch. (optional) (default to 1)
per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

try:
    # Get a list of upcoming incidents
    api_response = api_instance.get_pages_page_id_incidents_upcoming(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->get_pages_page_id_incidents_upcoming: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**list[Incident]**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of upcoming incidents |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pages_page_id_incidents_incident_id**
> Incident patch_pages_page_id_incidents_incident_id(page_id, incident_id, patch_pages_page_id_incidents)

Update an incident

Update an incident

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
patch_pages_page_id_incidents = spio.PatchPagesPageIdIncidents() # PatchPagesPageIdIncidents | 

try:
    # Update an incident
    api_response = api_instance.patch_pages_page_id_incidents_incident_id(page_id, incident_id, patch_pages_page_id_incidents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->patch_pages_page_id_incidents_incident_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **patch_pages_page_id_incidents** | [**PatchPagesPageIdIncidents**](PatchPagesPageIdIncidents.md)|  | 

### Return type

[**Incident**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update an incident |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_incidents**
> Incident post_pages_page_id_incidents(page_id, post_pages_page_id_incidents)

Create an incident

Create an incident

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_incidents = spio.PostPagesPageIdIncidents() # PostPagesPageIdIncidents | 

try:
    # Create an incident
    api_response = api_instance.post_pages_page_id_incidents(page_id, post_pages_page_id_incidents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->post_pages_page_id_incidents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_incidents** | [**PostPagesPageIdIncidents**](PostPagesPageIdIncidents.md)|  | 

### Return type

[**Incident**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create an incident |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_incidents_incident_id**
> Incident put_pages_page_id_incidents_incident_id(page_id, incident_id, put_pages_page_id_incidents)

Update an incident

Update an incident

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
api_instance = spio.IncidentsApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
put_pages_page_id_incidents = spio.PutPagesPageIdIncidents() # PutPagesPageIdIncidents | 

try:
    # Update an incident
    api_response = api_instance.put_pages_page_id_incidents_incident_id(page_id, incident_id, put_pages_page_id_incidents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentsApi->put_pages_page_id_incidents_incident_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **put_pages_page_id_incidents** | [**PutPagesPageIdIncidents**](PutPagesPageIdIncidents.md)|  | 

### Return type

[**Incident**](Incident.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update an incident |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

