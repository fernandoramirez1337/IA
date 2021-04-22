import pygame 

WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#RGB
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
BEIGE = (207,185,151)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'),(33,20))