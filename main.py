import pygame
import sys
from settings import Settings
from mainmenu import Mainmenu
from game import Game
import game_functions as gf

def run_game():

    pygame.init()
    settings = Settings()

    # Create screen window for the game
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.game_title)

    mainmenu = Mainmenu(settings, screen)
    game = Game(settings, screen)

    current_screen = mainmenu
    # Start the main loop for the game
    while True:

        if current_screen == mainmenu:
            flag = current_screen.run()
            if flag:
                current_screen = game
        else:
            gf.check_events(screen, settings, game)
            gf.update_screen(screen, settings, game)


if __name__ == "__main__":
    run_game()