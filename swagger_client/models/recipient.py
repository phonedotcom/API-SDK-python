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


class Recipient(object):
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
        'status': 'str'
    }

    attribute_map = {
        'number': 'number',
        'status': 'status'
    }

    def __init__(self, number=None, status=None):
        """
        Recipient - a model defined in Swagger
        """

        self._number = None
        self._status = None

        if number is not None:
          self.number = number
        if status is not None:
          self.status = status

    @property
    def number(self):
        """
        Gets the number of this Recipient.
        Phone number that will receive the SMS message

        :return: The number of this Recipient.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Recipient.
        Phone number that will receive the SMS message

        :param number: The number of this Recipient.
        :type: str
        """

        self._number = number

    @property
    def status(self):
        """
        Gets the status of this Recipient.
        Indicate the status of your SMS object. May be 'sent', 'received', 'queued', 'new' ...

        :return: The status of this Recipient.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Recipient.
        Indicate the status of your SMS object. May be 'sent', 'received', 'queued', 'new' ...

        :param status: The status of this Recipient.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, Recipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
