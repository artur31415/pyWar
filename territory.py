import pygame


class Territory:

    def __init__(self, position, name, r) -> None:
        self.position = position
        self.name = name
        self.connected_terrotories = []
        self.r = r

    def draw(self, DISPLAY, FONT):
        pygame.draw.circle(DISPLAY, (255, 0, 0), self.position, self.r)

        textsurface = FONT.render(self.name, False, (0, 0, 0))
        DISPLAY.blit(textsurface, (self.position[0] - self.r / 2, self.position[1]))