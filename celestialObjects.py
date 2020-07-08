from astropy import constants as const
from vpython import *
from math import *
#Meters
UA = 149597870700
class CelestialObjects(object):
    def __init__(self,mass,radio,pos,col):
        self.mass = mass
        self.radio = radio
        self.pos = pos
        self.col = col
        self.escape_vel = sqrt(2 * const.G.value * self.mass / self.radio)
        print(self.escape_vel)
        if(col == "yellow"):
            self.obj = sphere(pos = vector(self.pos[0],self.pos[1],self.pos[2]), radius=self.radio,color=color.yellow)
        elif(col == "blue"):
            self.obj = sphere(pos = vector(self.pos[0],self.pos[1],self.pos[2]), radius=self.radio,color=color.blue)
        elif(col == "white"):
            self.obj = sphere(pos = vector(self.pos[0],self.pos[1],self.pos[2]), radius=self.radio,color=color.white)
#695508.0 , 6371000
sun = CelestialObjects(mass = const.M_sun.value,radio = 695508000.0,pos = [0,0,0],col = "yellow")
earth = CelestialObjects(mass = 5.9722*(10**24),radio = 637100000,pos = [UA,0,0],col = "blue")
#moon = CelestialObjects(mass = const.M_sun.value,radio = 1737,pos = (500000,500000,0),col = "white")
