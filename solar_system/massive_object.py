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

import sys
import pygame
import csv
import struct
import math

def get_velocities(x, y, T):
    return -y / T, x / T

class MassiveObject:
    solar_system = {}


    def __init__(self, name='Unnamed object', color=(255,255,255), x=0, y=0, mass=1.99e30, diameter=1, orbit_period=0):
        self.name = name
        self.color = color

        self.mass = float(mass)
        self.diameter = float(diameter)
        self.orbit_period = float(orbit_period)

        self.set_position(x, y)
        if (self.orbit_period):
            self.set_velocity(*get_velocities(float(x), float(y), self.orbit_period))
            self.set_acceleration(0, 0)
            self.set_force(0, 0)
        else:
            self.set_velocity(0, 0)
            self.set_acceleration(0, 0)
            self.set_force(0, 0)



    def set_position(self, x, y):
        self.x, self.y = (float(x), float(y))
    def set_velocity(self, vx, vy):
        self.vx, self.vy = (float(vx), float(vy))
    def set_acceleration(self, ax, ay):
        self.ax, self.ay = (float(ax), float(ay))
    def set_force(self, Fx, Fy):
        self.Fx, self.Fy = (float(Fx), float(Fy))

    def get_x(self):
        return int(self.x)
    def get_y(self):
        return int(self.y)
    def get_position(self):
        return (int(self.x), int(self.y))
    def get_screen_position(self, screen, scale):
        x = max(0, min(screen.get_width(), int(self.x * (10**scale)) + int(screen.get_width() / 2)))
        y = max(0, min(screen.get_height(), int(self.y * (10**scale)) + int(screen.get_height() / 2)))
        return (x, y)

    def display(self, screen, scale):
        # w, h = screen.get_size()
        pygame.draw.circle(screen, self.color, self.get_screen_position(screen, scale), 10)

with open('solar_system_details_trimmed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        MassiveObject.solar_system[row['name']] = MassiveObject(name=row['name'], color=struct.unpack('BBB',bytes.fromhex(row['color'])), x=row['hx'], y=row['hy'], mass=row['mass'], diameter=row['diameter'], orbit_period=float(row['orbit_period'])*3600*24)



