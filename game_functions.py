import pygame,sys

def check_events(screen, settings, game):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, game):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    # game.draw()
    # Make the most recently drawn screen visible.
    pygame.display.flip()