import pygame,sys
import time, math
import random
from game import Target
from settings import Label

def format_time(secs):
    miliseconds = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(round(secs) // 60)

    return f"{minutes:02d}:{seconds:02d}:{miliseconds:01d}"
    
def draw_game_status(screen, settings, game):
    # pygame.draw.rect(screen, (255, 255, 255), (0, 0, settings.screen_width, 50))
    time_label = Label(20, 10, f"Time: {format_time(settings.elapsed_time)}", settings.button_font, 32, (255,255, 255))
    time_label.draw(screen)

    speed = round(settings.target_pressed / settings.elapsed_time, 1)
    speed_label = Label(200, 10, f"Speed: {speed} t/s", settings.button_font, 32, (255,255, 255))
    speed_label.draw(screen)

    hits_label = Label(400, 10, f"Hits: {settings.target_pressed}", settings.button_font, 32, (255,255, 255))
    hits_label.draw(screen)

    for i in range(settings.lives):
        screen.blit(game.heart_image, (settings.screen_width - 50 - i * 35, 10))




def check_events(screen, settings, game):
    """Respond to keypresses and mouse events."""
    
    click = False
    settings.elapsed_time = time.time() - settings.start_time

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
            y = random.randint(settings.TARGET_PADDING + 70, settings.screen_height - settings.TARGET_PADDING)
            game.targets.append(Target(x, y))

    for target in game.targets:
        target.update(settings)

        if target.size <= 0 :
            game.targets.remove(target)
            settings.misses += 1

        if click and target.collide(pygame.mouse.get_pos()):
            settings.btn_click_sound.play()
            game.targets.remove(target)
            settings.target_pressed += 1

    if settings.misses >= settings.lives:
        pass 


def update_screen(screen, settings, game):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    game.draw()
    game.cursor.draw(screen)

    # Draw the game status
    draw_game_status(screen, settings, game)


    # Make the most recently drawn screen visible.
    pygame.display.flip()

