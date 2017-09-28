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


class AccountsApi(object):
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

    def get_account(self, account_id, **kwargs):
        """
        Retrieve details of an individual account
        Retrieve details of an individual account. See Accounts for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :return: AccountFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_with_http_info(account_id, **kwargs)
        else:
            (data) = self.get_account_with_http_info(account_id, **kwargs)
            return data

    def get_account_with_http_info(self, account_id, **kwargs):
        """
        Retrieve details of an individual account
        Retrieve details of an individual account. See Accounts for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :return: AccountFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account`")


        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']

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

        return self.api_client.call_api('/accounts/{account_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AccountFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_accounts(self, **kwargs):
        """
        Get a list of accounts visible to the authenticated user or client.
        Get a list of accounts visible to the authenticated user or client. In most cases, there will only be one such account. See Accounts for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_accounts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] filters_id: ID filter
        :param str sort_id: ID sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListAccounts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_accounts_with_http_info(**kwargs)
        else:
            (data) = self.list_accounts_with_http_info(**kwargs)
            return data

    def list_accounts_with_http_info(self, **kwargs):
        """
        Get a list of accounts visible to the authenticated user or client.
        Get a list of accounts visible to the authenticated user or client. In most cases, there will only be one such account. See Accounts for more info on the properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_accounts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] filters_id: ID filter
        :param str sort_id: ID sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListAccounts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filters_id', 'sort_id', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_accounts" % key
                )
            params[key] = val
        del params['kwargs']

        if 'sort_id' in params and not re.search('asc|desc', params['sort_id']):
            raise ValueError("Invalid value for parameter `sort_id` when calling `list_accounts`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filters_id' in params:
            query_params.append(('filters[id]', params['filters_id']))
            collection_formats['filters[id]'] = 'multi'
        if 'sort_id' in params:
            query_params.append(('sort[id]', params['sort_id']))
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

        return self.api_client.call_api('/accounts', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListAccounts',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
