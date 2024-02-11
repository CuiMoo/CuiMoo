# 1 - Import package
import pygame
from  sys import exit
from PlayerShip import *

# 2 - Define constants
WINDOW_WIDTH = 768
WINDOW_HEIGHT = 768
FPS = 60
# 3 -Initialize the world
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('CuiMoo SPACECRAFT')
clock = pygame.time.Clock()

playerShip2_red = 'space\PNG\playerShip2_red.png' 
playerShip2_green = 'space\PNG\playerShip2_green.png'
playerShip2_orange = 'space\PNG\playerShip2_orange.png'
playerShip2_blue = 'space\PNG\playerShip2_blue.png'


player = pygame.sprite.GroupSingle()
fire = pygame.sprite.GroupSingle()
player.add(Ship(WINDOW_WIDTH,WINDOW_HEIGHT,playerShip2_orange))
fire.add(Turbo())
# 4 - Load asset: images, sounds, etc.
space_surface = pygame.image.load('space/Backgrounds/black.png').convert()


# 5 - Initialize variables


# 6 - Loop forever
while True:
    # 7 -Check for handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 8 - Do any 'per frame' actions
    #-SPACE BACK GROUND-#                    

    # 9 - Clear the window

    # 10 -Draw all window elements
            
    N_bg = 9
    bg_pos = [(0,0),(256,0),(512,0),(0,256),(256,256),(512,256),(0,512),
              (256,512),(512,512)]

    for pic in range(N_bg):
        screen.blit(space_surface,bg_pos[pic])

    player.draw(screen)
    player.update()
    fire.draw(screen)
    fire.update()
            
    # 11 -Update the window
    pygame.display.update()

    # 12 -Slow things down a bit
    clock.tick(FPS)