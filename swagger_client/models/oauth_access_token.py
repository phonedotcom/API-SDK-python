# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OauthAccessToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'token_type': 'str',
        'scope': 'str',
        'refresh_token': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'scope': 'scope',
        'refresh_token': 'refresh_token',
        'expires_in': 'expires_in'
    }

    def __init__(self, access_token=None, token_type=None, scope=None, refresh_token=None, expires_in=None):
        """
        OauthAccessToken - a model defined in Swagger
        """

        self._access_token = None
        self._token_type = None
        self._scope = None
        self._refresh_token = None
        self._expires_in = None

        if access_token is not None:
          self.access_token = access_token
        if token_type is not None:
          self.token_type = token_type
        if scope is not None:
          self.scope = scope
        if refresh_token is not None:
          self.refresh_token = refresh_token
        if expires_in is not None:
          self.expires_in = expires_in

    @property
    def access_token(self):
        """
        Gets the access_token of this OauthAccessToken.

        :return: The access_token of this OauthAccessToken.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this OauthAccessToken.

        :param access_token: The access_token of this OauthAccessToken.
        :type: str
        """

        self._access_token = access_token

    @property
    def token_type(self):
        """
        Gets the token_type of this OauthAccessToken.

        :return: The token_type of this OauthAccessToken.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this OauthAccessToken.

        :param token_type: The token_type of this OauthAccessToken.
        :type: str
        """

        self._token_type = token_type

    @property
    def scope(self):
        """
        Gets the scope of this OauthAccessToken.

        :return: The scope of this OauthAccessToken.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this OauthAccessToken.

        :param scope: The scope of this OauthAccessToken.
        :type: str
        """

        self._scope = scope

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this OauthAccessToken.

        :return: The refresh_token of this OauthAccessToken.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this OauthAccessToken.

        :param refresh_token: The refresh_token of this OauthAccessToken.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def expires_in(self):
        """
        Gets the expires_in of this OauthAccessToken.

        :return: The expires_in of this OauthAccessToken.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this OauthAccessToken.

        :param expires_in: The expires_in of this OauthAccessToken.
        :type: int
        """

        self._expires_in = expires_in

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, OauthAccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
