import math
import string
import pygame
from random import *

from territory import Territory
from utils import vec_d

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

territory_font = pygame.font.SysFont('Comic Sans MS', 10)

running = True

clock = pygame.time.Clock()

territories = []

territory_count = 10

smallest_r = 10
highest_r = 50


################################################################################################
#                                           FUNCTIONS
################################################################################################
def map(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def generate_random_str(n):
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    return ''.join(choices(string.ascii_uppercase + string.digits, k = n))    

def init_map():
    for i in range(territory_count):
        new_pos = (100 + i * 2 * highest_r, 100)
        

        while True:
            new_pos = (randint(highest_r, width - highest_r), randint(highest_r, height - highest_r))
            is_new_pos = True
            for terr in territories:
                d = vec_d(new_pos, terr.position)
                if d <= highest_r * 2:
                    is_new_pos = False
                    break
                    
            if len(territories) == 0 or is_new_pos:
                break

        territories.append(Territory(new_pos, generate_random_str(5), randint(smallest_r, highest_r)))


def get_terr_by_name(name):
    for terr in territories:
        if terr.name == name:
            return terr
    return None
################################################################################################
#                                           MAIN LOOP
################################################################################################

init_map()

# territories[0].connected_territories.append(territories[1].name)
# territories[1].connected_territories.append(territories[2].name)

for terr in territories:
    while True:
        rand_index = randint(0, len(territories) - 1)
        if terr != territories[rand_index]:
            terr.connected_territories.append(territories[rand_index].name)
            break

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            for terr in territories:
                if terr.collision(mouse_pos):
                    print("clicked on ", terr.name)
                    terr.selected = True
                    break

    ##################################################################
    # UPDATE CODE
    ##################################################################

    


    ##################################################################
    # DRAW CODE
    ##################################################################

    # textsurface = myfont.render('Ticks = ' + str(ticks), False, (0, 0, 0))
    # screen.blit(textsurface, (0, 0))

    screen.fill((50, 50, 50))


    # draw connections
    for territory in territories:
        for terr_name in territory.connected_territories:
            terr = get_terr_by_name(terr_name)
            if terr != None:
                pygame.draw.line(screen, (0, 0, 0), territory.position, terr.position, 10)


    # draw territories
    for territory in territories:
        territory.draw(screen, territory_font)

    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()

    clock.tick(10)
    

# Done! Time to quit.
pygame.quit()