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


class DeviceFull(object):
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
        'id': 'int',
        'name': 'str',
        'sip_authentication': 'SipAuthentication',
        'lines': 'list[Line]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'sip_authentication': 'sip_authentication',
        'lines': 'lines'
    }

    def __init__(self, id=None, name=None, sip_authentication=None, lines=None):
        """
        DeviceFull - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._sip_authentication = None
        self._lines = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if sip_authentication is not None:
          self.sip_authentication = sip_authentication
        if lines is not None:
          self.lines = lines

    @property
    def id(self):
        """
        Gets the id of this DeviceFull.
        ID

        :return: The id of this DeviceFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceFull.
        ID

        :param id: The id of this DeviceFull.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DeviceFull.
        User-supplied name, otherwise NULL

        :return: The name of this DeviceFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceFull.
        User-supplied name, otherwise NULL

        :param name: The name of this DeviceFull.
        :type: str
        """

        self._name = name

    @property
    def sip_authentication(self):
        """
        Gets the sip_authentication of this DeviceFull.

        :return: The sip_authentication of this DeviceFull.
        :rtype: SipAuthentication
        """
        return self._sip_authentication

    @sip_authentication.setter
    def sip_authentication(self, sip_authentication):
        """
        Sets the sip_authentication of this DeviceFull.

        :param sip_authentication: The sip_authentication of this DeviceFull.
        :type: SipAuthentication
        """

        self._sip_authentication = sip_authentication

    @property
    def lines(self):
        """
        Gets the lines of this DeviceFull.
        Array of Line Objects showing which extensions are attached to this device, and their assigned line numbers. See below for details.

        :return: The lines of this DeviceFull.
        :rtype: list[Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this DeviceFull.
        Array of Line Objects showing which extensions are attached to this device, and their assigned line numbers. See below for details.

        :param lines: The lines of this DeviceFull.
        :type: list[Line]
        """

        self._lines = lines

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
        if not isinstance(other, DeviceFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
