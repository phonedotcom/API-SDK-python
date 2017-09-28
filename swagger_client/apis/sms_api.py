# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SmsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_account_sms(self, account_id, data, **kwargs):
        """
        Send a SMS to one or a group of recipients.
        Send a SMS to one or a group of recipients. For details on the input fields, see Intro to SMS. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Create SMS API with the following definition: POST https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_sms(account_id, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreateSmsParams data: SMS data (required)
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_account_sms_with_http_info(account_id, data, **kwargs)
        else:
            (data) = self.create_account_sms_with_http_info(account_id, data, **kwargs)
            return data

    def create_account_sms_with_http_info(self, account_id, data, **kwargs):
        """
        Send a SMS to one or a group of recipients.
        Send a SMS to one or a group of recipients. For details on the input fields, see Intro to SMS. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Create SMS API with the following definition: POST https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_sms_with_http_info(account_id, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreateSmsParams data: SMS data (required)
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_account_sms`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_account_sms`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/accounts/{account_id}/sms', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SmsFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_account_sms(self, account_id, sms_id, **kwargs):
        """
        This service shows the details of an individual SMS.
        This service shows the details of an individual SMS. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Get SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_sms(account_id, sms_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param str sms_id: SMS ID (required)
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_sms_with_http_info(account_id, sms_id, **kwargs)
        else:
            (data) = self.get_account_sms_with_http_info(account_id, sms_id, **kwargs)
            return data

    def get_account_sms_with_http_info(self, account_id, sms_id, **kwargs):
        """
        This service shows the details of an individual SMS.
        This service shows the details of an individual SMS. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Get SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_sms_with_http_info(account_id, sms_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param str sms_id: SMS ID (required)
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'sms_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_sms`")
        # verify the required parameter 'sms_id' is set
        if ('sms_id' not in params) or (params['sms_id'] is None):
            raise ValueError("Missing the required parameter `sms_id` when calling `get_account_sms`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'sms_id' in params:
            path_params['sms_id'] = params['sms_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/accounts/{account_id}/sms/{sms_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SmsFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_account_sms(self, account_id, **kwargs):
        """
        Get a list of SMS messages for an account.
        Get a list of SMS messages for an account. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level List SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_sms(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param str filters_from: Caller ID filter
        :param str filters_to: Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B
        :param str filters_direction: Direction filter
        :param list[str] filters_extension: Extension filter
        :param str filters_created_at: Date string representing the UTC time that sms was created
        :param str sort_id: ID sorting
        :param str sort_created_at: Sort by created time of message
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListSms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_account_sms_with_http_info(account_id, **kwargs)
        else:
            (data) = self.list_account_sms_with_http_info(account_id, **kwargs)
            return data

    def list_account_sms_with_http_info(self, account_id, **kwargs):
        """
        Get a list of SMS messages for an account.
        Get a list of SMS messages for an account. See Intro to SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level List SMS API with the following definition: GET https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_sms_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param str filters_from: Caller ID filter
        :param str filters_to: Callee ID filter, the E.164 phone number to send the SMS TO. Note you must encode the + as %2B
        :param str filters_direction: Direction filter
        :param list[str] filters_extension: Extension filter
        :param str filters_created_at: Date string representing the UTC time that sms was created
        :param str sort_id: ID sorting
        :param str sort_created_at: Sort by created time of message
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListSms
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'filters_id', 'filters_from', 'filters_to', 'filters_direction', 'filters_extension', 'filters_created_at', 'sort_id', 'sort_created_at', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_account_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_account_sms`")

        if 'filters_from' in params and not re.search('^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*', params['filters_from']):
            raise ValueError("Invalid value for parameter `filters_from` when calling `list_account_sms`, must conform to the pattern `/^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*/`")
        if 'filters_to' in params and not re.search('^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*', params['filters_to']):
            raise ValueError("Invalid value for parameter `filters_to` when calling `list_account_sms`, must conform to the pattern `/^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*/`")
        if 'filters_direction' in params and not re.search('^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*', params['filters_direction']):
            raise ValueError("Invalid value for parameter `filters_direction` when calling `list_account_sms`, must conform to the pattern `/^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*/`")
        if 'filters_created_at' in params and not re.search('^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*', params['filters_created_at']):
            raise ValueError("Invalid value for parameter `filters_created_at` when calling `list_account_sms`, must conform to the pattern `/^eq:.*|^ne:.*|^lt:.*|^gt:.*|^lte:.*|^gte:.*|^starts-with:.*|^ends-with:.*|^contains:.*|^not-starts-with:.*|^not-ends-with:.*|^not-contains:.*|^between:.*,.*|^not-between:.*,.*/`")
        if 'sort_id' in params and not re.search('asc|desc', params['sort_id']):
            raise ValueError("Invalid value for parameter `sort_id` when calling `list_account_sms`, must conform to the pattern `/asc|desc/`")
        if 'sort_created_at' in params and not re.search('asc|desc', params['sort_created_at']):
            raise ValueError("Invalid value for parameter `sort_created_at` when calling `list_account_sms`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = []
        if 'filters_id' in params:
            query_params.append(('filters[id]', params['filters_id']))
            collection_formats['filters[id]'] = 'multi'
        if 'filters_from' in params:
            query_params.append(('filters[from]', params['filters_from']))
        if 'filters_to' in params:
            query_params.append(('filters[to]', params['filters_to']))
        if 'filters_direction' in params:
            query_params.append(('filters[direction]', params['filters_direction']))
        if 'filters_extension' in params:
            query_params.append(('filters[extension]', params['filters_extension']))
            collection_formats['filters[extension]'] = 'multi'
        if 'filters_created_at' in params:
            query_params.append(('filters[created_at]', params['filters_created_at']))
        if 'sort_id' in params:
            query_params.append(('sort[id]', params['sort_id']))
        if 'sort_created_at' in params:
            query_params.append(('sort[created_at]', params['sort_created_at']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'fields' in params:
            query_params.append(('fields', params['fields']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/accounts/{account_id}/sms', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListSms',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def patch_account_sms(self, account_id, sms_id, **kwargs):
        """
        Update the is_new parameter in a sms record.
        Update the is_new parameter in a sms record. See Account SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Patch SMS API with the following definition: PATCH https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_account_sms(account_id, sms_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param str sms_id: SMS ID (required)
        :param PatchSmsParams data: Sms data
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.patch_account_sms_with_http_info(account_id, sms_id, **kwargs)
        else:
            (data) = self.patch_account_sms_with_http_info(account_id, sms_id, **kwargs)
            return data

    def patch_account_sms_with_http_info(self, account_id, sms_id, **kwargs):
        """
        Update the is_new parameter in a sms record.
        Update the is_new parameter in a sms record. See Account SMS for more info on the properties. Note: This API is for users with Account Owner scope access token. Users with Extension User scope token should invoke the Extension level Patch SMS API with the following definition: PATCH https://api.phone.com/v4/accounts/:account_id/extensions/:extension_id/sms/:sms_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_account_sms_with_http_info(account_id, sms_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param str sms_id: SMS ID (required)
        :param PatchSmsParams data: Sms data
        :return: SmsFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'sms_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_account_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `patch_account_sms`")
        # verify the required parameter 'sms_id' is set
        if ('sms_id' not in params) or (params['sms_id'] is None):
            raise ValueError("Missing the required parameter `sms_id` when calling `patch_account_sms`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'sms_id' in params:
            path_params['sms_id'] = params['sms_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api('/accounts/{account_id}/sms/{sms_id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SmsFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
