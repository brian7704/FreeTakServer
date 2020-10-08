#######################################################
# 
# MainSocket.py
# Python implementation of the Class MainSocket
# Generated by Enterprise Architect
# Created on:      21-May-2020 12:46:04 PM
# Original author: Natha Paquette
# 
#######################################################
import socket

class MainSocket:
    def __init__(self):  
        self.ip = "0.0.0.0" 
        self.port = "" 
        self.sock = "" 
        self.socketAF = socket.AF_INET
        self.socketSTREAM = socket.SOCK_STREAM 
        self.solSock = socket.SOL_SOCKET
        self.soReuseAddr = socket.SO_REUSEADDR
        self.sockProto = 1

