import pygame, random, menus, food
from snake import Snake
from particle_system import ParticleSystem

DEBUG = False

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
                    if DEBUG: print("start game")
                    in_menu = False
                    
                elif start_menu.option == "settings":
                    if DEBUG: print("settings")
                    menu_mode = str("settings")

                elif start_menu.option == "credits":
                    if DEBUG: print("credits")
                    menu_mode = str("credits")
                    break

                elif start_menu.option == "quit game":
                    if DEBUG: print("quit game")
                    end_game(score)
                    
        if menu_mode == str("game over"):            
            game_over_menu = menus.GameOverMenu(screen, clock, text_font, colour)
            game_over_menu.setup()
            while game_over_menu.option == None:
                game_over_menu.update()
                game_over_menu.is_clicked()

                if game_over_menu.option == "play again":
                    main()

                elif game_over_menu.option == "quit game":
                    if DEBUG: print("quit game")
                    pygame.quit()
                    quit()
                    
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
                    if DEBUG: print("start menu")
                    menu_mode = str("start")
                    break

        elif menu_mode == str("credits"):
            credits_menu = menus.CreditsMenu(screen, clock, text_font, colour)
            credits_menu.setup()

            while credits_menu.option == None:
                credits_menu.update()
                credits_menu.is_clicked()

                if credits_menu.option == "back":
                    if DEBUG: print("start menu")
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
                    menu_mode = str("start")
                    if DEBUG: print("menu mode set to start")
                    break

    return settings_options

def main():
    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    GOLD = (255, 215, 0)
    PURPLE = (153,50,204)
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
    apple = food.Apple(screen, RED)
    golden_apple = food.GoldenApple(screen, GOLD)
    poisonous_apple = food.PoisonousApple(screen, PURPLE)
    particle_system = ParticleSystem(screen)

    trigger = False
    stage_1 = True
    stage_2 = False
    stage_3 = False
    particle_colour = GREEN

    burp_1 = pygame.mixer.Sound("sounds/burp_1.wav")
    burp_2 = pygame.mixer.Sound("sounds/burp_2.wav")
    eat_food = pygame.mixer.Sound("sounds/eat_food.wav")
    game_over = pygame.mixer.Sound("sounds/game_over.wav")

    music = pygame.mixer.music.load("sounds/Cyberpunk_Moonlight_Sonata.mp3")
    pygame.mixer.music.play(-1)

    while not snake.is_dead:
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

        if score > 10:
            stage_2 = True
            stage_1 = False

        if score > 20:
            stage_3 = True
            stage_2 = False
          
        if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
            snake.is_dead = True
        
        screen.fill(BLACK)

        if stage_1:
            if DEBUG: print("stage 1")
            apple.draw()
            
            if apple.is_eaten(snake.x, snake.y, snake.size):
                eat_food.play()
                apple.update_xy()
                snake.grow()
                score += 1
                trigger = True
                particle_colour = apple.colour

                num = random.randrange(10)
                if num == 9:
                    burp_1.play()
                elif num == 1:
                    burp_2.play()

        elif stage_2:
            if DEBUG: print("stage 2")
            golden_apple.draw()

            if golden_apple.is_eaten(snake.x, snake.y, snake.size):
                eat_food.play()
                golden_apple.update_xy()
                snake.grow()
                score += 2
                trigger = True
                particle_colour = golden_apple.colour

                num = random.randrange(5)
                if num == 4:
                    burp_1.play()
                elif num == 1:
                    burp_2.play()

        elif stage_3:
            if DEBUG: print("stage 3")
            poisonous_apple.draw()
            poisonous_apple.follow_snake(snake.x, snake.y)

            if poisonous_apple.is_eaten(snake.x, snake.y, snake.size):
                eat_food.play()
                snake.is_dead = True

        snake.move(snake.direction)
        particle_system.explode(trigger, snake.x, snake.y, particle_colour)
        trigger = False

        pygame.display.update()
        clock.tick(fps)

    pygame.mixer.fadeout(1)
    menu_mode = str("game over")
    menu_handler(menu_mode, screen, clock, text_font, WHITE, score)

if __name__ == "__main__":
    main()
