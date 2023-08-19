# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mission_invitation import MissionInvitation  # noqa: F401,E501
from swagger_server import util


class ApiResponseListMissionInvitation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, version: str=None, type: str=None, data: List[MissionInvitation]=None, messages: List[str]=None, node_id: str=None):  # noqa: E501
        """ApiResponseListMissionInvitation - a model defined in Swagger

        :param version: The version of this ApiResponseListMissionInvitation.  # noqa: E501
        :type version: str
        :param type: The type of this ApiResponseListMissionInvitation.  # noqa: E501
        :type type: str
        :param data: The data of this ApiResponseListMissionInvitation.  # noqa: E501
        :type data: List[MissionInvitation]
        :param messages: The messages of this ApiResponseListMissionInvitation.  # noqa: E501
        :type messages: List[str]
        :param node_id: The node_id of this ApiResponseListMissionInvitation.  # noqa: E501
        :type node_id: str
        """
        self.swagger_types = {
            'version': str,
            'type': str,
            'data': List[MissionInvitation],
            'messages': List[str],
            'node_id': str
        }

        self.attribute_map = {
            'version': 'version',
            'type': 'type',
            'data': 'data',
            'messages': 'messages',
            'node_id': 'nodeId'
        }
        self._version = version
        self._type = type
        self._data = data
        self._messages = messages
        self._node_id = node_id

    @classmethod
    def from_dict(cls, dikt) -> 'ApiResponseListMissionInvitation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApiResponseListMissionInvitation of this ApiResponseListMissionInvitation.  # noqa: E501
        :rtype: ApiResponseListMissionInvitation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this ApiResponseListMissionInvitation.


        :return: The version of this ApiResponseListMissionInvitation.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ApiResponseListMissionInvitation.


        :param version: The version of this ApiResponseListMissionInvitation.
        :type version: str
        """

        self._version = version

    @property
    def type(self) -> str:
        """Gets the type of this ApiResponseListMissionInvitation.


        :return: The type of this ApiResponseListMissionInvitation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ApiResponseListMissionInvitation.


        :param type: The type of this ApiResponseListMissionInvitation.
        :type type: str
        """

        self._type = type

    @property
    def data(self) -> List[MissionInvitation]:
        """Gets the data of this ApiResponseListMissionInvitation.


        :return: The data of this ApiResponseListMissionInvitation.
        :rtype: List[MissionInvitation]
        """
        return self._data

    @data.setter
    def data(self, data: List[MissionInvitation]):
        """Sets the data of this ApiResponseListMissionInvitation.


        :param data: The data of this ApiResponseListMissionInvitation.
        :type data: List[MissionInvitation]
        """

        self._data = data

    @property
    def messages(self) -> List[str]:
        """Gets the messages of this ApiResponseListMissionInvitation.


        :return: The messages of this ApiResponseListMissionInvitation.
        :rtype: List[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[str]):
        """Sets the messages of this ApiResponseListMissionInvitation.


        :param messages: The messages of this ApiResponseListMissionInvitation.
        :type messages: List[str]
        """

        self._messages = messages

    @property
    def node_id(self) -> str:
        """Gets the node_id of this ApiResponseListMissionInvitation.


        :return: The node_id of this ApiResponseListMissionInvitation.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id: str):
        """Sets the node_id of this ApiResponseListMissionInvitation.


        :param node_id: The node_id of this ApiResponseListMissionInvitation.
        :type node_id: str
        """

        self._node_id = node_id