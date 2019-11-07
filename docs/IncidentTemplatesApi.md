# spio.IncidentTemplatesApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pages_page_id_incident_templates**](IncidentTemplatesApi.md#get_pages_page_id_incident_templates) | **GET** /pages/{page_id}/incident_templates | Get a list of incident templates


# **get_pages_page_id_incident_templates**
> list[IncidentTemplate] get_pages_page_id_incident_templates(page_id, page=page, per_page=per_page)

Get a list of incident templates

Get a list of incident templates

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
api_instance = spio.IncidentTemplatesApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
page = 1 # int | Page offset to fetch. (optional) (default to 1)
per_page = 100 # int | Number of results to return per page. (optional) (default to 100)

try:
    # Get a list of incident templates
    api_response = api_instance.get_pages_page_id_incident_templates(page_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IncidentTemplatesApi->get_pages_page_id_incident_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **page** | **int**| Page offset to fetch. | [optional] [default to 1]
 **per_page** | **int**| Number of results to return per page. | [optional] [default to 100]

### Return type

[**list[IncidentTemplate]**](IncidentTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of incident templates |  -  |
**401** | Could not authenticate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

