import pygame,sys
from settings import Button, Label 

class Mainmenu():

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        # title position
        x = self.settings.screen_width/2 - 200
        y = self.settings.screen_height/2 - 140
        self.title = Label(x, y, self.settings.game_title, self.settings.title_font)

        # play button position
        x = self.settings.screen_width/2 - 80
        y = self.settings.screen_height/2 + 40
        self.play_button = Button("Play", x, y, 160, 40)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.is_over(pygame.mouse.get_pos()):
                        self.settings.btn_click_sound.play()
                        return True
                
            self.screen.fill(self.settings.bg_color)
            self.title.draw(self.screen)
            self.play_button.draw(self.screen, self.settings.button_font)
            pygame.display.flip()