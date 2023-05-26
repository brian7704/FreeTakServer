# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TakCert(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, creator_dn: str=None, subject_dn: str=None, user_dn: str=None, certificate: str=None, hash: str=None, client_uid: str=None, issuance_date: datetime=None, expiration_date: datetime=None, effective_date: datetime=None, revocation_date: datetime=None, token: str=None, serial_number: str=None):  # noqa: E501
        """TakCert - a model defined in Swagger

        :param id: The id of this TakCert.  # noqa: E501
        :type id: int
        :param creator_dn: The creator_dn of this TakCert.  # noqa: E501
        :type creator_dn: str
        :param subject_dn: The subject_dn of this TakCert.  # noqa: E501
        :type subject_dn: str
        :param user_dn: The user_dn of this TakCert.  # noqa: E501
        :type user_dn: str
        :param certificate: The certificate of this TakCert.  # noqa: E501
        :type certificate: str
        :param hash: The hash of this TakCert.  # noqa: E501
        :type hash: str
        :param client_uid: The client_uid of this TakCert.  # noqa: E501
        :type client_uid: str
        :param issuance_date: The issuance_date of this TakCert.  # noqa: E501
        :type issuance_date: datetime
        :param expiration_date: The expiration_date of this TakCert.  # noqa: E501
        :type expiration_date: datetime
        :param effective_date: The effective_date of this TakCert.  # noqa: E501
        :type effective_date: datetime
        :param revocation_date: The revocation_date of this TakCert.  # noqa: E501
        :type revocation_date: datetime
        :param token: The token of this TakCert.  # noqa: E501
        :type token: str
        :param serial_number: The serial_number of this TakCert.  # noqa: E501
        :type serial_number: str
        """
        self.swagger_types = {
            'id': int,
            'creator_dn': str,
            'subject_dn': str,
            'user_dn': str,
            'certificate': str,
            'hash': str,
            'client_uid': str,
            'issuance_date': datetime,
            'expiration_date': datetime,
            'effective_date': datetime,
            'revocation_date': datetime,
            'token': str,
            'serial_number': str
        }

        self.attribute_map = {
            'id': 'id',
            'creator_dn': 'creatorDn',
            'subject_dn': 'subjectDn',
            'user_dn': 'userDn',
            'certificate': 'certificate',
            'hash': 'hash',
            'client_uid': 'clientUid',
            'issuance_date': 'issuanceDate',
            'expiration_date': 'expirationDate',
            'effective_date': 'effectiveDate',
            'revocation_date': 'revocationDate',
            'token': 'token',
            'serial_number': 'serialNumber'
        }
        self._id = id
        self._creator_dn = creator_dn
        self._subject_dn = subject_dn
        self._user_dn = user_dn
        self._certificate = certificate
        self._hash = hash
        self._client_uid = client_uid
        self._issuance_date = issuance_date
        self._expiration_date = expiration_date
        self._effective_date = effective_date
        self._revocation_date = revocation_date
        self._token = token
        self._serial_number = serial_number

    @classmethod
    def from_dict(cls, dikt) -> 'TakCert':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TakCert of this TakCert.  # noqa: E501
        :rtype: TakCert
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this TakCert.


        :return: The id of this TakCert.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this TakCert.


        :param id: The id of this TakCert.
        :type id: int
        """

        self._id = id

    @property
    def creator_dn(self) -> str:
        """Gets the creator_dn of this TakCert.


        :return: The creator_dn of this TakCert.
        :rtype: str
        """
        return self._creator_dn

    @creator_dn.setter
    def creator_dn(self, creator_dn: str):
        """Sets the creator_dn of this TakCert.


        :param creator_dn: The creator_dn of this TakCert.
        :type creator_dn: str
        """

        self._creator_dn = creator_dn

    @property
    def subject_dn(self) -> str:
        """Gets the subject_dn of this TakCert.


        :return: The subject_dn of this TakCert.
        :rtype: str
        """
        return self._subject_dn

    @subject_dn.setter
    def subject_dn(self, subject_dn: str):
        """Sets the subject_dn of this TakCert.


        :param subject_dn: The subject_dn of this TakCert.
        :type subject_dn: str
        """

        self._subject_dn = subject_dn

    @property
    def user_dn(self) -> str:
        """Gets the user_dn of this TakCert.


        :return: The user_dn of this TakCert.
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn: str):
        """Sets the user_dn of this TakCert.


        :param user_dn: The user_dn of this TakCert.
        :type user_dn: str
        """

        self._user_dn = user_dn

    @property
    def certificate(self) -> str:
        """Gets the certificate of this TakCert.


        :return: The certificate of this TakCert.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate: str):
        """Sets the certificate of this TakCert.


        :param certificate: The certificate of this TakCert.
        :type certificate: str
        """

        self._certificate = certificate

    @property
    def hash(self) -> str:
        """Gets the hash of this TakCert.


        :return: The hash of this TakCert.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash: str):
        """Sets the hash of this TakCert.


        :param hash: The hash of this TakCert.
        :type hash: str
        """

        self._hash = hash

    @property
    def client_uid(self) -> str:
        """Gets the client_uid of this TakCert.


        :return: The client_uid of this TakCert.
        :rtype: str
        """
        return self._client_uid

    @client_uid.setter
    def client_uid(self, client_uid: str):
        """Sets the client_uid of this TakCert.


        :param client_uid: The client_uid of this TakCert.
        :type client_uid: str
        """

        self._client_uid = client_uid

    @property
    def issuance_date(self) -> datetime:
        """Gets the issuance_date of this TakCert.


        :return: The issuance_date of this TakCert.
        :rtype: datetime
        """
        return self._issuance_date

    @issuance_date.setter
    def issuance_date(self, issuance_date: datetime):
        """Sets the issuance_date of this TakCert.


        :param issuance_date: The issuance_date of this TakCert.
        :type issuance_date: datetime
        """

        self._issuance_date = issuance_date

    @property
    def expiration_date(self) -> datetime:
        """Gets the expiration_date of this TakCert.


        :return: The expiration_date of this TakCert.
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: datetime):
        """Sets the expiration_date of this TakCert.


        :param expiration_date: The expiration_date of this TakCert.
        :type expiration_date: datetime
        """

        self._expiration_date = expiration_date

    @property
    def effective_date(self) -> datetime:
        """Gets the effective_date of this TakCert.


        :return: The effective_date of this TakCert.
        :rtype: datetime
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date: datetime):
        """Sets the effective_date of this TakCert.


        :param effective_date: The effective_date of this TakCert.
        :type effective_date: datetime
        """

        self._effective_date = effective_date

    @property
    def revocation_date(self) -> datetime:
        """Gets the revocation_date of this TakCert.


        :return: The revocation_date of this TakCert.
        :rtype: datetime
        """
        return self._revocation_date

    @revocation_date.setter
    def revocation_date(self, revocation_date: datetime):
        """Sets the revocation_date of this TakCert.


        :param revocation_date: The revocation_date of this TakCert.
        :type revocation_date: datetime
        """

        self._revocation_date = revocation_date

    @property
    def token(self) -> str:
        """Gets the token of this TakCert.


        :return: The token of this TakCert.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this TakCert.


        :param token: The token of this TakCert.
        :type token: str
        """

        self._token = token

    @property
    def serial_number(self) -> str:
        """Gets the serial_number of this TakCert.


        :return: The serial_number of this TakCert.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        """Sets the serial_number of this TakCert.


        :param serial_number: The serial_number of this TakCert.
        :type serial_number: str
        """

        self._serial_number = serial_number