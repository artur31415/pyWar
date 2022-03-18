import math
import pygame
from random import *

pygame.init()
pygame.font.init()

# seed random number generator
#seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 700
height = 700

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True

clock = pygame.time.Clock()

################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

################################################################################################
#                                           MAIN LOOP
################################################################################################

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##################################################################
    # DRAW CODE
    ##################################################################

    # textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    # screen.blit(textsurface, (0, 0))

    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(10)
    

# Done! Time to quit.
pygame.quit()