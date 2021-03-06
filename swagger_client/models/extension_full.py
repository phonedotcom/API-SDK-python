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


class ExtensionFull(object):
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
        'extension': 'int',
        'voip_id': 'int',
        'full_name': 'str',
        'usage_type': 'str',
        'device_membership': 'DeviceMembership',
        'timezone': 'str',
        'name_greeting': 'MediaSummary',
        'include_in_directory': 'bool',
        'caller_id': 'str',
        'local_area_code': 'str',
        'enable_call_waiting': 'bool',
        'enable_outbound_calls': 'bool',
        'voicemail': 'Voicemail',
        'call_notifications': 'Notification',
        'route': 'RouteSummary'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'extension': 'extension',
        'voip_id': 'voip_id',
        'full_name': 'full_name',
        'usage_type': 'usage_type',
        'device_membership': 'device_membership',
        'timezone': 'timezone',
        'name_greeting': 'name_greeting',
        'include_in_directory': 'include_in_directory',
        'caller_id': 'caller_id',
        'local_area_code': 'local_area_code',
        'enable_call_waiting': 'enable_call_waiting',
        'enable_outbound_calls': 'enable_outbound_calls',
        'voicemail': 'voicemail',
        'call_notifications': 'call_notifications',
        'route': 'route'
    }

    def __init__(self, id=None, name=None, extension=None, voip_id=None, full_name=None, usage_type=None, device_membership=None, timezone=None, name_greeting=None, include_in_directory=None, caller_id=None, local_area_code=None, enable_call_waiting=None, enable_outbound_calls=None, voicemail=None, call_notifications=None, route=None):
        """
        ExtensionFull - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._extension = None
        self._voip_id = None
        self._full_name = None
        self._usage_type = None
        self._device_membership = None
        self._timezone = None
        self._name_greeting = None
        self._include_in_directory = None
        self._caller_id = None
        self._local_area_code = None
        self._enable_call_waiting = None
        self._enable_outbound_calls = None
        self._voicemail = None
        self._call_notifications = None
        self._route = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if extension is not None:
          self.extension = extension
        if voip_id is not None:
          self.voip_id = voip_id
        if full_name is not None:
          self.full_name = full_name
        if usage_type is not None:
          self.usage_type = usage_type
        if device_membership is not None:
          self.device_membership = device_membership
        if timezone is not None:
          self.timezone = timezone
        if name_greeting is not None:
          self.name_greeting = name_greeting
        if include_in_directory is not None:
          self.include_in_directory = include_in_directory
        if caller_id is not None:
          self.caller_id = caller_id
        if local_area_code is not None:
          self.local_area_code = local_area_code
        if enable_call_waiting is not None:
          self.enable_call_waiting = enable_call_waiting
        if enable_outbound_calls is not None:
          self.enable_outbound_calls = enable_outbound_calls
        if voicemail is not None:
          self.voicemail = voicemail
        if call_notifications is not None:
          self.call_notifications = call_notifications
        if route is not None:
          self.route = route

    @property
    def id(self):
        """
        Gets the id of this ExtensionFull.
        ID of the extension. This is the internal Phone.com ID, not the extension number callers may dial.

        :return: The id of this ExtensionFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExtensionFull.
        ID of the extension. This is the internal Phone.com ID, not the extension number callers may dial.

        :param id: The id of this ExtensionFull.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ExtensionFull.
        User-supplied name for the extension. On POST, leaving this empty will result in an auto-generated value. On PUT, this field is required.

        :return: The name of this ExtensionFull.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExtensionFull.
        User-supplied name for the extension. On POST, leaving this empty will result in an auto-generated value. On PUT, this field is required.

        :param name: The name of this ExtensionFull.
        :type: str
        """

        self._name = name

    @property
    def extension(self):
        """
        Gets the extension of this ExtensionFull.
        Extension number that callers may dial. On POST, leaving this empty will result in an auto-generated value. On PUT, this field is required.

        :return: The extension of this ExtensionFull.
        :rtype: int
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this ExtensionFull.
        Extension number that callers may dial. On POST, leaving this empty will result in an auto-generated value. On PUT, this field is required.

        :param extension: The extension of this ExtensionFull.
        :type: int
        """

        self._extension = extension

    @property
    def voip_id(self):
        """
        Gets the voip_id of this ExtensionFull.
        API Account ID. Optional, object may return the voip_id.

        :return: The voip_id of this ExtensionFull.
        :rtype: int
        """
        return self._voip_id

    @voip_id.setter
    def voip_id(self, voip_id):
        """
        Sets the voip_id of this ExtensionFull.
        API Account ID. Optional, object may return the voip_id.

        :param voip_id: The voip_id of this ExtensionFull.
        :type: int
        """

        self._voip_id = voip_id

    @property
    def full_name(self):
        """
        Gets the full_name of this ExtensionFull.
        Full name of the individual or department to which this extension is assigned

        :return: The full_name of this ExtensionFull.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this ExtensionFull.
        Full name of the individual or department to which this extension is assigned

        :param full_name: The full_name of this ExtensionFull.
        :type: str
        """

        self._full_name = full_name

    @property
    def usage_type(self):
        """
        Gets the usage_type of this ExtensionFull.
        Can be \"limited\" or \"unlimited\". In most cases, changing this will affect your monthly bill. Please see our Control Panel or contact Customer Service for pricing.

        :return: The usage_type of this ExtensionFull.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """
        Sets the usage_type of this ExtensionFull.
        Can be \"limited\" or \"unlimited\". In most cases, changing this will affect your monthly bill. Please see our Control Panel or contact Customer Service for pricing.

        :param usage_type: The usage_type of this ExtensionFull.
        :type: str
        """

        self._usage_type = usage_type

    @property
    def device_membership(self):
        """
        Gets the device_membership of this ExtensionFull.

        :return: The device_membership of this ExtensionFull.
        :rtype: DeviceMembership
        """
        return self._device_membership

    @device_membership.setter
    def device_membership(self, device_membership):
        """
        Sets the device_membership of this ExtensionFull.

        :param device_membership: The device_membership of this ExtensionFull.
        :type: DeviceMembership
        """

        self._device_membership = device_membership

    @property
    def timezone(self):
        """
        Gets the timezone of this ExtensionFull.
        Time zone. Can be in any commonly recognized format, such as \"America/Los_Angeles\".

        :return: The timezone of this ExtensionFull.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ExtensionFull.
        Time zone. Can be in any commonly recognized format, such as \"America/Los_Angeles\".

        :param timezone: The timezone of this ExtensionFull.
        :type: str
        """

        self._timezone = timezone

    @property
    def name_greeting(self):
        """
        Gets the name_greeting of this ExtensionFull.
        Greeting that communicates the extension's name. Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :return: The name_greeting of this ExtensionFull.
        :rtype: MediaSummary
        """
        return self._name_greeting

    @name_greeting.setter
    def name_greeting(self, name_greeting):
        """
        Sets the name_greeting of this ExtensionFull.
        Greeting that communicates the extension's name. Output is a Greeting Summary Object. Input must be a Greeting Lookup Object.

        :param name_greeting: The name_greeting of this ExtensionFull.
        :type: MediaSummary
        """

        self._name_greeting = name_greeting

    @property
    def include_in_directory(self):
        """
        Gets the include_in_directory of this ExtensionFull.
        Whether this extension should be included in the dial-by-name directory for this account. Boolean.

        :return: The include_in_directory of this ExtensionFull.
        :rtype: bool
        """
        return self._include_in_directory

    @include_in_directory.setter
    def include_in_directory(self, include_in_directory):
        """
        Sets the include_in_directory of this ExtensionFull.
        Whether this extension should be included in the dial-by-name directory for this account. Boolean.

        :param include_in_directory: The include_in_directory of this ExtensionFull.
        :type: bool
        """

        self._include_in_directory = include_in_directory

    @property
    def caller_id(self):
        """
        Gets the caller_id of this ExtensionFull.
        Phone number to use as Caller ID for outgoing calls. Must be a phone number belonging to this account, or one of any additional authorized phone numbers. You can use our List Caller Ids service to see a current list. To unassign, you may set this to \"private\", NULL, or an empty string.

        :return: The caller_id of this ExtensionFull.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id):
        """
        Sets the caller_id of this ExtensionFull.
        Phone number to use as Caller ID for outgoing calls. Must be a phone number belonging to this account, or one of any additional authorized phone numbers. You can use our List Caller Ids service to see a current list. To unassign, you may set this to \"private\", NULL, or an empty string.

        :param caller_id: The caller_id of this ExtensionFull.
        :type: str
        """

        self._caller_id = caller_id

    @property
    def local_area_code(self):
        """
        Gets the local_area_code of this ExtensionFull.
        For outbound calls, this is the North American area code that this extension is calling from.

        :return: The local_area_code of this ExtensionFull.
        :rtype: str
        """
        return self._local_area_code

    @local_area_code.setter
    def local_area_code(self, local_area_code):
        """
        Sets the local_area_code of this ExtensionFull.
        For outbound calls, this is the North American area code that this extension is calling from.

        :param local_area_code: The local_area_code of this ExtensionFull.
        :type: str
        """

        self._local_area_code = local_area_code

    @property
    def enable_call_waiting(self):
        """
        Gets the enable_call_waiting of this ExtensionFull.
        Whether Call Waiting is enabled. Boolean. Default is TRUE.

        :return: The enable_call_waiting of this ExtensionFull.
        :rtype: bool
        """
        return self._enable_call_waiting

    @enable_call_waiting.setter
    def enable_call_waiting(self, enable_call_waiting):
        """
        Sets the enable_call_waiting of this ExtensionFull.
        Whether Call Waiting is enabled. Boolean. Default is TRUE.

        :param enable_call_waiting: The enable_call_waiting of this ExtensionFull.
        :type: bool
        """

        self._enable_call_waiting = enable_call_waiting

    @property
    def enable_outbound_calls(self):
        """
        Gets the enable_outbound_calls of this ExtensionFull.
        Whether outgoing calls are enabled. Boolean. Default is TRUE.

        :return: The enable_outbound_calls of this ExtensionFull.
        :rtype: bool
        """
        return self._enable_outbound_calls

    @enable_outbound_calls.setter
    def enable_outbound_calls(self, enable_outbound_calls):
        """
        Sets the enable_outbound_calls of this ExtensionFull.
        Whether outgoing calls are enabled. Boolean. Default is TRUE.

        :param enable_outbound_calls: The enable_outbound_calls of this ExtensionFull.
        :type: bool
        """

        self._enable_outbound_calls = enable_outbound_calls

    @property
    def voicemail(self):
        """
        Gets the voicemail of this ExtensionFull.

        :return: The voicemail of this ExtensionFull.
        :rtype: Voicemail
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """
        Sets the voicemail of this ExtensionFull.

        :param voicemail: The voicemail of this ExtensionFull.
        :type: Voicemail
        """

        self._voicemail = voicemail

    @property
    def call_notifications(self):
        """
        Gets the call_notifications of this ExtensionFull.

        :return: The call_notifications of this ExtensionFull.
        :rtype: Notification
        """
        return self._call_notifications

    @call_notifications.setter
    def call_notifications(self, call_notifications):
        """
        Sets the call_notifications of this ExtensionFull.

        :param call_notifications: The call_notifications of this ExtensionFull.
        :type: Notification
        """

        self._call_notifications = call_notifications

    @property
    def route(self):
        """
        Gets the route of this ExtensionFull.
        Route which will handle incoming voice and fax calls. Only valid on PUT requests, not POST. Output is a Route Summary Object if the route is named, otherwise the Full Route Object will be shown. Input must be a Route Lookup Object pointing to a named route. Route must belong to this extension already.

        :return: The route of this ExtensionFull.
        :rtype: RouteSummary
        """
        return self._route

    @route.setter
    def route(self, route):
        """
        Sets the route of this ExtensionFull.
        Route which will handle incoming voice and fax calls. Only valid on PUT requests, not POST. Output is a Route Summary Object if the route is named, otherwise the Full Route Object will be shown. Input must be a Route Lookup Object pointing to a named route. Route must belong to this extension already.

        :param route: The route of this ExtensionFull.
        :type: RouteSummary
        """

        self._route = route

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
        if not isinstance(other, ExtensionFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
