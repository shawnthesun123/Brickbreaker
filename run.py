import pygame
from main import main
pygame.init()
screen_width = 1500
screen_height = 700
screen_start = pygame.display.set_mode((screen_width, screen_height))

def run():
    black = (0, 0, 0)
    screen_start.fill(black)
    main()

run()
