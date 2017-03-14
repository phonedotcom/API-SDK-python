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


class ContactsApi(object):
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

    def create_account_extension_contact(self, account_id, extension_id, **kwargs):
        """
        Add a new address book contact for an extension
        For more on the input fields, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_extension_contact(account_id, extension_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param CreateContactParams data: Contact data
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_account_extension_contact_with_http_info(account_id, extension_id, **kwargs)
        else:
            (data) = self.create_account_extension_contact_with_http_info(account_id, extension_id, **kwargs)
            return data

    def create_account_extension_contact_with_http_info(self, account_id, extension_id, **kwargs):
        """
        Add a new address book contact for an extension
        For more on the input fields, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_account_extension_contact_with_http_info(account_id, extension_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param CreateContactParams data: Contact data
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'extension_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account_extension_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_account_extension_contact`")
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params) or (params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `create_account_extension_contact`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/extensions/{extension_id}/contacts'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'extension_id' in params:
            path_params['extension_id'] = params['extension_id']

        query_params = {}

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

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ContactFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_account_extension_contact(self, account_id, extension_id, contact_id, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_account_extension_contact(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :return: DeleteContact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
        else:
            (data) = self.delete_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
            return data

    def delete_account_extension_contact_with_http_info(self, account_id, extension_id, contact_id, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_account_extension_contact_with_http_info(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :return: DeleteContact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'extension_id', 'contact_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_account_extension_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_account_extension_contact`")
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params) or (params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `delete_account_extension_contact`")
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `delete_account_extension_contact`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'extension_id' in params:
            path_params['extension_id'] = params['extension_id']
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']

        query_params = {}

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

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeleteContact',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_account_extension_contact(self, account_id, extension_id, contact_id, **kwargs):
        """
        Retrieve the details of an address book contact
        For more info on the fields shown, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_extension_contact(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
        else:
            (data) = self.get_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
            return data

    def get_account_extension_contact_with_http_info(self, account_id, extension_id, contact_id, **kwargs):
        """
        Retrieve the details of an address book contact
        For more info on the fields shown, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_extension_contact_with_http_info(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'extension_id', 'contact_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_extension_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_account_extension_contact`")
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params) or (params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `get_account_extension_contact`")
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `get_account_extension_contact`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'extension_id' in params:
            path_params['extension_id'] = params['extension_id']
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']

        query_params = {}

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

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ContactFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_account_extension_contacts(self, account_id, extension_id, **kwargs):
        """
        Show a list of address book contacts
        See Account Contacts for more info on the fields in each item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_extension_contacts(account_id, extension_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_group_id: Group filter
        :param list[str] filters_updated_at: Updated At filter
        :param str sort_id: ID sorting
        :param str sort_updated_at: Updated At sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListContacts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_account_extension_contacts_with_http_info(account_id, extension_id, **kwargs)
        else:
            (data) = self.list_account_extension_contacts_with_http_info(account_id, extension_id, **kwargs)
            return data

    def list_account_extension_contacts_with_http_info(self, account_id, extension_id, **kwargs):
        """
        Show a list of address book contacts
        See Account Contacts for more info on the fields in each item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_account_extension_contacts_with_http_info(account_id, extension_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param list[str] filters_id: ID filter
        :param list[str] filters_group_id: Group filter
        :param list[str] filters_updated_at: Updated At filter
        :param str sort_id: ID sorting
        :param str sort_updated_at: Updated At sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListContacts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'extension_id', 'filters_id', 'filters_group_id', 'filters_updated_at', 'sort_id', 'sort_updated_at', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_account_extension_contacts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_account_extension_contacts`")
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params) or (params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `list_account_extension_contacts`")

        if 'sort_id' in params and not re.search('asc|desc', params['sort_id']):
            raise ValueError("Invalid value for parameter `sort_id` when calling `list_account_extension_contacts`, must conform to the pattern `/asc|desc/`")
        if 'sort_updated_at' in params and not re.search('asc|desc', params['sort_updated_at']):
            raise ValueError("Invalid value for parameter `sort_updated_at` when calling `list_account_extension_contacts`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        resource_path = '/accounts/{account_id}/extensions/{extension_id}/contacts'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'extension_id' in params:
            path_params['extension_id'] = params['extension_id']

        query_params = {}
        if 'filters_id' in params:
            query_params['filters[id]'] = params['filters_id']
            collection_formats['filters[id]'] = 'multi'
        if 'filters_group_id' in params:
            query_params['filters[group_id]'] = params['filters_group_id']
            collection_formats['filters[group_id]'] = 'multi'
        if 'filters_updated_at' in params:
            query_params['filters[updated_at]'] = params['filters_updated_at']
            collection_formats['filters[updated_at]'] = 'multi'
        if 'sort_id' in params:
            query_params['sort[id]'] = params['sort_id']
        if 'sort_updated_at' in params:
            query_params['sort[updated_at]'] = params['sort_updated_at']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'fields' in params:
            query_params['fields'] = params['fields']

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

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListContacts',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def replace_account_extension_contact(self, account_id, extension_id, contact_id, **kwargs):
        """
        
        For more on the input fields, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.replace_account_extension_contact(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :param CreateContactParams data: Contact data
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.replace_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
        else:
            (data) = self.replace_account_extension_contact_with_http_info(account_id, extension_id, contact_id, **kwargs)
            return data

    def replace_account_extension_contact_with_http_info(self, account_id, extension_id, contact_id, **kwargs):
        """
        
        For more on the input fields, see Account Contacts.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.replace_account_extension_contact_with_http_info(account_id, extension_id, contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int account_id: Account ID (required)
        :param int extension_id: Extension ID (required)
        :param int contact_id: Contact ID (required)
        :param CreateContactParams data: Contact data
        :return: ContactFull
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'extension_id', 'contact_id', 'data']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace_account_extension_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `replace_account_extension_contact`")
        # verify the required parameter 'extension_id' is set
        if ('extension_id' not in params) or (params['extension_id'] is None):
            raise ValueError("Missing the required parameter `extension_id` when calling `replace_account_extension_contact`")
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params) or (params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `replace_account_extension_contact`")


        collection_formats = {}

        resource_path = '/accounts/{account_id}/extensions/{extension_id}/contacts/{contact_id}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']
        if 'extension_id' in params:
            path_params['extension_id'] = params['extension_id']
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']

        query_params = {}

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

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ContactFull',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)