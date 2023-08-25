#######################################################
# 
# core_name_general_controller.py
# Python implementation of the Class CoreNameGeneralController
# Generated by Enterprise Architect
# Created on:      16-Dec-2022 10:56:05 AM
# Original author: Giu Platania
# 
#######################################################
from FreeTAKServer.components.core.abstract_component.cot_node import CoTNode
from FreeTAKServer.core.domain.node import Node
from digitalpy.core.main.controller import Controller
from digitalpy.core.zmanager.request import Request
from digitalpy.core.zmanager.response import Response
from digitalpy.core.zmanager.action_mapper import ActionMapper
from digitalpy.core.digipy_configuration.configuration import Configuration
from .cot_management_private_cot_controller import CoTManagementPrivateCoTController

from ..configuration.cot_management_constants import (
    BASE_OBJECT,
    BASE_OBJECT_NAME,
)
class COTManagementGeneralController(Controller):
    """this controller is responsible for general or fundamental component functionality"""
    def __init__(
        self,
        request: Request,
        response: Response,
    sync_action_mapper: ActionMapper,
        configuration: Configuration,
    ) -> None:
        super().__init__(request, response, sync_action_mapper, configuration)
        self.private_cot_controller = CoTManagementPrivateCoTController(request, response, sync_action_mapper, configuration)

    def initialize(self, request: Request, response: Response):
        super().initialize(request, response)
        self.private_cot_controller.initialize(request, response)

    def share_privately(self, cot_id: str, recipient_id: str):
        """Shares a specific COT privately with another user.
        
        Args:
            cot_id (str): The ID of the COT to be shared.
            recipient_id (str): The ID of the user to receive the shared COT.
        """
        # Check if the recipient is a valid user
        if not self.user_manager.is_valid_user(recipient_id):
            raise ValueError("Invalid recipient provided.")

        # Check if the COT exists and is owned by the current user
        cot = self.db.get_cot(cot_id)
        if cot is None or cot.owner_id != self.current_user.id:
            raise ValueError("Invalid COT provided.")

        # Share the COT privately with the recipient
        self.db.add_cot_to_user(cot_id, recipient_id)

    def broadcast(self, cot_id: str):
        """Broadcasts a specific COT to all users in the system.
        
        Args:
            cot_id (str): The ID of the COT to be broadcasted.
        """
        # Check if the COT exists and is owned by the current user
        cot = self.db.get_cot(cot_id)
        if cot is None or cot.owner != self.current_user:
            raise ValueError("Invalid COT ID or unauthorized access.")
        # Create a broadcast message with the COT data
        message = {"type": "cot_broadcast", "cot": cot.to_dict()}
        self.messaging.broadcast(message)

    def cot_broadcast(self):
        # retrieve the COT message from the request values
        cot_message = self.request.get_value("cot_message")
        # broadcast the COT message to all registered listeners
        self.broadcast(cot_message)
    
    def handle_default_cot(self, config_loader, action_mapper, **kwargs):
        """forward cots without a distinct handler
        """
        self.request.set_value("object_class_name", BASE_OBJECT_NAME)

        configuration = config_loader.find_configuration(BASE_OBJECT)

        self.request.set_value("configuration", configuration)

        self.request.set_value(
            "source_format", self.request.get_value("source_format")
        )
        self.request.set_value("target_format", "node")

        response = self.execute_sub_action("CreateNode")

        self.request.set_value("model_object", response.get_value("model_object"))

        response = self.execute_sub_action("DictToNode")

        for key, value in response.get_values().items():
            self.response.set_value(key, value)

        self.request.set_value('message', response.get_value("model_object"))
        # Serializer called by service manager requires the message value
        self.response.set_value('message', [response.get_value("model_object")])
        recipients = self.private_cot_controller.get_recipients(response.get_value("model_object"))
        self.request.set_value('recipients', recipients)

        # validate the users in the recipients list
        users_validated_response = self.execute_sub_action("ValidateUsers")

        self.cot_event_chain_of_command(response.get_value("model_object"), self.request.get_value("dictionary"), action_mapper)

        for key, value in users_validated_response.get_values().items():
            self.response.set_value(key, value)
        
        self.response.set_action("publish")

    def cot_event_chain_of_command(self, cot_model_object: CoTNode, cot_dict: str, action_mapper: ActionMapper, *args, **kwargs):
        """this method will handle different events which may or may not be associated with a CoT
        making the relevant (async) requests if it is, these events should be based on the contents of the CoT
        as anything type related should be handled in the routing phase and should not reach this point
        """
        # if the CoT is being sent to a mission and the CoT is a video alias
        missions = []
        if cot_model_object.detail is not None:
            missions = [d.mission for d in cot_model_object.detail.marti.dest if d.mission is not None]
        if len(missions)>0:
            self.request.set_value("xml_dict", cot_dict)
            cot_xml = self.execute_sub_action("DictToXML").get_value("xml")            

            if cot_model_object.type == "b-i-v":
                action_mapper.process_action("CreateMissionVideoAlias", self.request, self.response)

            # if the CoT is being sent to a mission and the CoT is a geofence
            elif cot_model_object.type == "u-d-c-c":
                action_mapper.process_action("CreateMissionGeoFence", self.request, self.response)
            
            # generic handler for all other CoTs being sent to a mission
            else:
                self.request.set_value("mission_ids", missions)
                self.request.set_value("cot_type", cot_model_object.type)
                self.request.set_value("callsign", cot_model_object.detail.contact.callsign)
                self.request.set_value("uid", cot_model_object.uid)
                self.request.set_value("lat", cot_model_object.point.lat)
                self.request.set_value("lon", cot_model_object.point.lon)
                self.request.set_value("iconset_path", cot_model_object.detail.usericon.iconsetpath)
                self.request.set_value("xml_content", cot_xml)
                self.request.set_context("mission")
                self.request.set_action("CreateMissionCOT")
                self.request.set_format("pickled")
                action_mapper.process_action(self.request, self.response, False, protocol="XML")