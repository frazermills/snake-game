import pygame, random
from snake import Snake
from food import Food
import menus

def menu_handler(mode, screen, clock, text_font, colour, score):
    if mode == str("start"):
        start_menu = menus.StartMenu(screen, clock, text_font, colour)
        start_menu.setup()
        while start_menu.option == None:
            start_menu.update()
            start_menu.is_clicked()

            if start_menu.option == "start game":
                print("start game")
                return
                
            elif start_menu.option == "settings":
                print("settings")
                menu_mode = str("settings")
                menu_handler(menu_mode, screen, clock, text_font, colour, score)

            elif start_menu.option == "credits":
                print("credits")
                menu_mode = str("credits")
                menu_handler(menu_mode, screen, clock, text_font, colour, score)

            elif start_menu.option == "quit game":
                print("quit game")
                end_game(score)
                
    elif mode == str("settings"):
        settings_menu = menus.SettingsMenu(screen, clock, text_font, colour)
        settings_menu.setup()

        while True:
            settings_menu.update()
            settings_menu.is_clicked()

            if settings_menu.option == "button 1":
                pass
                
            elif settings_menu.option == "button 1":
                pass

            elif settings_menu.option == "button 1":
                pass

    elif mode == str("credits"):
        print("insert credits")

def end_game(score):
    pygame.quit()
    print(f"your score was: {score}")

    play_again = input("would you like to play again? (y/n) ")
    if play_again == "y":
        main()
    else:
        quit()

def main():
    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
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
    text_font = pygame.font.SysFont("Arial", 20)
    
    menu_mode = str("start")
    menu_handler(menu_mode, screen, clock, text_font, WHITE, score)

    snake = Snake(screen, GREEN)
    apple = Food(screen, RED)

    burp_1 = pygame.mixer.Sound("sounds/burp_1.wav")
    burp_2 = pygame.mixer.Sound("sounds/burp_2.wav")
    eat_food = pygame.mixer.Sound("sounds/eat_food.wav")
    game_over = pygame.mixer.Sound("sounds/game_over.wav")
    
    music = pygame.mixer.music.load("sounds/Cyberpunk_Moonlight_Sonata.mp3")
    pygame.mixer.music.play(-1)

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
            pygame.mixer.fadeout(1)
            end_game(score)
        
        screen.fill(BLACK)

        snake.move(snake.direction)
        apple.draw()

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
