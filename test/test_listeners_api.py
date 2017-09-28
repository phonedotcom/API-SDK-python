# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.listeners_api import ListenersApi


class TestListenersApi(unittest.TestCase):
    """ ListenersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.listeners_api.ListenersApi()

    def tearDown(self):
        pass

    def test_create_account_listener(self):
        """
        Test case for create_account_listener

        Add a listener object to your account that can be used to subscribe an event.
        """
        pass

    def test_delete_account_listener(self):
        """
        Test case for delete_account_listener

        Delete an individual event listener.
        """
        pass

    def test_get_account_listener(self):
        """
        Test case for get_account_listener

        Show details of an individual listener.
        """
        pass

    def test_list_account_listeners(self):
        """
        Test case for list_account_listeners

        Get a list of listeners for an account.
        """
        pass

    def test_replace_account_listener(self):
        """
        Test case for replace_account_listener

        Update the settings of an individual event listener.
        """
        pass


if __name__ == '__main__':
    unittest.main()
