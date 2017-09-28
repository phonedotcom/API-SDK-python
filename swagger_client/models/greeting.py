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


class Greeting(object):
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
        'type': 'str',
        'alternate': 'MediaSummary',
        'standard': 'MediaSummary',
        'enable_leave_message_prompt': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'alternate': 'alternate',
        'standard': 'standard',
        'enable_leave_message_prompt': 'enable_leave_message_prompt'
    }

    def __init__(self, type=None, alternate=None, standard=None, enable_leave_message_prompt=None):
        """
        Greeting - a model defined in Swagger
        """

        self._type = None
        self._alternate = None
        self._standard = None
        self._enable_leave_message_prompt = None

        if type is not None:
          self.type = type
        if alternate is not None:
          self.alternate = alternate
        if standard is not None:
          self.standard = standard
        if enable_leave_message_prompt is not None:
          self.enable_leave_message_prompt = enable_leave_message_prompt

    @property
    def type(self):
        """
        Gets the type of this Greeting.
        The greeting to play. Can be \"name\" for the name_greeting as described above, \"standard\" for the standard greeting, or \"alternate\" for an alternate greeting. See below for details.

        :return: The type of this Greeting.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Greeting.
        The greeting to play. Can be \"name\" for the name_greeting as described above, \"standard\" for the standard greeting, or \"alternate\" for an alternate greeting. See below for details.

        :param type: The type of this Greeting.
        :type: str
        """

        self._type = type

    @property
    def alternate(self):
        """
        Gets the alternate of this Greeting.
        Greeting to be played when type=\"alternate\". Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :return: The alternate of this Greeting.
        :rtype: MediaSummary
        """
        return self._alternate

    @alternate.setter
    def alternate(self, alternate):
        """
        Sets the alternate of this Greeting.
        Greeting to be played when type=\"alternate\". Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :param alternate: The alternate of this Greeting.
        :type: MediaSummary
        """

        self._alternate = alternate

    @property
    def standard(self):
        """
        Gets the standard of this Greeting.
        Greeting to be played when type=\"standard\". Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :return: The standard of this Greeting.
        :rtype: MediaSummary
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """
        Sets the standard of this Greeting.
        Greeting to be played when type=\"standard\". Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :param standard: The standard of this Greeting.
        :type: MediaSummary
        """

        self._standard = standard

    @property
    def enable_leave_message_prompt(self):
        """
        Gets the enable_leave_message_prompt of this Greeting.
        Whether to prompt the caller with the following words after the voicemail greeting has been played: \"Please leave your message after the tone. When finished, hang up or press the pound key.\" Boolean.

        :return: The enable_leave_message_prompt of this Greeting.
        :rtype: bool
        """
        return self._enable_leave_message_prompt

    @enable_leave_message_prompt.setter
    def enable_leave_message_prompt(self, enable_leave_message_prompt):
        """
        Sets the enable_leave_message_prompt of this Greeting.
        Whether to prompt the caller with the following words after the voicemail greeting has been played: \"Please leave your message after the tone. When finished, hang up or press the pound key.\" Boolean.

        :param enable_leave_message_prompt: The enable_leave_message_prompt of this Greeting.
        :type: bool
        """

        self._enable_leave_message_prompt = enable_leave_message_prompt

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
        if not isinstance(other, Greeting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
