import pygame


class Territory:

    def __init__(self, position, name, r) -> None:
        self.position = position
        self.name = name
        self.connected_terrotories = []
        self.r = r

    def draw(self, DISPLAY):
        pygame.draw.circle(DISPLAY, (255, 0, 0), self.position, self.r)