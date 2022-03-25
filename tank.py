import pygame


class Tank:

    def __init__(self, position, name, territory_name, count) -> None:
        self.position = position
        self.name = name
        self.territory_name = territory_name
        self.count = count
        self.selected = False

    def draw(self, DISPLAY):
        w = 10
        h = 10
        pygame.draw.rect(DISPLAY, (255, 255, 255), (self.position[0] - w / 2, self.position[1] - h / 2, w, h))