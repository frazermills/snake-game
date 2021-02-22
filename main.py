import pygame, random, menus, food, time
from snake import Snake
from particle_system import ParticleSystem

# ---------------------------- Handles the menus from the menus module --------------------------- #
def menu_handler(menu_mode, screen, clock, text_font, colour, score, game_won, elapsed_time=0):
    settings_options = {
        "game_difficulty": "easy",
        "snake_colour": (0, 255, 0),
        "fruit_type": "apple"
    }

    in_menu = True

    while in_menu:

# ------------------------------------------ Start menu ------------------------------------------ #
        if menu_mode == "start":
            start_menu = menus.StartMenu(screen, clock, text_font, colour)
            start_menu.setup()
            while start_menu.option == None:
                start_menu.update()
                start_menu.is_clicked()

                if start_menu.option == "start game":
                    in_menu = False
                    
                elif start_menu.option == "settings":
                    menu_mode = "settings"

                elif start_menu.option == "credits":
                    menu_mode = "credits"
                    break

                elif start_menu.option == "quit game":
                    pygame.quit()
                    quit()

# ---------------------------------------- Game over menu ---------------------------------------- #                    
        elif menu_mode == "game over":            
            game_over_menu = menus.GameOverMenu(screen, clock, text_font, colour, game_won)
            game_over_menu.setup()
            while game_over_menu.option == None:
                game_over_menu.update()
                game_over_menu.is_clicked()

                if game_over_menu.option == "play again":
                    main()

                elif game_over_menu.option == "quit game":
                    pygame.quit()
                    quit()

                elif game_over_menu.option == "high score":
                    menu_mode = "high score"

# --------------------------------- Options from game over menu ---------------------------------- #
        elif menu_mode == "high score":
            high_score_menu = menus.HighScoreMenu(screen, clock, text_font, colour, elapsed_time)
            high_score_menu.setup()
            while high_score_menu.option == None:
                high_score_menu.update()
                high_score_menu.is_clicked()
                
                if high_score_menu.option == "main menu":
                    menu_mode = "start"
                    
# ---------------------------------------- Settings menu ----------------------------------------- #
        elif menu_mode == "settings":
            settings_menu = menus.SettingsMenu(screen, clock, text_font, colour)
            settings_menu.setup()

            while settings_menu.option == None:
                settings_menu.update()
                settings_menu.is_clicked()

                if settings_menu.option == "difficulty":
                    menu_mode = "difficulty"
                    break
                    
                elif settings_menu.option == "snake colour":
                    menu_mode = "snake colour"

                elif settings_menu.option == "fruit type":
                    menu_mode = "fruit type"

                elif settings_menu.option == "back":
                    menu_mode = "start"
                    break

# ---------------------------------- Options from settings menu ---------------------------------- #
        elif menu_mode == "snake colour":
            snake_colour_menu = menus.SnakeColourMenu(screen, clock, text_font, colour)
            snake_colour_menu.setup()

            while snake_colour_menu.option == None:
                snake_colour_menu.update()
                snake_colour_menu.is_clicked()

                if snake_colour_menu.option == "green":
                    settings_options["snake_colour"] = (0, 255, 0)
                    
                elif snake_colour_menu.option == "white":
                    settings_options["snake_colour"] = (255, 255, 255)
                    
                elif snake_colour_menu.option == "pink":
                    settings_options["snake_colour"] = (255, 105, 180)

                elif snake_colour_menu.option == "blue":
                    settings_options["snake_colour"] = (0, 0, 255)

                elif snake_colour_menu.option == "back":
                    menu_mode = "start"
                    break

        elif menu_mode == "difficulty":
            difficulty_menu = menus.DifficultyMenu(screen, clock, text_font, colour)
            difficulty_menu.setup()

            while difficulty_menu.option == None:
                difficulty_menu.update()
                difficulty_menu.is_clicked()

                if difficulty_menu.option == "easy":
                    settings_options["game_difficulty"] = "easy"
                    
                elif difficulty_menu.option == "normal":
                    settings_options["game_difficulty"] = "normal"
                    
                elif difficulty_menu.option == "hard":
                    settings_options["game_difficulty"] = "hard"

                elif difficulty_menu.option == "very hard":
                    settings_options["game_difficulty"] = "very hard"

                elif difficulty_menu.option == "back":
                    menu_mode = "start"
                    break

        elif menu_mode == "fruit type":
            fruit_type_menu = menus.FruitTypeMenu(screen, clock, text_font, colour)
            fruit_type_menu.setup()

            while fruit_type_menu.option == None:
                fruit_type_menu.update()
                fruit_type_menu.is_clicked()

                if fruit_type_menu.option == "apple":
                    settings_options["fruit_type"] = "apple"
                    
                elif fruit_type_menu.option == "banana":
                    settings_options["fruit_type"] = "banana"
                    
                elif fruit_type_menu.option == "orange":
                    settings_options["fruit_type"] = "orange"

                elif fruit_type_menu.option == "blueberry":
                    settings_options["fruit_type"] = "blueberry"

                elif fruit_type_menu.option == "back":
                    menu_mode = "start"
                    break
# ----------------------------------------- Credits menu ----------------------------------------- #
        elif menu_mode == "credits":
            credits_menu = menus.CreditsMenu(screen, clock, text_font, colour)
            credits_menu.setup()

            while credits_menu.option == None:
                credits_menu.update()
                credits_menu.is_clicked()

                if credits_menu.option == "back":
                    menu_mode = "start"
                    break

    return settings_options

# --------------------------------------------- Main --------------------------------------------- #
def main():

# ------------------------------- Initialising variable/constants -------------------------------- #
    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GOLD = (255, 215, 0)
    PURPLE = (153,50,204)
    YELLOW = (255,255,0)
    ORANGE = (255,69,0)
    fps = 25
    score = 0

# ------------------------------ Initialising pygame related items ------------------------------- #
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 20)

# ---------------------------- Starting menu and getting user options ---------------------------- #
    menu_mode = "start"
    settings_options = menu_handler(menu_mode, screen, clock, text_font, WHITE, score, False)

    game_difficulty = settings_options["game_difficulty"]
    snake_colour = settings_options["snake_colour"]
    fruit_type = settings_options["fruit_type"]

    fruit_colour = {
        "apple": RED,
        "banana": YELLOW,
        "orange": ORANGE,
        "blueberry": BLUE
    }

# ---------------------------- Creating instances of all the classes ----------------------------- #
    snake = Snake(screen, snake_colour, game_difficulty)
    fruit = food.Fruit(screen, fruit_colour[fruit_type])
    golden_apple = food.GoldenApple(screen, GOLD)
    poisonous_apple = food.PoisonousApple(screen, PURPLE)
    victory_fruit = food.VictoryFruit(screen, WHITE)
    particle_system = ParticleSystem(screen)

# ----------------------------------- Setting up stage system ------------------------------------ #
    trigger = False
    stage_1 = True
    stage_2 = False
    stage_3 = False
    stage_4 = False
    stage_5 = False
    particle_colour = None

# ----------------------------------- Setting up music system ------------------------------------ #

    burp_1 = pygame.mixer.Sound("sounds/burp_1.wav")
    burp_2 = pygame.mixer.Sound("sounds/burp_2.wav")
    eat_food = pygame.mixer.Sound("sounds/eat_food.wav")
    game_over = pygame.mixer.Sound("sounds/game_over.wav")

    music = pygame.mixer.music.load("sounds/Cyberpunk_Moonlight_Sonata.mp3")
    pygame.mixer.music.play(-1)

# ---------------------------------------- Main game loop ---------------------------------------- #
    start_time = time.time()
    while not snake.is_dead and not snake.game_won:

# ---------------------------------------- Event handling ---------------------------------------- #
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

        if snake.x < 0 or snake.x > WIDTH or snake.y < 0 or snake.y > HEIGHT:
            print("collision detected")
            snake.is_dead = True

# ---------------------------------------- Stage checker ----------------------------------------- #
        if score > 10:
            stage_2 = True
            stage_1 = False

        if score > 20:
            stage_3 = True
            stage_2 = False

        if poisonous_apple.timer > 300:
            stage_4 = True
            stage_3 = False

        if snake.game_won:
            stage_5 = True
            stage_4 = False

        screen.fill(BLACK)

# ---------------------------------------- Stage manager ----------------------------------------- #
        if stage_1:
            fruit.draw()
            
            if fruit.is_eaten(snake.x, snake.y, snake.size):
                eat_food.play()
                fruit.update_xy()
                snake.grow()
                score += 1
                trigger = True
                particle_colour = fruit.colour

                num = random.randrange(10)
                if num == 9:
                    burp_1.play()
                elif num == 1:
                    burp_2.play()

        elif stage_2:
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
            if poisonous_apple.timer == 100:
                stage_4 = True
                stage_3 = False

            poisonous_apple.draw()
            poisonous_apple.follow_snake(snake.x, snake.y)

            if poisonous_apple.is_eaten(snake.x, snake.y, snake.size):
                eat_food.play()
                snake.is_dead = True

        elif stage_4:

            victory_fruit.draw()

            if victory_fruit.is_eaten(snake.x, snake.y, snake.size):
                snake.game_won = True
        
        elif stage_5:
            snake.game_won = True
            snake.is_dead = True

# ------------------------------------- Outputting to screen ------------------------------------- #
        elapsed_time = round((time.time() - start_time), 3)
        snake.move(snake.direction)
        particle_system.explode(trigger, snake.x, snake.y, particle_colour)
        screen.blit(text_font.render(f'score: {score}', True, WHITE), (10, 10))
        screen.blit(text_font.render(f'time: {elapsed_time}', True, WHITE), (10, 30))
        
        trigger = False

        pygame.display.update()
        clock.tick(fps)

# ------------------------------------ End of main game loop ------------------------------------- #
    pygame.mixer.fadeout(1)
    menu_mode = "game over"
    menu_handler(menu_mode, screen, clock, text_font, WHITE, score, snake.game_won, elapsed_time)

if __name__ == "__main__":
    main()
