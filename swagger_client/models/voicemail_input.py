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


class VoicemailInput(object):
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
        'enabled': 'str',
        'password': 'str',
        'greeting': 'GreetingInput',
        'attachments': 'str',
        'notifications': 'Notification',
        'transcription': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'password': 'password',
        'greeting': 'greeting',
        'attachments': 'attachments',
        'notifications': 'notifications',
        'transcription': 'transcription'
    }

    def __init__(self, enabled=None, password=None, greeting=None, attachments=None, notifications=None, transcription=None):
        """
        VoicemailInput - a model defined in Swagger
        """

        self._enabled = None
        self._password = None
        self._greeting = None
        self._attachments = None
        self._notifications = None
        self._transcription = None

        if enabled is not None:
          self.enabled = enabled
        if password is not None:
          self.password = password
        if greeting is not None:
          self.greeting = greeting
        if attachments is not None:
          self.attachments = attachments
        if notifications is not None:
          self.notifications = notifications
        if transcription is not None:
          self.transcription = transcription

    @property
    def enabled(self):
        """
        Gets the enabled of this VoicemailInput.
        Whether voicemail is enabled. Boolean.

        :return: The enabled of this VoicemailInput.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VoicemailInput.
        Whether voicemail is enabled. Boolean.

        :param enabled: The enabled of this VoicemailInput.
        :type: str
        """

        self._enabled = enabled

    @property
    def password(self):
        """
        Gets the password of this VoicemailInput.
        Password for accessing voicemail box. Must be digits only.

        :return: The password of this VoicemailInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this VoicemailInput.
        Password for accessing voicemail box. Must be digits only.

        :param password: The password of this VoicemailInput.
        :type: str
        """

        self._password = password

    @property
    def greeting(self):
        """
        Gets the greeting of this VoicemailInput.

        :return: The greeting of this VoicemailInput.
        :rtype: GreetingInput
        """
        return self._greeting

    @greeting.setter
    def greeting(self, greeting):
        """
        Sets the greeting of this VoicemailInput.

        :param greeting: The greeting of this VoicemailInput.
        :type: GreetingInput
        """

        self._greeting = greeting

    @property
    def attachments(self):
        """
        Gets the attachments of this VoicemailInput.
        If notification emails are being used, this defines the format of the audio attachments. Can be \"wav\" for WAV format, \"mp3\" for MP3 format, or NULL to disable attachments.

        :return: The attachments of this VoicemailInput.
        :rtype: str
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this VoicemailInput.
        If notification emails are being used, this defines the format of the audio attachments. Can be \"wav\" for WAV format, \"mp3\" for MP3 format, or NULL to disable attachments.

        :param attachments: The attachments of this VoicemailInput.
        :type: str
        """

        self._attachments = attachments

    @property
    def notifications(self):
        """
        Gets the notifications of this VoicemailInput.
        Voicemail Notifications Object. See below for details. Can be set to NULL to disable notifications.

        :return: The notifications of this VoicemailInput.
        :rtype: Notification
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """
        Sets the notifications of this VoicemailInput.
        Voicemail Notifications Object. See below for details. Can be set to NULL to disable notifications.

        :param notifications: The notifications of this VoicemailInput.
        :type: Notification
        """

        self._notifications = notifications

    @property
    def transcription(self):
        """
        Gets the transcription of this VoicemailInput.
        Type of voicemail transcription to use. Can be \"human\" for high-quality manual transcriptions by human operators, \"automated\" for machine-generated transcriptions, or NULL to omit trancriptions. Changing this option will affect your monthly bill. Please see our Control Panel or contact Customer Service for details.

        :return: The transcription of this VoicemailInput.
        :rtype: str
        """
        return self._transcription

    @transcription.setter
    def transcription(self, transcription):
        """
        Sets the transcription of this VoicemailInput.
        Type of voicemail transcription to use. Can be \"human\" for high-quality manual transcriptions by human operators, \"automated\" for machine-generated transcriptions, or NULL to omit trancriptions. Changing this option will affect your monthly bill. Please see our Control Panel or contact Customer Service for details.

        :param transcription: The transcription of this VoicemailInput.
        :type: str
        """

        self._transcription = transcription

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
        if not isinstance(other, VoicemailInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
