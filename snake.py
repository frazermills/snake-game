import pygame

class Snake:
    
    def __init__(self, screen, colour, difficulty):
        self.screen = screen
        self.colour = colour
        self.difficulty = difficulty
        self.size = 15
        self.lenght = 5
        self.vel = 15
        self.x = screen.get_width() // 4
        self.y = screen.get_height() // 2
        self.xy = [(self.x, self.y)]
        self.direction = 'r'
        self.is_dead = False
        self.game_won = False

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
        if self.difficulty == "easy":
            self.size += 1
            self.lenght += 1
        elif self.difficulty == "normal":
            self.size += 2
            self.lenght += 2
            self.vel += 1
        elif self.difficulty == "hard":
            self.size += 3
            self.lenght += 3
            self.vel += 2
        elif self.difficulty == "very hard":
            self.size += 5
            self.lenght += 4
            self.vel += 5
