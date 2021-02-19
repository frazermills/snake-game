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

    def setup(self):
        pygame.init()
        pygame.display.set_caption("start menu")
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
        
        self.draw_text("Snake game - by Frazer Mills", self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text("start game", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text("settings", button_2_xy[0] + 75, button_2_xy[1] + 35)
        self.draw_text("quit game", button_3_xy[0] + 75, button_3_xy[1] + 35)
        self.draw_text("credits", button_3_xy[0] + 75, button_4_xy[1] + 35)

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

class SettingsMenu(StartMenu):
    def __init__(self, screen, clock, font, colour):
        StartMenu.__init__(self, screen, clock, font, colour)
        self.button_command = ["button 1", "button 2", "button 3"]
        
    def setup(self):
        pygame.init()
        pygame.display.set_caption("settings menu")
        self.screen.fill((0,0,0))

    def update(self):
        mousex, mousey = pygame.mouse.get_pos()

        button_1_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - 100)
        button_1 = pygame.Rect(button_1_xy[0], button_1_xy[1], self.button_width, self.button_height)

        button_2_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2))
        button_2 = pygame.Rect(button_2_xy[0], button_2_xy[1], self.button_width, self.button_height)

        button_3_xy = ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) + 100)
        button_3 = pygame.Rect(button_3_xy[0], button_3_xy[1], self.button_width, self.button_height)        

        if button_1.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]
                print("button 1 pressed")

        elif button_2.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                print("button 2 pressed")
                
        elif button_3.collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[2]
                print("button 3 pressed")

        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), button_2)
        pygame.draw.rect(self.screen, (255, 0, 0), button_3)
        
        self.draw_text("button 1", button_1_xy[0] + 75, button_1_xy[1] + 35)
        self.draw_text("button 2", button_2_xy[0] + 75, button_2_xy[1] + 35)
        self.draw_text("button 3", button_3_xy[0] + 75, button_3_xy[1] + 35)

        pygame.display.update()
