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


class CreateOauthParams(object):
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
        'grant_type': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'code': 'str',
        'redirect_uri': 'str',
        'scope': 'str',
        'username': 'str',
        'password': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'code': 'code',
        'redirect_uri': 'redirect_uri',
        'scope': 'scope',
        'username': 'username',
        'password': 'password',
        'refresh_token': 'refresh_token'
    }

    def __init__(self, grant_type=None, client_id=None, client_secret=None, code=None, redirect_uri=None, scope=None, username=None, password=None, refresh_token=None):
        """
        CreateOauthParams - a model defined in Swagger
        """

        self._grant_type = None
        self._client_id = None
        self._client_secret = None
        self._code = None
        self._redirect_uri = None
        self._scope = None
        self._username = None
        self._password = None
        self._refresh_token = None

        if grant_type is not None:
          self.grant_type = grant_type
        if client_id is not None:
          self.client_id = client_id
        if client_secret is not None:
          self.client_secret = client_secret
        if code is not None:
          self.code = code
        if redirect_uri is not None:
          self.redirect_uri = redirect_uri
        if scope is not None:
          self.scope = scope
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password
        if refresh_token is not None:
          self.refresh_token = refresh_token

    @property
    def grant_type(self):
        """
        Gets the grant_type of this CreateOauthParams.
        authorization_code, client_credentials, password or refresh_token

        :return: The grant_type of this CreateOauthParams.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """
        Sets the grant_type of this CreateOauthParams.
        authorization_code, client_credentials, password or refresh_token

        :param grant_type: The grant_type of this CreateOauthParams.
        :type: str
        """

        self._grant_type = grant_type

    @property
    def client_id(self):
        """
        Gets the client_id of this CreateOauthParams.
        Client ID

        :return: The client_id of this CreateOauthParams.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateOauthParams.
        Client ID

        :param client_id: The client_id of this CreateOauthParams.
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this CreateOauthParams.
        Client Secret Key

        :return: The client_secret of this CreateOauthParams.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this CreateOauthParams.
        Client Secret Key

        :param client_secret: The client_secret of this CreateOauthParams.
        :type: str
        """

        self._client_secret = client_secret

    @property
    def code(self):
        """
        Gets the code of this CreateOauthParams.
        Authorization Code created via the /oauth/authorization API

        :return: The code of this CreateOauthParams.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CreateOauthParams.
        Authorization Code created via the /oauth/authorization API

        :param code: The code of this CreateOauthParams.
        :type: str
        """

        self._code = code

    @property
    def redirect_uri(self):
        """
        Gets the redirect_uri of this CreateOauthParams.
        The redirect URI where user enters authentication information

        :return: The redirect_uri of this CreateOauthParams.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """
        Sets the redirect_uri of this CreateOauthParams.
        The redirect URI where user enters authentication information

        :param redirect_uri: The redirect_uri of this CreateOauthParams.
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def scope(self):
        """
        Gets the scope of this CreateOauthParams.
        account-owner, extension-user and/or methods:ALL, separated by space (%20)

        :return: The scope of this CreateOauthParams.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CreateOauthParams.
        account-owner, extension-user and/or methods:ALL, separated by space (%20)

        :param scope: The scope of this CreateOauthParams.
        :type: str
        """

        self._scope = scope

    @property
    def username(self):
        """
        Gets the username of this CreateOauthParams.
        User name

        :return: The username of this CreateOauthParams.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateOauthParams.
        User name

        :param username: The username of this CreateOauthParams.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this CreateOauthParams.
        Password

        :return: The password of this CreateOauthParams.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateOauthParams.
        Password

        :param password: The password of this CreateOauthParams.
        :type: str
        """

        self._password = password

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this CreateOauthParams.
        Refresh token

        :return: The refresh_token of this CreateOauthParams.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this CreateOauthParams.
        Refresh token

        :param refresh_token: The refresh_token of this CreateOauthParams.
        :type: str
        """

        self._refresh_token = refresh_token

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
        if not isinstance(other, CreateOauthParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
