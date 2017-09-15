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

_NUMERALS = '0123456789abcdefABCDEF'
_HEXDEC = {v: int(v, 16) for v in (x+y for x in _NUMERALS for y in _NUMERALS)}
LOWERCASE, UPPERCASE = 'x', 'X'

def rgb(triplet):
    return _HEXDEC[triplet[0:2]], _HEXDEC[triplet[2:4]], _HEXDEC[triplet[4:6]]

def triplet(rgb, lettercase=LOWERCASE):
    return format(rgb[0]<<16 | rgb[1]<<8 | rgb[2], '06'+lettercase)

class MassiveObject:
    solar_system = {}

    def __init__(self, name='Unnamed object', color=(255,255,255), hx=0, hy=0, mass=0):
        self.name = name
        self.color = color
        self.hx = float(hx)
        self.hy = float(hy)
        self.mass = float(mass)

    def get_x(self):
        return int(self.hx)
    def get_y(self):
        return int(self.hy)
    def get_position(self):
        return (int(self.hx), int(self.hy))
    def get_screen_position(self, scale):
        return (int(self.hx * 10**scale), int(self.hy * 10**scale))

    def display(self, screen, scale):
        # w, h = screen.get_size()
        pygame.draw.circle(screen, self.color, self.get_screen_position(scale), 10)

with open('solar_system_details_trimmed.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        MassiveObject.solar_system[row['name']] = MassiveObject(name=row['name'], color=triplet(row['color']), hx=row['hx'], hy=row['hy'], mass=row['mass'])



