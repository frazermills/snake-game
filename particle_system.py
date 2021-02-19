import pygame, random

class ParticleSystem:
    def __init__(self, screen):
        self.screen = screen
        self.particles = []
        self.colour = (255, 0, 0)
        self.blast_radius = 35
        self.particle_number = 25
        self.directions = []
        self.particle_sizes = []

    def explode(self,trigger, x, y):
        if trigger:
            self.particles = [
                (random.randint(x - self.blast_radius, x + self.blast_radius),
                random.randint(y - self.blast_radius, y + self.blast_radius))
                for i in range(self.particle_number)
            ]

            self.directions = [
                (random.randrange(-1, 1),
                 random.randrange(-1, 1))
                for i in range(self.particle_number)
            ]

            self.sizes = [
                (random.randrange(1, 10),
                random.randrange(1, 10))
                for i in range(self.particle_number)
            ]

        for i, xy in enumerate(self.particles):
            pygame.draw.rect(self.screen, self.colour, ((xy, self.sizes[i])))
            
        self.particles = [
            (xy[0] - d[0], xy[1] - d[1])
            for xy, d in zip(self.particles, self.directions)
        ]       
