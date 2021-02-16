import pygame, random

def setup_screen(RES):
    screen = pygame.display.set_mode([RES, RES])
    return screen

def render_screen(screen):
    screen.fill(pygame.Color("black"))
    pygame.display.flip()

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

    while True:
        render_screen(screen)
        clock.tick(FPS)

        event_handler()

if __name__ == "__main__":
    main()

