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


class CreateQueueParams(object):
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
        'name': 'str',
        'greeting': 'object',
        'hold_music': 'object',
        'max_hold_time': 'int',
        'caller_id_type': 'str',
        'ring_time': 'int',
        'members': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'greeting': 'greeting',
        'hold_music': 'hold_music',
        'max_hold_time': 'max_hold_time',
        'caller_id_type': 'caller_id_type',
        'ring_time': 'ring_time',
        'members': 'members'
    }

    def __init__(self, name=None, greeting=None, hold_music=None, max_hold_time=None, caller_id_type=None, ring_time=None, members=None):
        """
        CreateQueueParams - a model defined in Swagger
        """

        self._name = None
        self._greeting = None
        self._hold_music = None
        self._max_hold_time = None
        self._caller_id_type = None
        self._ring_time = None
        self._members = None

        if name is not None:
          self.name = name
        if greeting is not None:
          self.greeting = greeting
        if hold_music is not None:
          self.hold_music = hold_music
        if max_hold_time is not None:
          self.max_hold_time = max_hold_time
        if caller_id_type is not None:
          self.caller_id_type = caller_id_type
        if ring_time is not None:
          self.ring_time = ring_time
        if members is not None:
          self.members = members

    @property
    def name(self):
        """
        Gets the name of this CreateQueueParams.
        Name of queue

        :return: The name of this CreateQueueParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateQueueParams.
        Name of queue

        :param name: The name of this CreateQueueParams.
        :type: str
        """

        self._name = name

    @property
    def greeting(self):
        """
        Gets the greeting of this CreateQueueParams.
        Recording lookup object

        :return: The greeting of this CreateQueueParams.
        :rtype: object
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """
        Sets the greeting of this CreateQueueParams.
        Recording lookup object

        :param greeting: The greeting of this CreateQueueParams.
        :type: object
        """

        self._greeting = greeting

    @property
    def hold_music(self):
        """
        Gets the hold_music of this CreateQueueParams.
        Recording lookup object

        :return: The hold_music of this CreateQueueParams.
        :rtype: object
        """
        return self._hold_music

    @hold_music.setter
    def hold_music(self, hold_music):
        """
        Sets the hold_music of this CreateQueueParams.
        Recording lookup object

        :param hold_music: The hold_music of this CreateQueueParams.
        :type: object
        """

        self._hold_music = hold_music

    @property
    def max_hold_time(self):
        """
        Gets the max_hold_time of this CreateQueueParams.
        Max seconds for hold

        :return: The max_hold_time of this CreateQueueParams.
        :rtype: int
        """
        return self._max_hold_time

    @max_hold_time.setter
    def max_hold_time(self, max_hold_time):
        """
        Sets the max_hold_time of this CreateQueueParams.
        Max seconds for hold

        :param max_hold_time: The max_hold_time of this CreateQueueParams.
        :type: int
        """

        self._max_hold_time = max_hold_time

    @property
    def caller_id_type(self):
        """
        Gets the caller_id_type of this CreateQueueParams.
        Type of caller id

        :return: The caller_id_type of this CreateQueueParams.
        :rtype: str
        """
        return self._caller_id_type

    @caller_id_type.setter
    def caller_id_type(self, caller_id_type):
        """
        Sets the caller_id_type of this CreateQueueParams.
        Type of caller id

        :param caller_id_type: The caller_id_type of this CreateQueueParams.
        :type: str
        """

        self._caller_id_type = caller_id_type

    @property
    def ring_time(self):
        """
        Gets the ring_time of this CreateQueueParams.
        Number of seconds to ring each member

        :return: The ring_time of this CreateQueueParams.
        :rtype: int
        """
        return self._ring_time

    @ring_time.setter
    def ring_time(self, ring_time):
        """
        Sets the ring_time of this CreateQueueParams.
        Number of seconds to ring each member

        :param ring_time: The ring_time of this CreateQueueParams.
        :type: int
        """

        self._ring_time = ring_time

    @property
    def members(self):
        """
        Gets the members of this CreateQueueParams.
        Extensions or phone numbers

        :return: The members of this CreateQueueParams.
        :rtype: list[object]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this CreateQueueParams.
        Extensions or phone numbers

        :param members: The members of this CreateQueueParams.
        :type: list[object]
        """

        self._members = members

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
        if not isinstance(other, CreateQueueParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
