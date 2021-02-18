import pygame

class Snake:
    
    def __init__(self, surface, colour):
        self.surface = surface
        self.colour = colour
        self.side = 15
        self.lenght = 10
        self.vel = 15
        self.x = surface.get_width() // 4
        self.y = surface.get_height() // 2
        self.XY = [(self.x, self.y)]
        self.direction = 'r'

    def update(self):
        self.XY += [(self.x, self.y)]
        self.XY = self.XY[-self.lenght:]
        for kx, ky in self.XY:
            pygame.draw.rect(self.surface, self.colour, (kx, ky, self.side, self.side))

    def move(self, key):
        if key == 'l':
            self.x -= self.vel
            self.update()
        if key == 'r':
            self.x += self.vel
            self.update()
        if key == 'u':
            self.y -= self.vel
            self.update()
        if key == 'd':
            self.y += self.vel
            self.update()