import math
import string
import pygame
from random import *

from territory import Territory

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

territories = []

territory_count = 5

smallest_r = 50
highest_r = 100


################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def generate_random_str(n):
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))    

def init_map():
    for i in range(territory_count):
        territories.append(Territory((100 + i , 100), generate_random_str(10), randint(smallest_r, highest_r)))

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

    screen.fill((0, 0, 0))

    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(10)
    

# Done! Time to quit.
pygame.quit()