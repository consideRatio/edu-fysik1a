import pygame
import csv

from massive_object import MassiveObject

# Constants
fps = 60
display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Setup
pygame.init()
pygame.display.set_caption('Solar system simulation')
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def planet(img, x, y):
    screen.blit(img, (x*100,y*100))

def game_loop():
    x_change = 0
    y_change = 0
    x = display_width * 0.5
    y = display_width * 0.5




    solar_system = [
        MassiveObject.get
    ]

    game_exit = False
    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

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

        screen.fill(black)
        for obj in solar_system:
            obj.display(screen, scale=2)

        pygame.display.update()
        clock.tick(fps)

# End
game_loop()
pygame.quit()
quit()
