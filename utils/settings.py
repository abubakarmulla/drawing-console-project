import pygame
pygame.init()
pygame.font.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLACK = (224,224,224)

FPS = 60

WIDTH , HEIGHT = 637 , 690

ROWS = COLS = 50

TOOLBAR_HEIGHT = 55

PIXEL_SIZE = HEIGHT // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)
