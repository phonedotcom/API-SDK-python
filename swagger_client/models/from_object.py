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


class FromObject(object):
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
        'number': 'str',
        'name': 'str',
        'city': 'str',
        'state': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        'city': 'city',
        'state': 'state'
    }

    def __init__(self, number=None, name=None, city=None, state=None):
        """
        FromObject - a model defined in Swagger
        """

        self._number = None
        self._name = None
        self._city = None
        self._state = None

        if number is not None:
          self.number = number
        if name is not None:
          self.name = name
        if city is not None:
          self.city = city
        if state is not None:
          self.state = state

    @property
    def number(self):
        """
        Gets the number of this FromObject.
        The caller phone number

        :return: The number of this FromObject.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this FromObject.
        The caller phone number

        :param number: The number of this FromObject.
        :type: str
        """

        self._number = number

    @property
    def name(self):
        """
        Gets the name of this FromObject.
        The name / caller ID of the caller

        :return: The name of this FromObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FromObject.
        The name / caller ID of the caller

        :param name: The name of this FromObject.
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """
        Gets the city of this FromObject.
        The city where the caller is from

        :return: The city of this FromObject.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this FromObject.
        The city where the caller is from

        :param city: The city of this FromObject.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this FromObject.
        The state where the caller is from

        :return: The state of this FromObject.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this FromObject.
        The state where the caller is from

        :param state: The state of this FromObject.
        :type: str
        """

        self._state = state

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
        if not isinstance(other, FromObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
