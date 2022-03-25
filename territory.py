from lib2to3 import pygram
import pygame

from utils import vec_d


class Territory:

    def __init__(self, position, name, r) -> None:
        self.position = position
        self.name = name
        self.connected_territories = []
        self.r = r
        self.selected = False

    def draw(self, DISPLAY, FONT):
        pygame.draw.circle(DISPLAY, (255, 0, 0), self.position, self.r)

        textsurface = FONT.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(textsurface, (self.position[0] - self.r / 2, self.position[1]))

        if self.selected:
            pygame.draw.circle(DISPLAY, (255, 255, 255), self.position, self.r + 10, 2)

    def collision(self, point):
        return vec_d(self.position, point) <= self.r