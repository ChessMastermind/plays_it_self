from random import randint
import pygame
import constants
pygame.init()
CONST = constants.const()
def random_pos(SCREEN_WIDTH: int = CONST.SCREEN_WIDTH, SCREEN_HEIGHT: int = CONST.SCREEN_HEIGHT):
    """ Creates random cordinates between (0 - SCREEN_WIDTH, 0 - SCREEN_HEIGHT)
    """
    return(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))
def draw(screen, pos:tuple):
    pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 2, 2), 2, 2)

