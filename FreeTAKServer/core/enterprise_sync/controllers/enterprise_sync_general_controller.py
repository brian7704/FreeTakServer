#######################################################
# 
# core_name_general_controller.py
# Python implementation of the Class CoreNameGeneralController
# Generated by Enterprise Architect
# Created on:      16-Dec-2022 10:56:05 AM
# Original author: Giu Platania
# 
#######################################################
from typing import List
from digitalpy.core.main.controller import Controller
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.zmanager.action_mapper import ActionMapper
from digitalpy.core.digipy_configuration.configuration import Configuration

from FreeTAKServer.core.enterprise_sync.controllers.enterprise_sync_database_controller import EnterpriseSyncDatabaseController

from .enterprise_sync_filesystem_controller import EnterpriseSyncFilesystemController

class EnterpriseSyncGeneralController(Controller):
    """general enterprise sync operations"""

    def __init__(
        self,
        request: Request,
        response: Response,
        sync_action_mapper: ActionMapper,
        configuration: Configuration,
    ) -> None:
        super().__init__(request, response, sync_action_mapper, configuration)
        self.filesystem_controller = EnterpriseSyncFilesystemController(request, response, sync_action_mapper, configuration)
        self.persistence_controller = EnterpriseSyncDatabaseController(request, response, sync_action_mapper, configuration)

    def initialize(self, request: Request, response: Response):
        super().initialize(request, response)
        self.filesystem_controller.initialize(request, response)
        self.persistence_controller.initialize(request, response)

    def broadcast(self):
        """Broadcasts a specific data package to all users in the system."""
        pass
    
    def enrollment(self):
        """Enrolls the user to FTS, provisioning ATAK devices through device profiles."""
        pass
    
    def file_list_http(self):
        """Gets a list of files on the server."""
        pass
    
    def excheck_join_existing_checklist(self):
        """Joins the user to a started set of tasks."""
        pass
    
    def delete_file(self):
        """Deletes a file from the server."""
        pass
    
    def download_file(self):
        """Downloads a file from the server."""
        pass
    
    def download_file_http(self):
        """Downloads one file from the server via HTTP."""
        pass
    
    def download_file_https(self):
        """Downloads one file from the server via HTTPS."""
        pass
    
    def file_list(self):
        """Provides a list of files on the server."""
        pass
    
    def file_list_https(self):
        """Gets a list of files on the server via HTTPS."""
        pass
    
    def generate_show_qr_code(self):
        """Generates and shows a QR code."""
        pass
    
    def is_private(self):
        """Checks if a data package is private.
        
        Returns:
            bool: True if the data package is private, False otherwise.
        """
        pass
    
    def upload_file(self):
        """Uploads a data package from the UI."""
        pass
    
    def upload_file_http(self):
        """Uploads one file to the server via HTTP."""
        pass
    
    def upload_file_https(self):
        """Uploads one file to the server via HTTPS."""
        pass

    def save_enterprise_sync_data(self, synctype: str, objectuid: str, objectdata: str, *args, **kwargs):
        """save enterprise sync data to the db and the file system"""
        self.filesystem_controller.save_file(synctype, objectuid, objectdata)
        self.persistence_controller.create_enterprise_sync_data_object(synctype, objectuid)

    def get_enterprise_sync_data(self, objectuid: str, *args, **kwargs):
        """get the object data from an enterprise sync object"""
        data_obj = self.persistence_controller.get_enterprise_sync_data_object(objectuid)
        object_data = self.filesystem_controller.get_file(data_obj.file_type, data_obj.PrimaryKey)
        self.response.set_value("objectdata", object_data)

    def get_multiple_enterprise_sync_data(self, objectuids: List[str], *args, **kwargs):
        """
        Get the object data from multiple enterprise sync objects.

        Args:
            objectuids (List[str]): A list of object UIDs to retrieve the data for.

        Returns:
            None
        """
        object_data_list = []
        for uid in objectuids:
            data_obj = self.persistence_controller.get_enterprise_sync_data_object(uid)
            object_data = self.filesystem_controller.get_file(data_obj.file_type, data_obj.PrimaryKey)
            object_data_list.append(object_data)
        
        self.response.set_value("objectdata", object_data_list)