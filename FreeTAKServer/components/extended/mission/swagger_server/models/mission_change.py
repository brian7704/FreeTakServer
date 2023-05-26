# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.external_mission_data import ExternalMissionData  # noqa: F401,E501
from swagger_server.models.log_entry import LogEntry  # noqa: F401,E501
from swagger_server.models.map_layer import MapLayer  # noqa: F401,E501
from swagger_server.models.mission_feed import MissionFeed  # noqa: F401,E501
from swagger_server.models.resource import Resource  # noqa: F401,E501
from swagger_server.models.uid_details import UidDetails  # noqa: F401,E501
from swagger_server import util


class MissionChange(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, content_uid: str=None, mission_name: str=None, timestamp: datetime=None, creator_uid: str=None, server_time: datetime=None, details: UidDetails=None, external_data: ExternalMissionData=None, log_entry: LogEntry=None, map_layer: MapLayer=None, mission_feed: MissionFeed=None, content_resource: Resource=None):  # noqa: E501
        """MissionChange - a model defined in Swagger

        :param type: The type of this MissionChange.  # noqa: E501
        :type type: str
        :param content_uid: The content_uid of this MissionChange.  # noqa: E501
        :type content_uid: str
        :param mission_name: The mission_name of this MissionChange.  # noqa: E501
        :type mission_name: str
        :param timestamp: The timestamp of this MissionChange.  # noqa: E501
        :type timestamp: datetime
        :param creator_uid: The creator_uid of this MissionChange.  # noqa: E501
        :type creator_uid: str
        :param server_time: The server_time of this MissionChange.  # noqa: E501
        :type server_time: datetime
        :param details: The details of this MissionChange.  # noqa: E501
        :type details: UidDetails
        :param external_data: The external_data of this MissionChange.  # noqa: E501
        :type external_data: ExternalMissionData
        :param log_entry: The log_entry of this MissionChange.  # noqa: E501
        :type log_entry: LogEntry
        :param map_layer: The map_layer of this MissionChange.  # noqa: E501
        :type map_layer: MapLayer
        :param mission_feed: The mission_feed of this MissionChange.  # noqa: E501
        :type mission_feed: MissionFeed
        :param content_resource: The content_resource of this MissionChange.  # noqa: E501
        :type content_resource: Resource
        """
        self.swagger_types = {
            'type': str,
            'content_uid': str,
            'mission_name': str,
            'timestamp': datetime,
            'creator_uid': str,
            'server_time': datetime,
            'details': UidDetails,
            'external_data': ExternalMissionData,
            'log_entry': LogEntry,
            'map_layer': MapLayer,
            'mission_feed': MissionFeed,
            'content_resource': Resource
        }

        self.attribute_map = {
            'type': 'type',
            'content_uid': 'contentUid',
            'mission_name': 'missionName',
            'timestamp': 'timestamp',
            'creator_uid': 'creatorUid',
            'server_time': 'serverTime',
            'details': 'details',
            'external_data': 'externalData',
            'log_entry': 'logEntry',
            'map_layer': 'mapLayer',
            'mission_feed': 'missionFeed',
            'content_resource': 'contentResource'
        }
        self._type = type
        self._content_uid = content_uid
        self._mission_name = mission_name
        self._timestamp = timestamp
        self._creator_uid = creator_uid
        self._server_time = server_time
        self._details = details
        self._external_data = external_data
        self._log_entry = log_entry
        self._map_layer = map_layer
        self._mission_feed = mission_feed
        self._content_resource = content_resource

    @classmethod
    def from_dict(cls, dikt) -> 'MissionChange':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MissionChange of this MissionChange.  # noqa: E501
        :rtype: MissionChange
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this MissionChange.


        :return: The type of this MissionChange.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this MissionChange.


        :param type: The type of this MissionChange.
        :type type: str
        """
        allowed_values = ["CREATE_MISSION", "DELETE_MISSION", "ADD_CONTENT", "REMOVE_CONTENT", "CREATE_DATA_FEED", "DELETE_DATA_FEED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def content_uid(self) -> str:
        """Gets the content_uid of this MissionChange.


        :return: The content_uid of this MissionChange.
        :rtype: str
        """
        return self._content_uid

    @content_uid.setter
    def content_uid(self, content_uid: str):
        """Sets the content_uid of this MissionChange.


        :param content_uid: The content_uid of this MissionChange.
        :type content_uid: str
        """

        self._content_uid = content_uid

    @property
    def mission_name(self) -> str:
        """Gets the mission_name of this MissionChange.


        :return: The mission_name of this MissionChange.
        :rtype: str
        """
        return self._mission_name

    @mission_name.setter
    def mission_name(self, mission_name: str):
        """Sets the mission_name of this MissionChange.


        :param mission_name: The mission_name of this MissionChange.
        :type mission_name: str
        """

        self._mission_name = mission_name

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this MissionChange.


        :return: The timestamp of this MissionChange.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this MissionChange.


        :param timestamp: The timestamp of this MissionChange.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def creator_uid(self) -> str:
        """Gets the creator_uid of this MissionChange.


        :return: The creator_uid of this MissionChange.
        :rtype: str
        """
        return self._creator_uid

    @creator_uid.setter
    def creator_uid(self, creator_uid: str):
        """Sets the creator_uid of this MissionChange.


        :param creator_uid: The creator_uid of this MissionChange.
        :type creator_uid: str
        """

        self._creator_uid = creator_uid

    @property
    def server_time(self) -> datetime:
        """Gets the server_time of this MissionChange.


        :return: The server_time of this MissionChange.
        :rtype: datetime
        """
        return self._server_time

    @server_time.setter
    def server_time(self, server_time: datetime):
        """Sets the server_time of this MissionChange.


        :param server_time: The server_time of this MissionChange.
        :type server_time: datetime
        """

        self._server_time = server_time

    @property
    def details(self) -> UidDetails:
        """Gets the details of this MissionChange.


        :return: The details of this MissionChange.
        :rtype: UidDetails
        """
        return self._details

    @details.setter
    def details(self, details: UidDetails):
        """Sets the details of this MissionChange.


        :param details: The details of this MissionChange.
        :type details: UidDetails
        """

        self._details = details

    @property
    def external_data(self) -> ExternalMissionData:
        """Gets the external_data of this MissionChange.


        :return: The external_data of this MissionChange.
        :rtype: ExternalMissionData
        """
        return self._external_data

    @external_data.setter
    def external_data(self, external_data: ExternalMissionData):
        """Sets the external_data of this MissionChange.


        :param external_data: The external_data of this MissionChange.
        :type external_data: ExternalMissionData
        """

        self._external_data = external_data

    @property
    def log_entry(self) -> LogEntry:
        """Gets the log_entry of this MissionChange.


        :return: The log_entry of this MissionChange.
        :rtype: LogEntry
        """
        return self._log_entry

    @log_entry.setter
    def log_entry(self, log_entry: LogEntry):
        """Sets the log_entry of this MissionChange.


        :param log_entry: The log_entry of this MissionChange.
        :type log_entry: LogEntry
        """

        self._log_entry = log_entry

    @property
    def map_layer(self) -> MapLayer:
        """Gets the map_layer of this MissionChange.


        :return: The map_layer of this MissionChange.
        :rtype: MapLayer
        """
        return self._map_layer

    @map_layer.setter
    def map_layer(self, map_layer: MapLayer):
        """Sets the map_layer of this MissionChange.


        :param map_layer: The map_layer of this MissionChange.
        :type map_layer: MapLayer
        """

        self._map_layer = map_layer

    @property
    def mission_feed(self) -> MissionFeed:
        """Gets the mission_feed of this MissionChange.


        :return: The mission_feed of this MissionChange.
        :rtype: MissionFeed
        """
        return self._mission_feed

    @mission_feed.setter
    def mission_feed(self, mission_feed: MissionFeed):
        """Sets the mission_feed of this MissionChange.


        :param mission_feed: The mission_feed of this MissionChange.
        :type mission_feed: MissionFeed
        """

        self._mission_feed = mission_feed

    @property
    def content_resource(self) -> Resource:
        """Gets the content_resource of this MissionChange.


        :return: The content_resource of this MissionChange.
        :rtype: Resource
        """
        return self._content_resource

    @content_resource.setter
    def content_resource(self, content_resource: Resource):
        """Sets the content_resource of this MissionChange.


        :param content_resource: The content_resource of this MissionChange.
        :type content_resource: Resource
        """

        self._content_resource = content_resource