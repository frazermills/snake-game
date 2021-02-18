import pygame

class Food:

    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour
        self.side = 30
        self.x = (screen.get_width() // 2) - (self.side // 2)
        self.y = (screen.get_height() // 2) - (self.side // 2)
        self.set_x = set()
        self.set_y = set()

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.side, self.side))
        self.set_x = set(range(self.x, self.x + self.side + 1))
        self.set_y = set(range(self.y, self.y + self.side))
