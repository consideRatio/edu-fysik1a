import pygame
import csv

from massive_object import SolarSystemObject

FPS = 60
display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Solar system simulation')
clock = pygame.time.Clock()

def planet(img, x, y):
    game_display.blit(img, (x*100,y*100))

x_change = 0
y_change = 0
x = display_width * 0.5
y = display_width * 0.5


def get_solar_system():
    with open('solar_system.csv') as f:
        solar_system = [SolarSystemObject(**{str.strip(k): str.strip(v) for k, v in row.items()}) for row in csv.DictReader(f)]
        return solar_system

solar_system = get_solar_system()

abort = False
while not abort:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abort = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= 0.5
            elif event.key == pygame.K_RIGHT:
                x_change += 0.5
            elif event.key == pygame.K_UP:
                y_change -= 0.5
            elif event.key == pygame.K_DOWN:
                y_change += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change += 0.5
            elif event.key == pygame.K_RIGHT:
                x_change -= 0.5
            elif event.key == pygame.K_UP:
                y_change += 0.5
            elif event.key == pygame.K_DOWN:
                y_change -= 0.5

    x += x_change
    y += y_change

    game_display.fill(black)
    for obj in solar_system:
        obj.display(game_display)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
