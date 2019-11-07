# coding: utf-8

"""
    Statuspage API

    # Code of Conduct Please don't abuse the API, and please report all feature requests and issues to https://help.statuspage.io/help/contact-us-30  # Rate Limiting Each API token is limited to 1 request / second as measured on a 60 second rolling window. To get this limit increased or lifted, please contact us at https://help.statuspage.io/help/contact-us-30  # Basics  ## HTTPS It's required  ## URL Prefix In order to maintain version integrity into the future, the API is versioned. All calls currently begin with the following prefix:    https://api.statuspage.io/v1/  ## RESTful Interface Wherever possible, the API seeks to implement repeatable patterns with logical, representative URLs and descriptive HTTP verbs. Below are some examples and conventions you will see throughout the documentation.  * Collections are buckets: https://api.statuspage.io/v1/pages/asdf123/incidents.json * Elements have unique IDs: https://api.statuspage.io/v1/pages/asdf123/incidents/jklm456.json * GET will retrieve information about a collection/element * POST will create an element in a collection * PATCH will update a single element * PUT will replace a single element in a collection (rarely used) * DELETE will destroy a single element  ## Sending Data Information can be sent in the body as form urlencoded or JSON, but make sure the Content-Type header matches the body structure or the server gremlins will be angry.  All examples are provided in JSON format, however they can easily be converted to form encoding if required.  Some examples of how to convert things are below:      // JSON     {       \"incident\": {         \"name\": \"test incident\",         \"components\": [\"8kbf7d35c070\", \"vtnh60py4yd7\"]       }     }      // Form Encoded (using curl as an example):     curl -X POST https://api.statuspage.io/v1/example \\       -d \"incident[name]=test incident\" \\       -d \"incident[components][]=8kbf7d35c070\" \\       -d \"incident[components][]=vtnh60py4yd7\"  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from spio.api_client import ApiClient
from spio.exceptions import (
    ApiTypeError,
    ApiValueError
)


class IncidentSubscribersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Unsubscribe an incident subscriber  # noqa: E501

        Unsubscribe an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(page_id, incident_id, subscriber_id, **kwargs)  # noqa: E501

    def delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Unsubscribe an incident subscriber  # noqa: E501

        Unsubscribe an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscriber, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_id', 'incident_id', 'subscriber_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['page_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `page_id` when calling `delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501
        # verify the required parameter 'incident_id' is set
        if self.api_client.client_side_validation and ('incident_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['incident_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `incident_id` when calling `delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501
        # verify the required parameter 'subscriber_id' is set
        if self.api_client.client_side_validation and ('subscriber_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscriber_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscriber_id` when calling `delete_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in local_var_params:
            path_params['page_id'] = local_var_params['page_id']  # noqa: E501
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']  # noqa: E501
        if 'subscriber_id' in local_var_params:
            path_params['subscriber_id'] = local_var_params['subscriber_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pages_page_id_incidents_incident_id_subscribers(self, page_id, incident_id, **kwargs):  # noqa: E501
        """Get a list of incident subscribers  # noqa: E501

        Get a list of incident subscribers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Subscriber]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_pages_page_id_incidents_incident_id_subscribers_with_http_info(page_id, incident_id, **kwargs)  # noqa: E501

    def get_pages_page_id_incidents_incident_id_subscribers_with_http_info(self, page_id, incident_id, **kwargs):  # noqa: E501
        """Get a list of incident subscribers  # noqa: E501

        Get a list of incident subscribers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pages_page_id_incidents_incident_id_subscribers_with_http_info(page_id, incident_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Subscriber], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_id', 'incident_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pages_page_id_incidents_incident_id_subscribers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['page_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `page_id` when calling `get_pages_page_id_incidents_incident_id_subscribers`")  # noqa: E501
        # verify the required parameter 'incident_id' is set
        if self.api_client.client_side_validation and ('incident_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['incident_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `incident_id` when calling `get_pages_page_id_incidents_incident_id_subscribers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in local_var_params:
            path_params['page_id'] = local_var_params['page_id']  # noqa: E501
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pages/{page_id}/incidents/{incident_id}/subscribers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Subscriber]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pages_page_id_incidents_incident_id_subscribers_subscriber_id(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Get an incident subscriber  # noqa: E501

        Get an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pages_page_id_incidents_incident_id_subscribers_subscriber_id(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(page_id, incident_id, subscriber_id, **kwargs)  # noqa: E501

    def get_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Get an incident subscriber  # noqa: E501

        Get an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pages_page_id_incidents_incident_id_subscribers_subscriber_id_with_http_info(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscriber, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_id', 'incident_id', 'subscriber_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pages_page_id_incidents_incident_id_subscribers_subscriber_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['page_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `page_id` when calling `get_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501
        # verify the required parameter 'incident_id' is set
        if self.api_client.client_side_validation and ('incident_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['incident_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `incident_id` when calling `get_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501
        # verify the required parameter 'subscriber_id' is set
        if self.api_client.client_side_validation and ('subscriber_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscriber_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscriber_id` when calling `get_pages_page_id_incidents_incident_id_subscribers_subscriber_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in local_var_params:
            path_params['page_id'] = local_var_params['page_id']  # noqa: E501
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']  # noqa: E501
        if 'subscriber_id' in local_var_params:
            path_params['subscriber_id'] = local_var_params['subscriber_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pages_page_id_incidents_incident_id_subscribers(self, page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers, **kwargs):  # noqa: E501
        """Create an incident subscriber  # noqa: E501

        Create an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pages_page_id_incidents_incident_id_subscribers(page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param PostPagesPageIdIncidentsIncidentIdSubscribers post_pages_page_id_incidents_incident_id_subscribers: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Subscriber
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_pages_page_id_incidents_incident_id_subscribers_with_http_info(page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers, **kwargs)  # noqa: E501

    def post_pages_page_id_incidents_incident_id_subscribers_with_http_info(self, page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers, **kwargs):  # noqa: E501
        """Create an incident subscriber  # noqa: E501

        Create an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pages_page_id_incidents_incident_id_subscribers_with_http_info(page_id, incident_id, post_pages_page_id_incidents_incident_id_subscribers, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param PostPagesPageIdIncidentsIncidentIdSubscribers post_pages_page_id_incidents_incident_id_subscribers: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Subscriber, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_id', 'incident_id', 'post_pages_page_id_incidents_incident_id_subscribers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pages_page_id_incidents_incident_id_subscribers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['page_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `page_id` when calling `post_pages_page_id_incidents_incident_id_subscribers`")  # noqa: E501
        # verify the required parameter 'incident_id' is set
        if self.api_client.client_side_validation and ('incident_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['incident_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `incident_id` when calling `post_pages_page_id_incidents_incident_id_subscribers`")  # noqa: E501
        # verify the required parameter 'post_pages_page_id_incidents_incident_id_subscribers' is set
        if self.api_client.client_side_validation and ('post_pages_page_id_incidents_incident_id_subscribers' not in local_var_params or  # noqa: E501
                                                        local_var_params['post_pages_page_id_incidents_incident_id_subscribers'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `post_pages_page_id_incidents_incident_id_subscribers` when calling `post_pages_page_id_incidents_incident_id_subscribers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in local_var_params:
            path_params['page_id'] = local_var_params['page_id']  # noqa: E501
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_pages_page_id_incidents_incident_id_subscribers' in local_var_params:
            body_params = local_var_params['post_pages_page_id_incidents_incident_id_subscribers']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pages/{page_id}/incidents/{incident_id}/subscribers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Subscriber',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Resend confirmation to an incident subscriber  # noqa: E501

        Resend confirmation to an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation_with_http_info(page_id, incident_id, subscriber_id, **kwargs)  # noqa: E501

    def post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation_with_http_info(self, page_id, incident_id, subscriber_id, **kwargs):  # noqa: E501
        """Resend confirmation to an incident subscriber  # noqa: E501

        Resend confirmation to an incident subscriber  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation_with_http_info(page_id, incident_id, subscriber_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str page_id: Page identifier (required)
        :param str incident_id: Incident Identifier (required)
        :param str subscriber_id: Subscriber Identifier (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['page_id', 'incident_id', 'subscriber_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'page_id' is set
        if self.api_client.client_side_validation and ('page_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['page_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `page_id` when calling `post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation`")  # noqa: E501
        # verify the required parameter 'incident_id' is set
        if self.api_client.client_side_validation and ('incident_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['incident_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `incident_id` when calling `post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation`")  # noqa: E501
        # verify the required parameter 'subscriber_id' is set
        if self.api_client.client_side_validation and ('subscriber_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['subscriber_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `subscriber_id` when calling `post_pages_page_id_incidents_incident_id_subscribers_subscriber_id_resend_confirmation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'page_id' in local_var_params:
            path_params['page_id'] = local_var_params['page_id']  # noqa: E501
        if 'incident_id' in local_var_params:
            path_params['incident_id'] = local_var_params['incident_id']  # noqa: E501
        if 'subscriber_id' in local_var_params:
            path_params['subscriber_id'] = local_var_params['subscriber_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/pages/{page_id}/incidents/{incident_id}/subscribers/{subscriber_id}/resend_confirmation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
