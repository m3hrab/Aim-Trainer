import pygame,sys
import random
from game import Target

def check_events(screen, settings, game):
    """Respond to keypresses and mouse events."""
    
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            settings.clicks += 1

        
        if event.type == pygame.MOUSEMOTION:
            game.cursor.update_pos(pygame.mouse.get_pos())

        if event.type == settings.TARGET_EVENT:
            x = random.randint(settings.TARGET_PADDING, settings.screen_width - settings.TARGET_PADDING)
            y = random.randint(settings.TARGET_PADDING, settings.screen_height - settings.TARGET_PADDING)
            game.targets.append(Target(x, y))

    for target in game.targets:
        target.update(settings)

        if target.size <= 0 :
            game.targets.remove(target)
            settings.misses += 1

        if click and target.collide(pygame.mouse.get_pos()):
            game.targets.remove(target)
            settings.target_pressed += 1
            # settings.misses -= 1

    if settings.misses >= 3:
        print("Game Over")

def update_screen(screen, settings, game):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    game.draw()
    game.cursor.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()