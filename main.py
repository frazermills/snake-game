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

def draw_apple(screen, applex, appley, SIZE):
    pygame.draw.rect(screen, pygame.Color('red'), (applex, appley, SIZE, SIZE))

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

    snakex = random.randrange(SIZE, RES - SIZE, SIZE)
    snakey = random.randrange(SIZE, RES - SIZE, SIZE)

    snake = [(snakex, snakey)]

    applex = random.randrange(SIZE, RES - SIZE, SIZE)
    appley = random.randrange(SIZE, RES - SIZE, SIZE)

    while True:
        render_screen(screen)
        draw_snake(screen, snake, SIZE)
        draw_apple(screen, applex, appley, SIZE)
        
        clock.tick(FPS)
        update_screen()
        event_handler()
        

if __name__ == "__main__":
    main()

