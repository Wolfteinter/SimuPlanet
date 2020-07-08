from vpython import *
from celestialObjects import sun
from celestialObjects import earth
#from celestialObjects import moon
from astropy import constants as const
from math import sqrt
UA = 149597870700
#eje_x = arrow(pos = vector(0,0,0),axis = vector(+UA,0,0),shaftwidth=UA*.0001,headwidth = UA*.02,headlength = UA*.03,color = color.white)
#eje_y = arrow(pos = vector(0,0,0),axis = vector(0,+UA,0),shaftwidth=UA*.0001,headwidth = UA*.02,headlength = UA*.03,color = color.white)
#eje_z = arrow(pos = vector(0,0,0),axis = vector(0,0,+UA),shaftwidth=UA*.0001,headwidth = UA*.02,headlength = UA*.03,color = color.white)
t = 0
vt = 0
while True:
    rate(100)
    if(earth.pos[0] < 0):
        a = const.G.value * sun.mass / earth.pos[0] ** 2
    else:
        a = -1 * const.G.value * sun.mass / earth.pos[0] ** 2
        
    sun.obj.pos = vector(0,0,0)
    earth.obj.pos = vector(earth.pos[0] - vt * t + 1 / 2 * a * t ** 2,0,0)
    earth.pos[0] = earth.pos[0] - vt * t + 1 / 2 * a * t ** 2
    vt = abs(a) * t
    print(earth.pos[0])

    t += 1
