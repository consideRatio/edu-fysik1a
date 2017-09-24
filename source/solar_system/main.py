import pygame
import numpy as np
import math

from massive_object import MassiveObject
from easing import ease_out_quad

# Constants
WINDOW_TITLE = 'Solar System - A simulation'
FPS = 144
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_SIZE = np.array([DISPLAY_WIDTH, DISPLAY_HEIGHT], int)
SCALE_EASING_DURATION = 400
G = 6.67408e-11
TIME_SCALE = 3600 * 24 * 7  # One week per second

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCALE_DOUBLING = 2

# Setup
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

def game_loop():
    x, y, x_change, y_change = (0, 0, 0, 0)
    scale_current = 10 ** -9
    scale_easing_from, scale_easing_to, scale_easing_to_change = (scale_current, scale_current, 1)
    scale_easing_time = SCALE_EASING_DURATION

    offset = np.array([screen.get_width() / 2, screen.get_height() / 2], float) / scale_current
    recent_mouse_pos, new_mouse_pos = [0,0], [0,0]

    solar_system = [
        MassiveObject.solar_system["The sun"],
        MassiveObject.solar_system["Venus"],
        MassiveObject.solar_system["Earth"],
        MassiveObject.solar_system["Mars"],
        MassiveObject.solar_system["Jupiter"],
        MassiveObject.solar_system["Saturn"],
        MassiveObject.solar_system["Uranus"],
        MassiveObject.solar_system["Neptune"],
    ]

    game_exit = False
    while not game_exit:
        frame_time = clock.tick(FPS)
        simulation_time = frame_time / 1000 * TIME_SCALE

        # Conclude changes from events since since last frame...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 0.5
                elif event.key == pygame.K_RIGHT:
                    x_change += 0.5
                elif event.key == pygame.K_UP:
                    y_change -= 0.5
                elif event.key == pygame.K_DOWN:
                    y_change += 0.5
                elif event.key == pygame.K_SPACE:
                    offset = np.array([screen.get_width() / 2, screen.get_height() / 2], float) / scale_current
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    recent_mouse_pos = np.array(pygame.mouse.get_pos(), dtype=int)
                elif event.button == 4:
                    scale_easing_to_change *= SCALE_DOUBLING
                elif event.button == 5:
                    scale_easing_to_change /= SCALE_DOUBLING
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    new_mouse_pos = np.array(pygame.mouse.get_pos(), dtype=int)
                    offset += (new_mouse_pos - recent_mouse_pos) / scale_current
                    recent_mouse_pos = new_mouse_pos

        # Process changes...
        x += x_change
        x_change = 0
        y += y_change
        y_change = 0

        if (scale_easing_to_change != 1):
            scale_easing_from = scale_current
            scale_easing_to *= scale_easing_to_change
            scale_easing_to_change = 1
            scale_easing_time = 0

        if (scale_easing_time < SCALE_EASING_DURATION):
            scale_old = scale_current
            scale_easing_time = min(scale_easing_time + frame_time, SCALE_EASING_DURATION)
            scale_current = ease_out_quad(scale_easing_time, scale_easing_from, scale_easing_to - scale_easing_from, SCALE_EASING_DURATION)
            mouse_pos = np.array(pygame.mouse.get_pos(), dtype=int)
            offset -= mouse_pos * (1/scale_old - 1/scale_current)

        # STEP:
        # - update x' based on v
        # - update v' based on a
        # - update a' based on F
        # - update F' based on x
        # - flush -' to -

        for o1 in solar_system:
            for o2 in solar_system:
                if o1 == o2:
                    continue

                dr = o2.r - o1.r
                dr_norm = np.linalg.norm(dr)
                dr_hat = dr / dr_norm
                F_abs = G * o1.m * o2.m / dr_norm ** 2
                o1.new_F += dr_hat * F_abs

        for o1 in solar_system:
            o1.new_r = o1.r + o1.v * simulation_time
            o1.new_v = o1.v + o1.a * simulation_time
            o1.new_a = o1.F / o1.m

            o1.flush()

        # Render screen...
        screen.fill(BLACK)
        for o in solar_system:
            o.display(screen, scale=scale_current, offset=offset, time_scale=TIME_SCALE)

        pygame.display.update()


# End
game_loop()
pygame.quit()
quit()
