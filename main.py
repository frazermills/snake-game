import pygame, random, menus
from snake import Snake
from food import Food
from particle_system import ParticleSystem

def menu_handler(menu_mode, screen, clock, text_font, colour, score):
    settings_options = {
        "game_difficulty": "easy",
        "snake_colour": (0, 255, 0)
    }

    in_menu = True

    while in_menu:
        if menu_mode == str("start"):
            start_menu = menus.StartMenu(screen, clock, text_font, colour)
            start_menu.setup()
            while start_menu.option == None:
                start_menu.update()
                start_menu.is_clicked()

                if start_menu.option == "start game":
                    print("start game")
                    in_menu = False
                    
                elif start_menu.option == "settings":
                    print("settings")
                    menu_mode = str("settings")

                elif start_menu.option == "credits":
                    print("credits")
                    menu_mode = str("credits")
                    break

                elif start_menu.option == "quit game":
                    print("quit game")
                    end_game(score)
                    
        elif menu_mode == str("settings"):
            settings_menu = menus.SettingsMenu(screen, clock, text_font, colour)
            settings_menu.setup()

            while settings_menu.option == None:
                settings_menu.update()
                settings_menu.is_clicked()

                if settings_menu.option == "difficulty":
                    menu_mode = str("difficulty")
                    menu_handler(menu_mode, screen, clock, text_font, colour, score)
                    
                elif settings_menu.option == "button 2":
                    pass

                elif settings_menu.option == "button 3":
                    pass

                elif settings_menu.option == "back":
                    print("start menu")
                    menu_mode = str("start")
                    break

        elif menu_mode == str("credits"):
            credits_menu = menus.CreditsMenu(screen, clock, text_font, colour)
            credits_menu.setup()

            while credits_menu.option == None:
                credits_menu.update()
                credits_menu.is_clicked()

                if credits_menu.option == "back":
                    print("start menu")
                    menu_mode = str("start")
                    break

        elif menu_mode == str("difficulty"):
            difficulty_menu = menus.DifficultyMenu(screen, clock, text_font, colour)
            difficulty_menu.setup()

            while difficulty_menu.option == None:
                difficulty_menu.update()
                difficulty_menu.is_clicked()

                if difficulty_menu.option == "easy":
                    settings_options["game_difficulty"] = str("easy")
                    
                elif difficulty_menu.option == "normal":
                    settings_options["game_difficulty"] = str("normal")
                    
                elif difficulty_menu.option == "hard":
                    settings_options["game_difficulty"] = str("hard")

                elif difficulty_menu.option == "very hard":
                    settings_options["game_difficulty"] = str("very hard")


                elif difficulty_menu.option == "back":
                    print("start menu")
                    menu_mode = str("start")
                    print("menu mode set to start")
                    break

    return settings_options

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
    settings_options = menu_handler(menu_mode, screen, clock, text_font, WHITE, score)

    game_difficulty = settings_options["game_difficulty"]
    snake_colour = settings_options["snake_colour"]

    snake = Snake(screen, GREEN, game_difficulty)
    apple = Food(screen, RED)
    particle_system = ParticleSystem(screen)
    trigger = False

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
            trigger = True

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
        particle_system.explode(trigger, snake.x, snake.y)
        trigger = False

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
