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
from swagger_client.apis.trunks_api import TrunksApi


class TestTrunksApi(unittest.TestCase):
    """ TrunksApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.trunks_api.TrunksApi()

    def tearDown(self):
        pass

    def test_create_account_trunk(self):
        """
        Test case for create_account_trunk

        Add a trunk record with SIP information.
        """
        pass

    def test_delete_account_trunk(self):
        """
        Test case for delete_account_trunk

        Delete a trunk from account.
        """
        pass

    def test_get_account_trunk(self):
        """
        Test case for get_account_trunk

        Show details of an individual trunk.
        """
        pass

    def test_list_account_trunks(self):
        """
        Test case for list_account_trunks

        Get a list of trunks for an account.
        """
        pass

    def test_replace_account_trunk(self):
        """
        Test case for replace_account_trunk

        Replace parameters in a trunk.
        """
        pass


if __name__ == '__main__':
    unittest.main()
