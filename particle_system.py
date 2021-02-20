import pygame, random

class ParticleSystem:
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)
    
    def __init__(self, screen):
        self.screen = screen
        self.particles = []
        self.blast_radius = 35 
        self.particle_number = 25
        self.directions = []
        self.particle_sizes = []

    def explode(self,trigger, x, y, colour):
        if colour == self.GOLD:
            self.blast_radius = 70
            self.particle_number = 80

        elif colour == self.RED:
            self.blast_radius = 35
            self.particle_number = 25
        
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
            pygame.draw.rect(self.screen, colour, ((xy, self.sizes[i])))
            
        self.particles = [
            (xy[0] - d[0], xy[1] - d[1])
            for xy, d in zip(self.particles, self.directions)
        ]       
