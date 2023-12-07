# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Flowtag(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, enable: bool=None, text: str=None):  # noqa: E501
        """Flowtag - a model defined in Swagger

        :param enable: The enable of this Flowtag.  # noqa: E501
        :type enable: bool
        :param text: The text of this Flowtag.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'enable': bool,
            'text': str
        }

        self.attribute_map = {
            'enable': 'enable',
            'text': 'text'
        }
        self._enable = enable
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Flowtag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Flowtag of this Flowtag.  # noqa: E501
        :rtype: Flowtag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enable(self) -> bool:
        """Gets the enable of this Flowtag.


        :return: The enable of this Flowtag.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable: bool):
        """Sets the enable of this Flowtag.


        :param enable: The enable of this Flowtag.
        :type enable: bool
        """

        self._enable = enable

    @property
    def text(self) -> str:
        """Gets the text of this Flowtag.


        :return: The text of this Flowtag.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Flowtag.


        :param text: The text of this Flowtag.
        :type text: str
        """

        self._text = text
