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
import csv
import struct
import math
import numpy as np

class MassiveObject:
    solar_system = {}

    def __init__(self,
                 name='Unnamed object',
                 color=(255,255,255),
                 r=np.zeros(2),
                 v=np.zeros(2),
                 a=np.zeros(2),
                 F=np.zeros(2),
                 m=1.99e30,
                 orbit_period=1.
                 ):
        self.name = name
        self.color = color
        self.m = float(m)
        self.orbit_period = float(orbit_period)

        (self.r, self.new_r) = (r, np.zeros(2))
        (self.v, self.new_v) = (v, np.zeros(2))
        (self.a, self.new_a) = (a, np.zeros(2))
        (self.F, self.new_F) = (F, np.zeros(2))
        #self.F_components, self.new_F_components = (np.array([]), np.array([]))

        if (self.orbit_period > 0):
            anti_clockwise_rotation = np.array([[0, -1], [1, 0]])
            self.v = 2 * math.pi * np.dot(anti_clockwise_rotation, r) / self.orbit_period

    def flush(self):
        (self.r, self.new_r) = (self.new_r, np.zeros(2))
        (self.v, self.new_v) = (self.new_v, np.zeros(2))
        (self.a, self.new_a) = (self.new_a, np.zeros(2))
        (self.F, self.new_F) = (self.new_F, np.zeros(2))

    def get_screen_position(self, screen, scale, offset):
        #screen_offset = np.array([screen.get_width() / 2, screen.get_height() / 2], float)
        bounds = np.array([screen.get_width(), screen.get_height()])
        pos = np.maximum(-bounds*2, np.minimum(bounds*2, (self.r + offset) * scale)).astype(int)
        return tuple(pos)

    def get_screen_vector_position(self, screen, scale, offset, time_scale, dr):
        #screen_offset = np.array([screen.get_width() / 2, screen.get_height() / 2], float)
        bounds = np.array([screen.get_width(), screen.get_height()])
        pos = np.maximum(-bounds*2, np.minimum(bounds*2, ((self.r + offset) + dr * time_scale)* scale)).astype(int)
        return tuple(pos)

    def display(self, screen, scale, offset, time_scale):
        # w, h = screen.get_size()
        pos = self.get_screen_position(screen, scale, offset)
        pygame.draw.circle(screen, self.color, pos, 10)
        end_pos_v = self.get_screen_vector_position(screen, scale, offset, time_scale ** 1 * 3, self.v)
        end_pos_a = self.get_screen_vector_position(screen, scale, offset, time_scale ** 2 * 3, self.a)
        pygame.draw.line(screen, self.color, pos, end_pos_v, 3)
        pygame.draw.line(screen, self.color, pos, end_pos_a, 3)

with open('solar_system_details_trimmed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        MassiveObject.solar_system[row['name']] = MassiveObject(
            name=row['name'],
            color=struct.unpack('BBB',bytes.fromhex(row['color'])),
            r=np.array([float(row['hx']), float(row['hy'])]),
            m=float(row['mass']),
            orbit_period=float(row['orbit_period'])*3600*24
        )

