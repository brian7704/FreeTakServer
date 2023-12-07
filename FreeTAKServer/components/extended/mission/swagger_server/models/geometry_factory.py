# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.coordinate_sequence_factory import CoordinateSequenceFactory  # noqa: F401,E501
from swagger_server.models.precision_model import PrecisionModel  # noqa: F401,E501
from swagger_server import util


class GeometryFactory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, precision_model: PrecisionModel=None, coordinate_sequence_factory: CoordinateSequenceFactory=None, srid: int=None):  # noqa: E501
        """GeometryFactory - a model defined in Swagger

        :param precision_model: The precision_model of this GeometryFactory.  # noqa: E501
        :type precision_model: PrecisionModel
        :param coordinate_sequence_factory: The coordinate_sequence_factory of this GeometryFactory.  # noqa: E501
        :type coordinate_sequence_factory: CoordinateSequenceFactory
        :param srid: The srid of this GeometryFactory.  # noqa: E501
        :type srid: int
        """
        self.swagger_types = {
            'precision_model': PrecisionModel,
            'coordinate_sequence_factory': CoordinateSequenceFactory,
            'srid': int
        }

        self.attribute_map = {
            'precision_model': 'precisionModel',
            'coordinate_sequence_factory': 'coordinateSequenceFactory',
            'srid': 'srid'
        }
        self._precision_model = precision_model
        self._coordinate_sequence_factory = coordinate_sequence_factory
        self._srid = srid

    @classmethod
    def from_dict(cls, dikt) -> 'GeometryFactory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeometryFactory of this GeometryFactory.  # noqa: E501
        :rtype: GeometryFactory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def precision_model(self) -> PrecisionModel:
        """Gets the precision_model of this GeometryFactory.


        :return: The precision_model of this GeometryFactory.
        :rtype: PrecisionModel
        """
        return self._precision_model

    @precision_model.setter
    def precision_model(self, precision_model: PrecisionModel):
        """Sets the precision_model of this GeometryFactory.


        :param precision_model: The precision_model of this GeometryFactory.
        :type precision_model: PrecisionModel
        """

        self._precision_model = precision_model

    @property
    def coordinate_sequence_factory(self) -> CoordinateSequenceFactory:
        """Gets the coordinate_sequence_factory of this GeometryFactory.


        :return: The coordinate_sequence_factory of this GeometryFactory.
        :rtype: CoordinateSequenceFactory
        """
        return self._coordinate_sequence_factory

    @coordinate_sequence_factory.setter
    def coordinate_sequence_factory(self, coordinate_sequence_factory: CoordinateSequenceFactory):
        """Sets the coordinate_sequence_factory of this GeometryFactory.


        :param coordinate_sequence_factory: The coordinate_sequence_factory of this GeometryFactory.
        :type coordinate_sequence_factory: CoordinateSequenceFactory
        """

        self._coordinate_sequence_factory = coordinate_sequence_factory

    @property
    def srid(self) -> int:
        """Gets the srid of this GeometryFactory.


        :return: The srid of this GeometryFactory.
        :rtype: int
        """
        return self._srid

    @srid.setter
    def srid(self, srid: int):
        """Sets the srid of this GeometryFactory.


        :param srid: The srid of this GeometryFactory.
        :type srid: int
        """

        self._srid = srid
