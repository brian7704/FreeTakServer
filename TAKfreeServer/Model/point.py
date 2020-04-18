#######################################################
# 
# point.py
# Python implementation of the CoT point
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:07 AM
# Original author: Corvo
# 
#######################################################
# Latitude referred to the WGS 84 ellipsoid in degrees

class Point:

    def __init__(self, lat="00.00000000", lon='00.00000000', le = "9999999.0", ce = "9999999.0", hae = "00.00000000"):
        self.le = le
        self.ce = ce
        self.hae = hae
        self.lon = lon        
        self.lat = lat
        pass


    # ce getter 
    def getce(self): 
        return self.ce 

    # ce setter 
    def setce(self, ce):
        self.ce=ce 

    # le getter 
    def getle(self): 
        return le 

    # le setter 
    def setle(self,le):  
        self.le=le


    # lat getter 
    def getlat(self):
        return lat 

    # lat setter 
    def setlat(self, lat):  
        self.lat=lat

        # lon getter 
    def getlon(self):
        return lon 

    # lon setter 
    def setlon(self,lon):
        self.lon=lon
  
    def gethae(self):
        return hae

    def sethae(self,hae):
        self.hae = hae