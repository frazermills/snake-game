import pygame

class Snake:
    
    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour
        self.size = 15
        self.lenght = 5
        self.vel = 15
        self.x = screen.get_width() // 4
        self.y = screen.get_height() // 2
        self.xy = [(self.x, self.y)]
        self.direction = 'r'

    def update(self):
        self.xy += [(self.x, self.y)]
        self.xy = self.xy[-self.lenght:]
        for kx, ky in self.xy:
            pygame.draw.rect(self.screen, self.colour, (kx, ky, self.size, self.size))

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

    def grow(self):
        self.size += 1
        self.lenght += 1
