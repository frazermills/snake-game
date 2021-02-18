import pygame
from snake import Snake

def main():
    SIZE = WIDTH, HEIGHT = (800, 800)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    fps = 25

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    snake = Snake(screen, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if snake.direction != 'r':
                snake.direction = 'l'
        elif keys[pygame.K_d]:
            if snake.direction != 'l':
                snake.direction = 'r'
        elif keys[pygame.K_w]:
            if snake.direction != 'd':
                snake.direction = 'u'
        elif keys[pygame.K_s]:
            if snake.direction != 'u':
                snake.direction = 'd'
        screen.fill(BLACK)

        snake.move(snake.direction)

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
