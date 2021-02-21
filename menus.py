import pygame

class StartMenu:
    def __init__(self, screen, clock, font, colour):
        self.screen = screen
        self.clock = clock
        self.font = font
        self.colour = colour
        self.click = False
        self.button_size = 100
        self.button_width = 150
        self.button_height = 75
        self.option = None
        self.button_command = ["start game", "settings", "quit game", "credits"]
        self.title = "Snake game - by Frazer Mills"

    def setup(self):
        pygame.init()
        pygame.display.set_caption(f"{self.title}")
        self.screen.fill((0,0,0))
        
    def draw_text(self, text, x, y):
        textobj = self.font.render(text, 1, self.colour)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)

        button_4_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 200)
        button_4 = pygame.Rect(button_3_xy[0], button_4_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                
        elif button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]
                
        elif button_4.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[3]

        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), button_2)
        pygame.draw.rect(self.screen, (255, 0, 0), button_3)
        pygame.draw.rect(self.screen, (255, 0, 0), button_4)
        
        self.draw_text(f"{self.title}", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text(f"{self.button_command[1]}", button_2_xy[0] + 75, button_2_xy[1] + 35)
        self.draw_text(f"{self.button_command[2]}", button_3_xy[0] + 75, button_3_xy[1] + 35)
        self.draw_text(f"{self.button_command[3]}", button_3_xy[0] + 75, button_4_xy[1] + 35)

        pygame.display.update()

    def is_clicked(self):
        self.click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

class GameOverMenu(StartMenu):
    def __init__(self, screen, clock, font, colour, game_won):
        StartMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["play again", "quit game", "high score"]
        pygame.mixer.fadeout(1)
        self.game_won = game_won
        if self.game_won:
            self.title = "you win!"
        else:
            self.title = "game over menu"

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        if self.game_won:
                button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
                button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]

        elif self.game_won and button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]

        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), button_2)
        
        self.draw_text(f"{self.title}", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text(f"{self.button_command[1]}", button_2_xy[0] + 75, button_2_xy[1] + 35)

        if self.game_won:
            pygame.draw.rect(self.screen, (255, 0, 0), button_3)
            self.draw_text(f"{self.button_command[2]}", button_3_xy[0] + 75, button_3_xy[1] + 35)

        pygame.display.update()

class SettingsMenu(StartMenu):
    def __init__(self, screen, clock, font, colour):
        StartMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["difficulty", "snake colour", "fruit type", "back"]
        self.title = "settings menu"

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)        

        button_4_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 200)
        button_4 = pygame.Rect(button_4_xy[0], button_4_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]
                print("difficulty menu")

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                print("snake colour")
                
        elif button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]
                print("fruit type")

        elif button_4.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[3]
                print("back button pressed")

        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), button_2)
        pygame.draw.rect(self.screen, (255, 0, 0), button_3)
        pygame.draw.rect(self.screen, (255, 0, 0), button_4)

        self.draw_text(f"{self.title}", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text(f"{self.button_command[1]}", button_2_xy[0] + 75, button_2_xy[1] + 35)
        self.draw_text(f"{self.button_command[2]}", button_3_xy[0] + 75, button_3_xy[1] + 35)
        self.draw_text(f"{self.button_command[3]}", button_4_xy[0] + 75, button_4_xy[1] + 35)

        pygame.display.update()

class CreditsMenu(StartMenu):
    def __init__(self, screen, clock, font, colour):
        StartMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["back"]
        self.title = "Credits"
        self.widget_text = ["Frazer Mills", "Person x"]

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        creator_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        creator = pygame.Rect(creator_xy[0], creator_xy[1], self.button_width, self.button_height)

        speical_thanks_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        speical_thanks = pygame.Rect(speical_thanks_xy[0], speical_thanks_xy[1], self.button_width, self.button_height) 
        
        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]
                print("back button pressed")

        pygame.draw.rect(self.screen, (255, 0, 0), creator)
        pygame.draw.rect(self.screen, (255, 0, 0), speical_thanks)

        pygame.draw.rect(self.screen, (255, 0, 0), button_1)

        self.draw_text(f"{self.title}", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text(f"{self.widget_text[0]}", creator_xy[0] + 75, creator_xy[1] + 35)
        self.draw_text(f"{self.widget_text[1]}", speical_thanks_xy[0] + 75, speical_thanks_xy[1] + 35)
        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + 75, button_1_xy[1] + 35)

        pygame.display.update()

class DifficultyMenu(StartMenu):
    def __init__(self, screen, clock, font, colour):
        StartMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["easy", "normal", "hard", "very hard", "back"]
        self.title = "difficulty menu"

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)        

        button_4_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 200)
        button_4 = pygame.Rect(button_4_xy[0], button_4_xy[1], self.button_width, self.button_height)

        button_5_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 300)
        button_5 = pygame.Rect(button_5_xy[0], button_5_xy[1], self.button_width, self.button_height)

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]

        elif button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]

        elif button_4.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[3]
                
        elif button_5.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[4]
                
        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), button_2)
        pygame.draw.rect(self.screen, (255, 0, 0), button_3)
        pygame.draw.rect(self.screen, (255, 0, 0), button_4)
        pygame.draw.rect(self.screen, (255, 0, 0), button_5)

        self.draw_text(f"{self.title}", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text(f"{self.button_command[0]}", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text(f"{self.button_command[1]}", button_2_xy[0] + 75, button_2_xy[1] + 35)
        self.draw_text(f"{self.button_command[2]}", button_3_xy[0] + 75, button_3_xy[1] + 35)
        self.draw_text(f"{self.button_command[3]}", button_4_xy[0] + 75, button_4_xy[1] + 35)
        self.draw_text(f"{self.button_command[4]}", button_5_xy[0] + 75, button_5_xy[1] + 35)

        pygame.display.update()


class SnakeColourMenu(DifficultyMenu):
    def __init__(self, screen, clock, font, colour):
        DifficultyMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["green", "white", "pink", "blue", "back"]
        self.title = "snake colour menu"


class FruitTypeMenu(DifficultyMenu):
    def __init__(self, screen, clock, font, colour):
        DifficultyMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["apple", "banana", "orange", "blueberry", "back"]
        self.title = "snake colour menu"

