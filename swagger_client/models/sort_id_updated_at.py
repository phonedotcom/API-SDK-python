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


class SortIdUpdatedAt(object):
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
        'id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, updated_at=None):
        """
        SortIdUpdatedAt - a model defined in Swagger
        """

        self._id = None
        self._updated_at = None

        if id is not None:
          self.id = id
        if updated_at is not None:
          self.updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this SortIdUpdatedAt.

        :return: The id of this SortIdUpdatedAt.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SortIdUpdatedAt.

        :param id: The id of this SortIdUpdatedAt.
        :type: str
        """

        self._id = id

    @property
    def updated_at(self):
        """
        Gets the updated_at of this SortIdUpdatedAt.

        :return: The updated_at of this SortIdUpdatedAt.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this SortIdUpdatedAt.

        :param updated_at: The updated_at of this SortIdUpdatedAt.
        :type: str
        """

        self._updated_at = updated_at

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
        if not isinstance(other, SortIdUpdatedAt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
