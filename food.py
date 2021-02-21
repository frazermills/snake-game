import pygame, random

DEBUG = True

# --------------------------------------- Used for stage 1 --------------------------------------- #
class Fruit:
    def __init__(self, screen, colour):
        self.screen = screen
        self.colour = colour
        self.size = 30
        self.x = (screen.get_width() // 2) - (self.size // 2)
        self.y = (screen.get_height() // 2) - (self.size // 2)
        self.set_x = set()
        self.set_y = set()

# ------------------------------------ Draws fruit on screen ------------------------------------- #
    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.size, self.size))
        self.set_x = set(range(self.x, self.x + self.size + 1))
        self.set_y = set(range(self.y, self.y + self.size))

# ------------------------------------ Updates fruit x and y ------------------------------------- #
    def update_xy(self):
        self.x = random.randrange(self.screen.get_width() - self.size)
        self.y = random.randrange(self.screen.get_height() - self.size)

# ---------------------------------- Checks if fruit is eaten ------------------------------------ #
    def is_eaten(self, snake_x, snake_y, snake_size):
        if set(range(snake_x, snake_x + snake_size + 1)) & self.set_x and set(range(snake_y, snake_y + snake_size + 1)) & self.set_y:
            eaten = True
        else:
            eaten = False
        return eaten


# --------------------------------------- Used for stage 2 --------------------------------------- #
class GoldenApple(Fruit):
    def __init__(self, screen, colour):
        Fruit.__init__(self, screen, colour)
        self.size = 60


# --------------------------------------- Used for stage 3 --------------------------------------- #
class PoisonousApple(Fruit):
    def __init__(self, screen, colour):
        Fruit.__init__(self, screen, colour)
        self.size = 45
        self.timer = 0

# ---------------------------------- Gets apple to follow snake ---------------------------------- #
    def follow_snake(self, snakex, snakey):
        self.timer += 1
        
        if self.x < snakex:
            self.x += 5
        elif self.x > snakex:
            self.x -= 5

        if self.y < snakey:
            self.y += 5
        elif self.y > snakey:
            self.y -= 5


# --------------------------------------- Used for stage 4 --------------------------------------- #
class VictoryFruit(Fruit):
    def __init__(self, screen, colour):
        Fruit.__init__(self, screen, colour)
        self.size = 30
        
