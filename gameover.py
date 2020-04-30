import pygame
from text import text_to_screen

pygame.init()

screen_width = 1500
screen_height = 700
screen_gameover = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
# white = (255, 255, 255)

clock = pygame.time.Clock()


def gameover_screen():

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_c]:
            quit()
        # if keys[pygame.K_r]:
        #
        screen_gameover.fill(black)
        text_to_screen(screen_gameover, "Game Over", screen_width/2 - 50, screen_height/2-100)

        pygame.display.update()
        clock.tick(60)


# gameover_screen()