import pygame

FPS = 60
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Solar system simulation')
clock = pygame.time.Clock()

planet_img = pygame.image.load('images/planet.png')

def planet(x, y):
    game_display.blit(planet_img, (x,y))

x_change = 0
x = display_width * 0.5
y = display_width * 0.5


abort = False
while not abort:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abort = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                x_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change

    game_display.fill(black)
    planet(x, y)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()


