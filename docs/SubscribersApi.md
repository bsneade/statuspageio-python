# spio.SubscribersApi

All URIs are relative to *https://api.statuspage.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pages_page_id_subscribers_subscriber_id**](SubscribersApi.md#delete_pages_page_id_subscribers_subscriber_id) | **DELETE** /pages/{page_id}/subscribers/{subscriber_id} | Unsubscribe a subscriber
[**get_pages_page_id_subscribers**](SubscribersApi.md#get_pages_page_id_subscribers) | **GET** /pages/{page_id}/subscribers | Get a list of subscribers
[**get_pages_page_id_subscribers_count**](SubscribersApi.md#get_pages_page_id_subscribers_count) | **GET** /pages/{page_id}/subscribers/count | Get a count of subscribers by type
[**get_pages_page_id_subscribers_histogram_by_state**](SubscribersApi.md#get_pages_page_id_subscribers_histogram_by_state) | **GET** /pages/{page_id}/subscribers/histogram_by_state | Get a histogram of subscribers by type and then state
[**get_pages_page_id_subscribers_subscriber_id**](SubscribersApi.md#get_pages_page_id_subscribers_subscriber_id) | **GET** /pages/{page_id}/subscribers/{subscriber_id} | Get a subscriber
[**get_pages_page_id_subscribers_unsubscribed**](SubscribersApi.md#get_pages_page_id_subscribers_unsubscribed) | **GET** /pages/{page_id}/subscribers/unsubscribed | Get a list of unsubscribed subscribers
[**post_pages_page_id_subscribers**](SubscribersApi.md#post_pages_page_id_subscribers) | **POST** /pages/{page_id}/subscribers | Create a subscriber
[**post_pages_page_id_subscribers_reactivate**](SubscribersApi.md#post_pages_page_id_subscribers_reactivate) | **POST** /pages/{page_id}/subscribers/reactivate | Reactivate a list of subscribers
[**post_pages_page_id_subscribers_resend_confirmation**](SubscribersApi.md#post_pages_page_id_subscribers_resend_confirmation) | **POST** /pages/{page_id}/subscribers/resend_confirmation | Resend confirmations to a list of subscribers
[**post_pages_page_id_subscribers_subscriber_id_resend_confirmation**](SubscribersApi.md#post_pages_page_id_subscribers_subscriber_id_resend_confirmation) | **POST** /pages/{page_id}/subscribers/{subscriber_id}/resend_confirmation | Resend confirmation to a subscriber
[**post_pages_page_id_subscribers_unsubscribe**](SubscribersApi.md#post_pages_page_id_subscribers_unsubscribe) | **POST** /pages/{page_id}/subscribers/unsubscribe | Unsubscribe a list of subscribers


# **delete_pages_page_id_subscribers_subscriber_id**
> Subscriber delete_pages_page_id_subscribers_subscriber_id(page_id, subscriber_id, skip_unsubscription_notification=skip_unsubscription_notification)

Unsubscribe a subscriber

Unsubscribe a subscriber

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier
skip_unsubscription_notification = True # bool | If skip_unsubscription_notification is true, the subscriber does not receive any notifications when they are unsubscribed. (optional)

try:
    # Unsubscribe a subscriber
    api_response = api_instance.delete_pages_page_id_subscribers_subscriber_id(page_id, subscriber_id, skip_unsubscription_notification=skip_unsubscription_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->delete_pages_page_id_subscribers_subscriber_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **subscriber_id** | **str**| Subscriber Identifier | 
 **skip_unsubscription_notification** | **bool**| If skip_unsubscription_notification is true, the subscriber does not receive any notifications when they are unsubscribed. | [optional] 

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
**200** | Unsubscribe a subscriber |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_subscribers**
> list[Subscriber] get_pages_page_id_subscribers(page_id, q=q, type=type, state=state, limit=limit, page=page, sort_field=sort_field, sort_direction=sort_direction)

Get a list of subscribers

Get a list of subscribers

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
q = 'q_example' # str | If this is specified, search the contact information (email, endpoint, or phone number) for the provided value. (optional)
type = 'type_example' # str | If specified, only return subscribers of the indicated type. (optional)
state = 'active' # str | If this is present, only return subscribers in this state. Specify state \"all\" to find subscribers in any states. (optional) (default to 'active')
limit = 56 # int | The maximum number of rows to return. If a text query string is specified (q=), the default and maximum limit is 100. If the text query string is not specified, the default and maximum limit are not set, and not providing a limit will return all the subscribers. (optional)
page = 0 # int | The page offset of subscribers. The first page is page 0, the second page 1, etc. This skips page * limit subscribers. (optional) (default to 0)
sort_field = 'primary' # str | The field on which to sort: 'primary' to indicate sorting by the identifying field, 'created_at' for sorting by creation timestamp, 'quarantined_at' for sorting by quarantine timestamp, and 'relevance' which sorts by the relevancy of the search text. 'relevance' is not a valid parameter if no search text is supplied. (optional) (default to 'primary')
sort_direction = 'asc' # str | The sort direction of the listing. (optional) (default to 'asc')

try:
    # Get a list of subscribers
    api_response = api_instance.get_pages_page_id_subscribers(page_id, q=q, type=type, state=state, limit=limit, page=page, sort_field=sort_field, sort_direction=sort_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_pages_page_id_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **q** | **str**| If this is specified, search the contact information (email, endpoint, or phone number) for the provided value. | [optional] 
 **type** | **str**| If specified, only return subscribers of the indicated type. | [optional] 
 **state** | **str**| If this is present, only return subscribers in this state. Specify state \&quot;all\&quot; to find subscribers in any states. | [optional] [default to &#39;active&#39;]
 **limit** | **int**| The maximum number of rows to return. If a text query string is specified (q&#x3D;), the default and maximum limit is 100. If the text query string is not specified, the default and maximum limit are not set, and not providing a limit will return all the subscribers. | [optional] 
 **page** | **int**| The page offset of subscribers. The first page is page 0, the second page 1, etc. This skips page * limit subscribers. | [optional] [default to 0]
 **sort_field** | **str**| The field on which to sort: &#39;primary&#39; to indicate sorting by the identifying field, &#39;created_at&#39; for sorting by creation timestamp, &#39;quarantined_at&#39; for sorting by quarantine timestamp, and &#39;relevance&#39; which sorts by the relevancy of the search text. &#39;relevance&#39; is not a valid parameter if no search text is supplied. | [optional] [default to &#39;primary&#39;]
 **sort_direction** | **str**| The sort direction of the listing. | [optional] [default to &#39;asc&#39;]

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
**200** | Get a list of subscribers |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_subscribers_count**
> SubscriberCountByType get_pages_page_id_subscribers_count(page_id, type=type, state=state)

Get a count of subscribers by type

Get a count of subscribers by type

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
type = 'type_example' # str | If this is present, only count subscribers of this type. (optional)
state = 'active' # str | If this is present, only count subscribers in this state. Specify state \"all\" to count subscribers in any states. (optional) (default to 'active')

try:
    # Get a count of subscribers by type
    api_response = api_instance.get_pages_page_id_subscribers_count(page_id, type=type, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_pages_page_id_subscribers_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **type** | **str**| If this is present, only count subscribers of this type. | [optional] 
 **state** | **str**| If this is present, only count subscribers in this state. Specify state \&quot;all\&quot; to count subscribers in any states. | [optional] [default to &#39;active&#39;]

### Return type

[**SubscriberCountByType**](SubscriberCountByType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a count of subscribers by type |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_subscribers_histogram_by_state**
> SubscriberCountByTypeAndState get_pages_page_id_subscribers_histogram_by_state(page_id)

Get a histogram of subscribers by type and then state

Get a histogram of subscribers by type and then state

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a histogram of subscribers by type and then state
    api_response = api_instance.get_pages_page_id_subscribers_histogram_by_state(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_pages_page_id_subscribers_histogram_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

### Return type

[**SubscriberCountByTypeAndState**](SubscriberCountByTypeAndState.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a histogram of subscribers by type and then state |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_subscribers_subscriber_id**
> Subscriber get_pages_page_id_subscribers_subscriber_id(page_id, subscriber_id)

Get a subscriber

Get a subscriber

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier

try:
    # Get a subscriber
    api_response = api_instance.get_pages_page_id_subscribers_subscriber_id(page_id, subscriber_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_pages_page_id_subscribers_subscriber_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
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
**200** | Get a subscriber |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pages_page_id_subscribers_unsubscribed**
> list[Subscriber] get_pages_page_id_subscribers_unsubscribed(page_id)

Get a list of unsubscribed subscribers

Get a list of unsubscribed subscribers

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier

try:
    # Get a list of unsubscribed subscribers
    api_response = api_instance.get_pages_page_id_subscribers_unsubscribed(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->get_pages_page_id_subscribers_unsubscribed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 

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
**200** | Get a list of unsubscribed subscribers |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_subscribers**
> Subscriber post_pages_page_id_subscribers(page_id, post_pages_page_id_subscribers)

Create a subscriber

Create a subscriber

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_subscribers = spio.PostPagesPageIdSubscribers() # PostPagesPageIdSubscribers | 

try:
    # Create a subscriber
    api_response = api_instance.post_pages_page_id_subscribers(page_id, post_pages_page_id_subscribers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscribersApi->post_pages_page_id_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_subscribers** | [**PostPagesPageIdSubscribers**](PostPagesPageIdSubscribers.md)|  | 

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
**201** | Create a subscriber |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**403** | You are not authorized to access this resource. |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_subscribers_reactivate**
> post_pages_page_id_subscribers_reactivate(page_id, post_pages_page_id_subscribers_reactivate)

Reactivate a list of subscribers

Reactivate a list of subscribers

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_subscribers_reactivate = spio.PostPagesPageIdSubscribersReactivate() # PostPagesPageIdSubscribersReactivate | 

try:
    # Reactivate a list of subscribers
    api_instance.post_pages_page_id_subscribers_reactivate(page_id, post_pages_page_id_subscribers_reactivate)
except ApiException as e:
    print("Exception when calling SubscribersApi->post_pages_page_id_subscribers_reactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_subscribers_reactivate** | [**PostPagesPageIdSubscribersReactivate**](PostPagesPageIdSubscribersReactivate.md)|  | 

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
**201** | Reactivate a list of subscribers |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_subscribers_resend_confirmation**
> post_pages_page_id_subscribers_resend_confirmation(page_id, post_pages_page_id_subscribers_resend_confirmation)

Resend confirmations to a list of subscribers

Resend confirmations to a list of subscribers

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_subscribers_resend_confirmation = spio.PostPagesPageIdSubscribersResendConfirmation() # PostPagesPageIdSubscribersResendConfirmation | 

try:
    # Resend confirmations to a list of subscribers
    api_instance.post_pages_page_id_subscribers_resend_confirmation(page_id, post_pages_page_id_subscribers_resend_confirmation)
except ApiException as e:
    print("Exception when calling SubscribersApi->post_pages_page_id_subscribers_resend_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_subscribers_resend_confirmation** | [**PostPagesPageIdSubscribersResendConfirmation**](PostPagesPageIdSubscribersResendConfirmation.md)|  | 

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
**201** | Resend confirmations to a list of subscribers |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_subscribers_subscriber_id_resend_confirmation**
> post_pages_page_id_subscribers_subscriber_id_resend_confirmation(page_id, subscriber_id)

Resend confirmation to a subscriber

Resend confirmation to a subscriber

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
subscriber_id = 'subscriber_id_example' # str | Subscriber Identifier

try:
    # Resend confirmation to a subscriber
    api_instance.post_pages_page_id_subscribers_subscriber_id_resend_confirmation(page_id, subscriber_id)
except ApiException as e:
    print("Exception when calling SubscribersApi->post_pages_page_id_subscribers_subscriber_id_resend_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **subscriber_id** | **str**| Subscriber Identifier | 

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
**201** | Resend confirmation to a subscriber |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pages_page_id_subscribers_unsubscribe**
> post_pages_page_id_subscribers_unsubscribe(page_id, post_pages_page_id_subscribers_unsubscribe)

Unsubscribe a list of subscribers

Unsubscribe a list of subscribers

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
api_instance = spio.SubscribersApi(spio.ApiClient(configuration))
page_id = 'page_id_example' # str | Page identifier
post_pages_page_id_subscribers_unsubscribe = spio.PostPagesPageIdSubscribersUnsubscribe() # PostPagesPageIdSubscribersUnsubscribe | 

try:
    # Unsubscribe a list of subscribers
    api_instance.post_pages_page_id_subscribers_unsubscribe(page_id, post_pages_page_id_subscribers_unsubscribe)
except ApiException as e:
    print("Exception when calling SubscribersApi->post_pages_page_id_subscribers_unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier | 
 **post_pages_page_id_subscribers_unsubscribe** | [**PostPagesPageIdSubscribersUnsubscribe**](PostPagesPageIdSubscribersUnsubscribe.md)|  | 

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
**201** | Unsubscribe a list of subscribers |  -  |
**400** | Bad request |  -  |
**401** | Could not authenticate |  -  |
**404** | The requested resource could not be found. |  -  |
**422** | Unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

