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


class AvailableNumbersFull(object):
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
        'phone_number': 'str',
        'formatted': 'str',
        'price': 'int',
        'is_toll_free': 'bool',
        'country_code': 'str',
        'npa': 'str',
        'nxx': 'str',
        'xxxx': 'str',
        'city': 'str',
        'province': 'str',
        'country': 'str'
    }

    attribute_map = {
        'phone_number': 'phone_number',
        'formatted': 'formatted',
        'price': 'price',
        'is_toll_free': 'is_toll_free',
        'country_code': 'country_code',
        'npa': 'npa',
        'nxx': 'nxx',
        'xxxx': 'xxxx',
        'city': 'city',
        'province': 'province',
        'country': 'country'
    }

    def __init__(self, phone_number=None, formatted=None, price=None, is_toll_free=None, country_code=None, npa=None, nxx=None, xxxx=None, city=None, province=None, country=None):
        """
        AvailableNumbersFull - a model defined in Swagger
        """

        self._phone_number = None
        self._formatted = None
        self._price = None
        self._is_toll_free = None
        self._country_code = None
        self._npa = None
        self._nxx = None
        self._xxxx = None
        self._city = None
        self._province = None
        self._country = None

        if phone_number is not None:
          self.phone_number = phone_number
        if formatted is not None:
          self.formatted = formatted
        if price is not None:
          self.price = price
        if is_toll_free is not None:
          self.is_toll_free = is_toll_free
        if country_code is not None:
          self.country_code = country_code
        if npa is not None:
          self.npa = npa
        if nxx is not None:
          self.nxx = nxx
        if xxxx is not None:
          self.xxxx = xxxx
        if city is not None:
          self.city = city
        if province is not None:
          self.province = province
        if country is not None:
          self.country = country

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AvailableNumbersFull.
        Phone number, in E.164 format

        :return: The phone_number of this AvailableNumbersFull.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AvailableNumbersFull.
        Phone number, in E.164 format

        :param phone_number: The phone_number of this AvailableNumbersFull.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def formatted(self):
        """
        Gets the formatted of this AvailableNumbersFull.
        Human-readable formatted version of the phone number

        :return: The formatted of this AvailableNumbersFull.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """
        Sets the formatted of this AvailableNumbersFull.
        Human-readable formatted version of the phone number

        :param formatted: The formatted of this AvailableNumbersFull.
        :type: str
        """

        self._formatted = formatted

    @property
    def price(self):
        """
        Gets the price of this AvailableNumbersFull.
        The one-time initial price for this number, in USD. Some numbers show REQUEST_QUOTE here. Please contact our sales department if you are interested in these numbers.

        :return: The price of this AvailableNumbersFull.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this AvailableNumbersFull.
        The one-time initial price for this number, in USD. Some numbers show REQUEST_QUOTE here. Please contact our sales department if you are interested in these numbers.

        :param price: The price of this AvailableNumbersFull.
        :type: int
        """

        self._price = price

    @property
    def is_toll_free(self):
        """
        Gets the is_toll_free of this AvailableNumbersFull.
        Whether the number is toll-free

        :return: The is_toll_free of this AvailableNumbersFull.
        :rtype: bool
        """
        return self._is_toll_free

    @is_toll_free.setter
    def is_toll_free(self, is_toll_free):
        """
        Sets the is_toll_free of this AvailableNumbersFull.
        Whether the number is toll-free

        :param is_toll_free: The is_toll_free of this AvailableNumbersFull.
        :type: bool
        """

        self._is_toll_free = is_toll_free

    @property
    def country_code(self):
        """
        Gets the country_code of this AvailableNumbersFull.
        The international dialing prefix for this number. For US and Canadian numbers, for example, this will be \"1\".

        :return: The country_code of this AvailableNumbersFull.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this AvailableNumbersFull.
        The international dialing prefix for this number. For US and Canadian numbers, for example, this will be \"1\".

        :param country_code: The country_code of this AvailableNumbersFull.
        :type: str
        """

        self._country_code = country_code

    @property
    def npa(self):
        """
        Gets the npa of this AvailableNumbersFull.
        Area code (a.k.a. NPA). Included for North American numbers only.

        :return: The npa of this AvailableNumbersFull.
        :rtype: str
        """
        return self._npa

    @npa.setter
    def npa(self, npa):
        """
        Sets the npa of this AvailableNumbersFull.
        Area code (a.k.a. NPA). Included for North American numbers only.

        :param npa: The npa of this AvailableNumbersFull.
        :type: str
        """

        self._npa = npa

    @property
    def nxx(self):
        """
        Gets the nxx of this AvailableNumbersFull.
        Second 3 digits (a.k.a. NXX). Included for North American numbers only.

        :return: The nxx of this AvailableNumbersFull.
        :rtype: str
        """
        return self._nxx

    @nxx.setter
    def nxx(self, nxx):
        """
        Sets the nxx of this AvailableNumbersFull.
        Second 3 digits (a.k.a. NXX). Included for North American numbers only.

        :param nxx: The nxx of this AvailableNumbersFull.
        :type: str
        """

        self._nxx = nxx

    @property
    def xxxx(self):
        """
        Gets the xxxx of this AvailableNumbersFull.
        Last 4 digits (a.k.a. XXXX). Included for North American numbers only.

        :return: The xxxx of this AvailableNumbersFull.
        :rtype: str
        """
        return self._xxxx

    @xxxx.setter
    def xxxx(self, xxxx):
        """
        Sets the xxxx of this AvailableNumbersFull.
        Last 4 digits (a.k.a. XXXX). Included for North American numbers only.

        :param xxxx: The xxxx of this AvailableNumbersFull.
        :type: str
        """

        self._xxxx = xxxx

    @property
    def city(self):
        """
        Gets the city of this AvailableNumbersFull.
        City with which this number is associated, if known. Otherwise NULL.

        :return: The city of this AvailableNumbersFull.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AvailableNumbersFull.
        City with which this number is associated, if known. Otherwise NULL.

        :param city: The city of this AvailableNumbersFull.
        :type: str
        """

        self._city = city

    @property
    def province(self):
        """
        Gets the province of this AvailableNumbersFull.
        State or Province with which this number is associated, if known. Postal Code. Otherwise NULL.

        :return: The province of this AvailableNumbersFull.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """
        Sets the province of this AvailableNumbersFull.
        State or Province with which this number is associated, if known. Postal Code. Otherwise NULL.

        :param province: The province of this AvailableNumbersFull.
        :type: str
        """

        self._province = province

    @property
    def country(self):
        """
        Gets the country of this AvailableNumbersFull.
        Country with which this number is associated, if known. Otherwise NULL.

        :return: The country of this AvailableNumbersFull.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AvailableNumbersFull.
        Country with which this number is associated, if known. Otherwise NULL.

        :param country: The country of this AvailableNumbersFull.
        :type: str
        """

        self._country = country

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
        if not isinstance(other, AvailableNumbersFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
