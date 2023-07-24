# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.coordinate import Coordinate  # noqa: F401,E501
from swagger_server.models.envelope import Envelope  # noqa: F401,E501
from swagger_server.models.geometry import Geometry  # noqa: F401,E501
from swagger_server.models.geometry_factory import GeometryFactory  # noqa: F401,E501
from swagger_server.models.point import Point  # noqa: F401,E501
from swagger_server.models.precision_model import PrecisionModel  # noqa: F401,E501
from swagger_server import util


class Geometry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, envelope: Geometry=None, factory: GeometryFactory=None, user_data: object=None, length: float=None, empty: bool=None, valid: bool=None, dimension: int=None, geometry_type: str=None, srid: int=None, num_geometries: int=None, precision_model: PrecisionModel=None, coordinate: Coordinate=None, coordinates: List[Coordinate]=None, num_points: int=None, simple: bool=None, rectangle: bool=None, area: float=None, centroid: Point=None, interior_point: Point=None, boundary: Geometry=None, boundary_dimension: int=None, envelope_internal: Envelope=None):  # noqa: E501
        """Geometry - a model defined in Swagger

        :param envelope: The envelope of this Geometry.  # noqa: E501
        :type envelope: Geometry
        :param factory: The factory of this Geometry.  # noqa: E501
        :type factory: GeometryFactory
        :param user_data: The user_data of this Geometry.  # noqa: E501
        :type user_data: object
        :param length: The length of this Geometry.  # noqa: E501
        :type length: float
        :param empty: The empty of this Geometry.  # noqa: E501
        :type empty: bool
        :param valid: The valid of this Geometry.  # noqa: E501
        :type valid: bool
        :param dimension: The dimension of this Geometry.  # noqa: E501
        :type dimension: int
        :param geometry_type: The geometry_type of this Geometry.  # noqa: E501
        :type geometry_type: str
        :param srid: The srid of this Geometry.  # noqa: E501
        :type srid: int
        :param num_geometries: The num_geometries of this Geometry.  # noqa: E501
        :type num_geometries: int
        :param precision_model: The precision_model of this Geometry.  # noqa: E501
        :type precision_model: PrecisionModel
        :param coordinate: The coordinate of this Geometry.  # noqa: E501
        :type coordinate: Coordinate
        :param coordinates: The coordinates of this Geometry.  # noqa: E501
        :type coordinates: List[Coordinate]
        :param num_points: The num_points of this Geometry.  # noqa: E501
        :type num_points: int
        :param simple: The simple of this Geometry.  # noqa: E501
        :type simple: bool
        :param rectangle: The rectangle of this Geometry.  # noqa: E501
        :type rectangle: bool
        :param area: The area of this Geometry.  # noqa: E501
        :type area: float
        :param centroid: The centroid of this Geometry.  # noqa: E501
        :type centroid: Point
        :param interior_point: The interior_point of this Geometry.  # noqa: E501
        :type interior_point: Point
        :param boundary: The boundary of this Geometry.  # noqa: E501
        :type boundary: Geometry
        :param boundary_dimension: The boundary_dimension of this Geometry.  # noqa: E501
        :type boundary_dimension: int
        :param envelope_internal: The envelope_internal of this Geometry.  # noqa: E501
        :type envelope_internal: Envelope
        """
        self.swagger_types = {
            'envelope': Geometry,
            'factory': GeometryFactory,
            'user_data': object,
            'length': float,
            'empty': bool,
            'valid': bool,
            'dimension': int,
            'geometry_type': str,
            'srid': int,
            'num_geometries': int,
            'precision_model': PrecisionModel,
            'coordinate': Coordinate,
            'coordinates': List[Coordinate],
            'num_points': int,
            'simple': bool,
            'rectangle': bool,
            'area': float,
            'centroid': Point,
            'interior_point': Point,
            'boundary': Geometry,
            'boundary_dimension': int,
            'envelope_internal': Envelope
        }

        self.attribute_map = {
            'envelope': 'envelope',
            'factory': 'factory',
            'user_data': 'userData',
            'length': 'length',
            'empty': 'empty',
            'valid': 'valid',
            'dimension': 'dimension',
            'geometry_type': 'geometryType',
            'srid': 'srid',
            'num_geometries': 'numGeometries',
            'precision_model': 'precisionModel',
            'coordinate': 'coordinate',
            'coordinates': 'coordinates',
            'num_points': 'numPoints',
            'simple': 'simple',
            'rectangle': 'rectangle',
            'area': 'area',
            'centroid': 'centroid',
            'interior_point': 'interiorPoint',
            'boundary': 'boundary',
            'boundary_dimension': 'boundaryDimension',
            'envelope_internal': 'envelopeInternal'
        }
        self._envelope = envelope
        self._factory = factory
        self._user_data = user_data
        self._length = length
        self._empty = empty
        self._valid = valid
        self._dimension = dimension
        self._geometry_type = geometry_type
        self._srid = srid
        self._num_geometries = num_geometries
        self._precision_model = precision_model
        self._coordinate = coordinate
        self._coordinates = coordinates
        self._num_points = num_points
        self._simple = simple
        self._rectangle = rectangle
        self._area = area
        self._centroid = centroid
        self._interior_point = interior_point
        self._boundary = boundary
        self._boundary_dimension = boundary_dimension
        self._envelope_internal = envelope_internal

    @classmethod
    def from_dict(cls, dikt) -> 'Geometry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Geometry of this Geometry.  # noqa: E501
        :rtype: Geometry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def envelope(self) -> Geometry:
        """Gets the envelope of this Geometry.


        :return: The envelope of this Geometry.
        :rtype: Geometry
        """
        return self._envelope

    @envelope.setter
    def envelope(self, envelope: Geometry):
        """Sets the envelope of this Geometry.


        :param envelope: The envelope of this Geometry.
        :type envelope: Geometry
        """

        self._envelope = envelope

    @property
    def factory(self) -> GeometryFactory:
        """Gets the factory of this Geometry.


        :return: The factory of this Geometry.
        :rtype: GeometryFactory
        """
        return self._factory

    @factory.setter
    def factory(self, factory: GeometryFactory):
        """Sets the factory of this Geometry.


        :param factory: The factory of this Geometry.
        :type factory: GeometryFactory
        """

        self._factory = factory

    @property
    def user_data(self) -> object:
        """Gets the user_data of this Geometry.


        :return: The user_data of this Geometry.
        :rtype: object
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data: object):
        """Sets the user_data of this Geometry.


        :param user_data: The user_data of this Geometry.
        :type user_data: object
        """

        self._user_data = user_data

    @property
    def length(self) -> float:
        """Gets the length of this Geometry.


        :return: The length of this Geometry.
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length: float):
        """Sets the length of this Geometry.


        :param length: The length of this Geometry.
        :type length: float
        """

        self._length = length

    @property
    def empty(self) -> bool:
        """Gets the empty of this Geometry.


        :return: The empty of this Geometry.
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty: bool):
        """Sets the empty of this Geometry.


        :param empty: The empty of this Geometry.
        :type empty: bool
        """

        self._empty = empty

    @property
    def valid(self) -> bool:
        """Gets the valid of this Geometry.


        :return: The valid of this Geometry.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid: bool):
        """Sets the valid of this Geometry.


        :param valid: The valid of this Geometry.
        :type valid: bool
        """

        self._valid = valid

    @property
    def dimension(self) -> int:
        """Gets the dimension of this Geometry.


        :return: The dimension of this Geometry.
        :rtype: int
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: int):
        """Sets the dimension of this Geometry.


        :param dimension: The dimension of this Geometry.
        :type dimension: int
        """

        self._dimension = dimension

    @property
    def geometry_type(self) -> str:
        """Gets the geometry_type of this Geometry.


        :return: The geometry_type of this Geometry.
        :rtype: str
        """
        return self._geometry_type

    @geometry_type.setter
    def geometry_type(self, geometry_type: str):
        """Sets the geometry_type of this Geometry.


        :param geometry_type: The geometry_type of this Geometry.
        :type geometry_type: str
        """

        self._geometry_type = geometry_type

    @property
    def srid(self) -> int:
        """Gets the srid of this Geometry.


        :return: The srid of this Geometry.
        :rtype: int
        """
        return self._srid

    @srid.setter
    def srid(self, srid: int):
        """Sets the srid of this Geometry.


        :param srid: The srid of this Geometry.
        :type srid: int
        """

        self._srid = srid

    @property
    def num_geometries(self) -> int:
        """Gets the num_geometries of this Geometry.


        :return: The num_geometries of this Geometry.
        :rtype: int
        """
        return self._num_geometries

    @num_geometries.setter
    def num_geometries(self, num_geometries: int):
        """Sets the num_geometries of this Geometry.


        :param num_geometries: The num_geometries of this Geometry.
        :type num_geometries: int
        """

        self._num_geometries = num_geometries

    @property
    def precision_model(self) -> PrecisionModel:
        """Gets the precision_model of this Geometry.


        :return: The precision_model of this Geometry.
        :rtype: PrecisionModel
        """
        return self._precision_model

    @precision_model.setter
    def precision_model(self, precision_model: PrecisionModel):
        """Sets the precision_model of this Geometry.


        :param precision_model: The precision_model of this Geometry.
        :type precision_model: PrecisionModel
        """

        self._precision_model = precision_model

    @property
    def coordinate(self) -> Coordinate:
        """Gets the coordinate of this Geometry.


        :return: The coordinate of this Geometry.
        :rtype: Coordinate
        """
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate: Coordinate):
        """Sets the coordinate of this Geometry.


        :param coordinate: The coordinate of this Geometry.
        :type coordinate: Coordinate
        """

        self._coordinate = coordinate

    @property
    def coordinates(self) -> List[Coordinate]:
        """Gets the coordinates of this Geometry.


        :return: The coordinates of this Geometry.
        :rtype: List[Coordinate]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: List[Coordinate]):
        """Sets the coordinates of this Geometry.


        :param coordinates: The coordinates of this Geometry.
        :type coordinates: List[Coordinate]
        """

        self._coordinates = coordinates

    @property
    def num_points(self) -> int:
        """Gets the num_points of this Geometry.


        :return: The num_points of this Geometry.
        :rtype: int
        """
        return self._num_points

    @num_points.setter
    def num_points(self, num_points: int):
        """Sets the num_points of this Geometry.


        :param num_points: The num_points of this Geometry.
        :type num_points: int
        """

        self._num_points = num_points

    @property
    def simple(self) -> bool:
        """Gets the simple of this Geometry.


        :return: The simple of this Geometry.
        :rtype: bool
        """
        return self._simple

    @simple.setter
    def simple(self, simple: bool):
        """Sets the simple of this Geometry.


        :param simple: The simple of this Geometry.
        :type simple: bool
        """

        self._simple = simple

    @property
    def rectangle(self) -> bool:
        """Gets the rectangle of this Geometry.


        :return: The rectangle of this Geometry.
        :rtype: bool
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle: bool):
        """Sets the rectangle of this Geometry.


        :param rectangle: The rectangle of this Geometry.
        :type rectangle: bool
        """

        self._rectangle = rectangle

    @property
    def area(self) -> float:
        """Gets the area of this Geometry.


        :return: The area of this Geometry.
        :rtype: float
        """
        return self._area

    @area.setter
    def area(self, area: float):
        """Sets the area of this Geometry.


        :param area: The area of this Geometry.
        :type area: float
        """

        self._area = area

    @property
    def centroid(self) -> Point:
        """Gets the centroid of this Geometry.


        :return: The centroid of this Geometry.
        :rtype: Point
        """
        return self._centroid

    @centroid.setter
    def centroid(self, centroid: Point):
        """Sets the centroid of this Geometry.


        :param centroid: The centroid of this Geometry.
        :type centroid: Point
        """

        self._centroid = centroid

    @property
    def interior_point(self) -> Point:
        """Gets the interior_point of this Geometry.


        :return: The interior_point of this Geometry.
        :rtype: Point
        """
        return self._interior_point

    @interior_point.setter
    def interior_point(self, interior_point: Point):
        """Sets the interior_point of this Geometry.


        :param interior_point: The interior_point of this Geometry.
        :type interior_point: Point
        """

        self._interior_point = interior_point

    @property
    def boundary(self) -> Geometry:
        """Gets the boundary of this Geometry.


        :return: The boundary of this Geometry.
        :rtype: Geometry
        """
        return self._boundary

    @boundary.setter
    def boundary(self, boundary: Geometry):
        """Sets the boundary of this Geometry.


        :param boundary: The boundary of this Geometry.
        :type boundary: Geometry
        """

        self._boundary = boundary

    @property
    def boundary_dimension(self) -> int:
        """Gets the boundary_dimension of this Geometry.


        :return: The boundary_dimension of this Geometry.
        :rtype: int
        """
        return self._boundary_dimension

    @boundary_dimension.setter
    def boundary_dimension(self, boundary_dimension: int):
        """Sets the boundary_dimension of this Geometry.


        :param boundary_dimension: The boundary_dimension of this Geometry.
        :type boundary_dimension: int
        """

        self._boundary_dimension = boundary_dimension

    @property
    def envelope_internal(self) -> Envelope:
        """Gets the envelope_internal of this Geometry.


        :return: The envelope_internal of this Geometry.
        :rtype: Envelope
        """
        return self._envelope_internal

    @envelope_internal.setter
    def envelope_internal(self, envelope_internal: Envelope):
        """Sets the envelope_internal of this Geometry.


        :param envelope_internal: The envelope_internal of this Geometry.
        :type envelope_internal: Envelope
        """

        self._envelope_internal = envelope_internal