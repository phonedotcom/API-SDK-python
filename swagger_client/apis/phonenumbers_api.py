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


class PhonenumbersApi(object):
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

    def create_account_phone_number(self, account_id, **kwargs):
        """
        Add a phone number to an account.
        Add a phone number to an account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_phone_number(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreatePhoneNumberParams data: Phone Number data
        :return: PhoneNumberFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_account_phone_number_with_http_info(account_id, **kwargs)
        else:
            (data) = self.create_account_phone_number_with_http_info(account_id, **kwargs)
            return data

    def create_account_phone_number_with_http_info(self, account_id, **kwargs):
        """
        Add a phone number to an account.
        Add a phone number to an account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_phone_number_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param CreatePhoneNumberParams data: Phone Number data
        :return: PhoneNumberFull
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
                    " to method create_account_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_account_phone_number`")


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

        return self.api_client.call_api('/accounts/{account_id}/phone-numbers', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PhoneNumberFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_account_phone_number(self, account_id, number_id, **kwargs):
        """
        Show details of an individual phone number.
        Show details of an individual phone number. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_phone_number(account_id, number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int number_id: Number ID (required)
        :return: PhoneNumberFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_phone_number_with_http_info(account_id, number_id, **kwargs)
        else:
            (data) = self.get_account_phone_number_with_http_info(account_id, number_id, **kwargs)
            return data

    def get_account_phone_number_with_http_info(self, account_id, number_id, **kwargs):
        """
        Show details of an individual phone number.
        Show details of an individual phone number. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_phone_number_with_http_info(account_id, number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int number_id: Number ID (required)
        :return: PhoneNumberFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'number_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_phone_number`")
        # verify the required parameter 'number_id' is set
        if ('number_id' not in params) or (params['number_id'] is None):
            raise ValueError("Missing the required parameter `number_id` when calling `get_account_phone_number`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'number_id' in params:
            path_params['number_id'] = params['number_id']

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

        return self.api_client.call_api('/accounts/{account_id}/phone-numbers/{number_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PhoneNumberFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_account_phone_numbers(self, account_id, **kwargs):
        """
        Get a list of phone numbers registered to an account.
        Get a list of phone numbers registered to an account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_phone_numbers(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_name: Name filter
        :param list[str] filters_phone_number: Phone number filter
        :param str sort_id: ID sorting
        :param str sort_name: Name sorting
        :param str sort_phone_number: Phone number sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListPhoneNumbers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_account_phone_numbers_with_http_info(account_id, **kwargs)
        else:
            (data) = self.list_account_phone_numbers_with_http_info(account_id, **kwargs)
            return data

    def list_account_phone_numbers_with_http_info(self, account_id, **kwargs):
        """
        Get a list of phone numbers registered to an account.
        Get a list of phone numbers registered to an account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_phone_numbers_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_name: Name filter
        :param list[str] filters_phone_number: Phone number filter
        :param str sort_id: ID sorting
        :param str sort_name: Name sorting
        :param str sort_phone_number: Phone number sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListPhoneNumbers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'filters_id', 'filters_name', 'filters_phone_number', 'sort_id', 'sort_name', 'sort_phone_number', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_account_phone_numbers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_account_phone_numbers`")

        if 'sort_id' in params and not re.search('asc|desc', params['sort_id']):
            raise ValueError("Invalid value for parameter `sort_id` when calling `list_account_phone_numbers`, must conform to the pattern `/asc|desc/`")
        if 'sort_name' in params and not re.search('asc|desc', params['sort_name']):
            raise ValueError("Invalid value for parameter `sort_name` when calling `list_account_phone_numbers`, must conform to the pattern `/asc|desc/`")
        if 'sort_phone_number' in params and not re.search('asc|desc', params['sort_phone_number']):
            raise ValueError("Invalid value for parameter `sort_phone_number` when calling `list_account_phone_numbers`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

        query_params = []
        if 'filters_id' in params:
            query_params.append(('filters[id]', params['filters_id']))
            collection_formats['filters[id]'] = 'multi'
        if 'filters_name' in params:
            query_params.append(('filters[name]', params['filters_name']))
            collection_formats['filters[name]'] = 'multi'
        if 'filters_phone_number' in params:
            query_params.append(('filters[phone_number]', params['filters_phone_number']))
            collection_formats['filters[phone_number]'] = 'multi'
        if 'sort_id' in params:
            query_params.append(('sort[id]', params['sort_id']))
        if 'sort_name' in params:
            query_params.append(('sort[name]', params['sort_name']))
        if 'sort_phone_number' in params:
            query_params.append(('sort[phone_number]', params['sort_phone_number']))
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

        return self.api_client.call_api('/accounts/{account_id}/phone-numbers', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListPhoneNumbers',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def replace_account_phone_number(self, account_id, number_id, **kwargs):
        """
        Update the settings for an existing phone number on your account.
        Update the settings for an existing phone number on your account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.replace_account_phone_number(account_id, number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int number_id: Number ID (required)
        :param ReplacePhoneNumberParams data: Phone Number data
        :return: PhoneNumberFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.replace_account_phone_number_with_http_info(account_id, number_id, **kwargs)
        else:
            (data) = self.replace_account_phone_number_with_http_info(account_id, number_id, **kwargs)
            return data

    def replace_account_phone_number_with_http_info(self, account_id, number_id, **kwargs):
        """
        Update the settings for an existing phone number on your account.
        Update the settings for an existing phone number on your account. See Account Phone Numbers for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.replace_account_phone_number_with_http_info(account_id, number_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int number_id: Number ID (required)
        :param ReplacePhoneNumberParams data: Phone Number data
        :return: PhoneNumberFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'number_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_account_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `replace_account_phone_number`")
        # verify the required parameter 'number_id' is set
        if ('number_id' not in params) or (params['number_id'] is None):
            raise ValueError("Missing the required parameter `number_id` when calling `replace_account_phone_number`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'number_id' in params:
            path_params['number_id'] = params['number_id']

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

        return self.api_client.call_api('/accounts/{account_id}/phone-numbers/{number_id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PhoneNumberFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
