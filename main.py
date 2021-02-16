import pygame, random

def setup_screen(RES):
    screen = pygame.display.set_mode([RES, RES])
    return screen

def render_screen(screen):
    screen.fill(pygame.Color("black"))

def update_screen():
    pygame.display.flip()

def draw_snake(screen, snake, SIZE):
    [pygame.draw.rect(screen, pygame.Color('white'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def main(): 
    RES = 500
    SIZE = 25
    FPS = 60

    pygame.init()

    screen = setup_screen(RES)
    clock = pygame.time.Clock()

    x = random.randrange(SIZE, RES - SIZE, SIZE)
    y = random.randrange(SIZE, RES - SIZE, SIZE)

    snake = [(x, y)]

    while True:
        render_screen(screen)
        draw_snake(screen, snake, SIZE)
        clock.tick(FPS)
        update_screen()
        event_handler()

if __name__ == "__main__":
    main()

