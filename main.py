import pygame, random
from snake import Snake
from food import Food

def end_game(score):
    pygame.quit()
    print(f"your score was: {score}")
    play_again = input("would you like to play again? (y/n) ")
    if play_again == "y":
        main()
    else:
        quit()

def main():
    SIZE = WIDTH, HEIGHT = (800, 800)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    fps = 25
    score = 0
    
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    burp_1 = pygame.mixer.Sound("sounds/burp_1.wav")
    burp_2 = pygame.mixer.Sound("sounds/burp_2.wav")
    eat_food = pygame.mixer.Sound("sounds/eat_food.wav")
    game_over = pygame.mixer.Sound("sounds/game_over.wav")
    
    music = pygame.mixer.music.load("sounds/Cyberpunk_Moonlight_Sonata.mp3")
    pygame.mixer.music.play(-1)


    snake = Snake(screen, GREEN)
    apple = Food(screen, RED)
    

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

        if apple.is_eaten(snake.x, snake.y, snake.size):
            eat_food.play()
            apple.update_xy()
            snake.grow()
            score += 1

            num = random.randrange(10)
            if num == 9:
                burp_1.play()
            elif num == 1:
                burp_2.play()

        if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
            pygame.mixer.fadeout(100)
            end_game(score)
        
        screen.fill(BLACK)

        snake.move(snake.direction)
        apple.draw()

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
