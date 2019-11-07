# spio.IncidentUpdatesApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id**](IncidentUpdatesApi.md#patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id) | **PATCH** /pages/{page_id}/incidents/{incident_id}/incident_updates/{incident_update_id} | Update a previous incident update
[**put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id**](IncidentUpdatesApi.md#put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id) | **PUT** /pages/{page_id}/incidents/{incident_id}/incident_updates/{incident_update_id} | Update a previous incident update


# **patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id**
> IncidentUpdate patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id(page_id, incident_id, incident_update_id, patch_pages_page_id_incidents_incident_id_incident_updates)

Update a previous incident update

Update a previous incident update

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
api_instance = spio.IncidentUpdatesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
incident_update_id = 'incident_update_id_example' # str | Incident Update Identifier
patch_pages_page_id_incidents_incident_id_incident_updates = spio.PatchPagesPageIdIncidentsIncidentIdIncidentUpdates() # PatchPagesPageIdIncidentsIncidentIdIncidentUpdates | 

try:
    # Update a previous incident update
    api_response = api_instance.patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id(page_id, incident_id, incident_update_id, patch_pages_page_id_incidents_incident_id_incident_updates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentUpdatesApi->patch_pages_page_id_incidents_incident_id_incident_updates_incident_update_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **incident_update_id** | **str**| Incident Update Identifier | 
 **patch_pages_page_id_incidents_incident_id_incident_updates** | [**PatchPagesPageIdIncidentsIncidentIdIncidentUpdates**](PatchPagesPageIdIncidentsIncidentIdIncidentUpdates.md)|  | 

### Return type

[**IncidentUpdate**](IncidentUpdate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a previous incident update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id**
> IncidentUpdate put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id(page_id, incident_id, incident_update_id, put_pages_page_id_incidents_incident_id_incident_updates)

Update a previous incident update

Update a previous incident update

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
api_instance = spio.IncidentUpdatesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
incident_id = 'incident_id_example' # str | Incident Identifier
incident_update_id = 'incident_update_id_example' # str | Incident Update Identifier
put_pages_page_id_incidents_incident_id_incident_updates = spio.PutPagesPageIdIncidentsIncidentIdIncidentUpdates() # PutPagesPageIdIncidentsIncidentIdIncidentUpdates | 

try:
    # Update a previous incident update
    api_response = api_instance.put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id(page_id, incident_id, incident_update_id, put_pages_page_id_incidents_incident_id_incident_updates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentUpdatesApi->put_pages_page_id_incidents_incident_id_incident_updates_incident_update_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **incident_id** | **str**| Incident Identifier | 
 **incident_update_id** | **str**| Incident Update Identifier | 
 **put_pages_page_id_incidents_incident_id_incident_updates** | [**PutPagesPageIdIncidentsIncidentIdIncidentUpdates**](PutPagesPageIdIncidentsIncidentIdIncidentUpdates.md)|  | 

### Return type

[**IncidentUpdate**](IncidentUpdate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a previous incident update |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

