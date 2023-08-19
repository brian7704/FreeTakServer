# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RepeatableType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, initiate_test: str=None, cancel_test: str=None, name: str=None):  # noqa: E501
        """RepeatableType - a model defined in Swagger

        :param initiate_test: The initiate_test of this RepeatableType.  # noqa: E501
        :type initiate_test: str
        :param cancel_test: The cancel_test of this RepeatableType.  # noqa: E501
        :type cancel_test: str
        :param name: The name of this RepeatableType.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'initiate_test': str,
            'cancel_test': str,
            'name': str
        }

        self.attribute_map = {
            'initiate_test': 'initiateTest',
            'cancel_test': 'cancelTest',
            'name': 'name'
        }
        self._initiate_test = initiate_test
        self._cancel_test = cancel_test
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'RepeatableType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RepeatableType of this RepeatableType.  # noqa: E501
        :rtype: RepeatableType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def initiate_test(self) -> str:
        """Gets the initiate_test of this RepeatableType.


        :return: The initiate_test of this RepeatableType.
        :rtype: str
        """
        return self._initiate_test

    @initiate_test.setter
    def initiate_test(self, initiate_test: str):
        """Sets the initiate_test of this RepeatableType.


        :param initiate_test: The initiate_test of this RepeatableType.
        :type initiate_test: str
        """

        self._initiate_test = initiate_test

    @property
    def cancel_test(self) -> str:
        """Gets the cancel_test of this RepeatableType.


        :return: The cancel_test of this RepeatableType.
        :rtype: str
        """
        return self._cancel_test

    @cancel_test.setter
    def cancel_test(self, cancel_test: str):
        """Sets the cancel_test of this RepeatableType.


        :param cancel_test: The cancel_test of this RepeatableType.
        :type cancel_test: str
        """

        self._cancel_test = cancel_test

    @property
    def name(self) -> str:
        """Gets the name of this RepeatableType.


        :return: The name of this RepeatableType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RepeatableType.


        :param name: The name of this RepeatableType.
        :type name: str
        """

        self._name = name