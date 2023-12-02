import pygame,sys
import time, math
import random
from game import Target, HighScore
from settings import Label, Button

def format_time(secs):
    miliseconds = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(round(secs) // 60)

    return f"{minutes:02d}:{seconds:02d}.{miliseconds:02d}"
    
def draw_game_status(screen, settings, game):
    time_label = Label(20, 10, f"Time: {format_time(settings.elapsed_time)}", settings.button_font, 32, (255,255, 255))
    time_label.draw(screen)

    hits_label = Label(400, 10, f"Hits: {settings.target_pressed}", settings.button_font, 32, (255,255, 255))
    hits_label.draw(screen)

    speed = round(settings.target_pressed / settings.elapsed_time, 1)
    speed_label = Label(200, 10, f"Speed: {speed} t/s", settings.button_font, 32, (255,255, 255))
    speed_label.draw(screen)

    for i in range(settings.lives - settings.misses):
        screen.blit(game.heart_image, (settings.screen_width - 50 - i * 35, 10))
    

def game_over_screen(screen, settings, game):
    screen.fill(settings.bg_color)
    pygame.mouse.set_visible(True)

    x = settings.screen_width/2 - 110
    y = settings.screen_height/2 - 140

    if settings.elapsed_time > settings.high_score.score:
        settings.high_score.update(settings.elapsed_time)
        high_score_label = Label(x-140, y, f"Congratulation! New Highest Time: {format_time(settings.elapsed_time)}", settings.button_font, 32, (255,255, 255))
        high_score_label.draw(screen)
        settings.high_score_sound.play()
    else:
        high_score_label = Label(x-20, y, f"Highest Time: {format_time(settings.high_score.score)}", settings.button_font, 32, (255,255, 255))
        high_score_label.draw(screen)


    accuracy = round(settings.target_pressed / settings.clicks * 100, 1)
    accuracy_label = Label(x, y+130, f"Accuracy: {accuracy}%", settings.button_font, 32, (255,255, 255))
    accuracy_label.draw(screen)

    time_label = Label(x+15, y+80, f"Time: {format_time(settings.elapsed_time)}", settings.button_font, 32, (255,255, 255))
    time_label.draw(screen)

    hits_label = Label(x+45, y+180, f"Hits: {settings.target_pressed}", settings.button_font, 32, (255,255, 255))
    hits_label.draw(screen)

    speed = round(settings.target_pressed / settings.elapsed_time, 1)    
    speed_label = Label(x+15, y+230, f"Speed: {speed} t/s", settings.button_font, 32, (255,255, 255))
    speed_label.draw(screen)




    play_again_button = Button("Play Again", x, y+290, 220, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.is_over(pygame.mouse.get_pos()):
                        settings.btn_click_sound.play()
                        game.reset()
                        pygame.mouse.set_visible(True)

                        return True

        play_again_button.draw(screen, settings.button_font)
        pygame.display.flip()


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
            settings.lose_life.play()

        if click and target.collide(pygame.mouse.get_pos()):
                settings.btn_click_sound.play()
                game.targets.remove(target)
                settings.target_pressed += 1
                settings.hit.play()


    if settings.misses >= settings.lives:
        game_over_screen(screen, settings, game)
        pygame.display.flip()



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

