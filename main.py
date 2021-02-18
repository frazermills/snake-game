import pygame, random
import tkinter as tk
from snake import Snake
from food import Food

def menu_handler(mode, score):
    size = 800
    
    if mode == "start_menu":
        start_screen = tk.Tk()
        start_screen.geometry(f"{size}x{size}")
        start_screen.resizable(False, False)
        start_screen.configure(background = "black")
        
        quit_button = tk.Button(start_screen, text="quit game", width=15, height=2, command=quit)
        quit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        start_button = tk.Button(start_screen, text="start game", width=15, height=2, command=start_screen.destroy)
        start_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        start_screen.mainloop()

    elif mode == "end_menu":
        end_screen = tk.Tk()
        end_screen.geometry(f"{size}x{size}")
        end_screen.resizable(False, False)
        end_screen.configure(background = "black")
        
        quit_button = tk.Button(end_screen, text="quit game", width=15, height=2, command=quit)
        quit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        start_button = tk.Button(end_screen, text="try again", width=15, height=2, command=lambda:[end_screen.destroy(), main()])
        start_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        
        score = tk.Label(end_screen, text=f"your score was {score}", width=15, height=2)
        score.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        end_screen.mainloop()        

def end_game(score):
    pygame.quit()
    menu_handler("end_menu", score)

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

    menu_handler("start_menu", score)
    
    pygame.init()
    pygame.mixer.init()
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

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
