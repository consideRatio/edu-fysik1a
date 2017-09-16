import pygame
import math

from massive_object import MassiveObject
from easing import ease_out_quad

# Constants
WINDOW_TITLE = 'Solar System - A simulation'
FPS = 60
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
SCALE_EASING_DURATION = 500
G = 6.67408e-11

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

def game_loop():
    x, y, x_change, y_change = (0, 0, 0, 0)
    scale_current = -9
    scale_easing_from, scale_easing_to, scale_easing_to_change = (scale_current, scale_current, 0)
    scale_easing_time = SCALE_EASING_DURATION

    solar_system = [
        MassiveObject.solar_system["Earth"],
        MassiveObject.solar_system["The sun"],
        MassiveObject.solar_system["Venus"],
        MassiveObject.solar_system["Mars"],
        MassiveObject.solar_system["Jupiter"],
        MassiveObject.solar_system["Saturn"],
        MassiveObject.solar_system["Uranus"],
        MassiveObject.solar_system["Neptune"]
    ]

    game_exit = False
    while not game_exit:
        frame_time = clock.tick(FPS)

        # Conclude changes from events since since last frame...
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scale_easing_to_change += 0.5
                elif event.button == 5:
                    scale_easing_to_change -= 0.5

        # Process changes...
        x += x_change
        x_change = 0
        y += y_change
        y_change = 0

        if (scale_easing_to_change != 0):
            scale_easing_from = scale_current
            scale_easing_to += scale_easing_to_change
            scale_easing_to_change = 0
            scale_easing_time = 0

        if (scale_easing_time < SCALE_EASING_DURATION):
            scale_easing_time += frame_time
            scale_current = ease_out_quad(scale_easing_time, scale_easing_from, scale_easing_to - scale_easing_from, SCALE_EASING_DURATION)

        for o1 in solar_system:
            for o2 in solar_system:
                if o1 == o2:
                    continue

                dx, dy = (o1.x - o2.x), (o1.y - o2.y)
                r_abs = math.sqrt(dx ** 2 + dy ** 2)
                r_hat_x, r_hat_y = dx / r_abs, dy / r_abs
                F_abs = G * o1.mass * o2.mass / r_abs ** 2
                o2.Fx, o2.Fy = o2.Fx + r_hat_x * F_abs, o2.Fy + r_hat_y * F_abs

        for o1 in solar_system:

            o1.ax = o1.Fx / o1.mass
            o1.ay = o1.Fy / o1.mass
            o1.vx += o1.ax * 3600 * 24 * 31 / FPS
            o1.vy += o1.ay * 3600 * 24 * 31 / FPS
            o1.x += o1.vx * 3600 * 24 * 31 / FPS
            o1.y += o1.vy * 3600 * 24 * 31 / FPS





        # Render screen...
        screen.fill(BLACK)
        for o in solar_system:
            if o.name == "Earth":
                print(o.vx)
            o.display(screen, scale=scale_current)

        pygame.display.update()


# End
game_loop()
pygame.quit()
quit()
