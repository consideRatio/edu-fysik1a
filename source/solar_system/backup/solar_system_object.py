"""
    Space objects...
                m           kg          m               days            (°C)        (°C)
    name,       diameter,   mass,       orbit_distance, orbit_period,   lower_temp, upper_temp
    The sun,    1392684000, 1.99E30,    0,              0,              5500,       5500
    Mercury,    4879000,    3.30E23,    57909227000,    88,             -173,       427
    Venus,      12104000,   4.87E24,    108209475000,   225,            462,        462
    Earth,      12756000,   5.97E24,    149598262000,   365.24,         -88,        58
    Mars,       6792000,    6.42E23,    227943824000,   687,            -153,       20
    Jupiter,    142984000,  1.90E27,    778340821000,   4333,           -148,       -148
    Saturn,     120536000,  5.68E26,    1426666422000,  10756,          -178,       -178
    Uranus,     51118000,   8.68E25,    2870658186000,  30687,          -216,       -216
    Neptune,    49528000,   1.02E26,    4498396441000,  60190,          -214,       -214
    The moon,   3475000,    7.35E22,    384400,         27.3,           -233,       123

    Constants...
        seconds per day: 86400 s / day
        astronomical unit: 149597870700 m
"""

import pygame
import math

class SolarSystemObject:
    pixels_per_au = 400
    body_magnification = 1000

    def __init__(self, name='Unnamed object', hx=0, hy=0, hz=0, mag=0, diameter=0, mass=0, orbit_distance=0, orbit_period=0, lower_temp=0, upper_temp=0):
        self.name = name
        self.hx = float(hx)
        self.hy = float(hy)
        self.hz = float(hz)
        #self.pos2 = (float(hx), float(hy))
        #self.pos3 = (float(hx), float(hy), float(hz))
        self.diameter = float(diameter)
        self.mass = float(mass)
        self.orbit_distance = float(orbit_distance)
        self.orbit_period = float(orbit_period)
        self.lower_temp = float(lower_temp)
        self.upper_temp = float(upper_temp)

        self.image = pygame.image.load('images/{}.png'.format(str.lower(self.name)))
        self.earth_masses = self.mass / 5.97E24;
        self.image_size = self.diameter*pixels_per_au*
        self.image = pygame.transform.smoothscale(self.image, (int(self.image_size), int(self.image_size)))


    def display(self, game_display):
        objects_to_render = ["Earth", "Sun"]
        if objects_to_render.__contains__(self.name):

            w, h = game_display.get_size()
            game_display.blit(self.image, (self.hx*400+w/2-self.image_size/2, self.hy*400+h/2-self.image_size/2))



