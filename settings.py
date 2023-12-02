import pygame 
import time

class Settings():

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        # Sounds
        self.btn_click_sound = pygame.mixer.Sound("assets/sounds/btn.wav")

        # Game Title
        self.game_title = "AIM TRAINING"
        self.title_font = pygame.font.Font("assets/fonts/paraxome-font/Paraxome-K7YGD.ttf", 104)

        # Scren Settings
        self.screen_width = 800
        self.screen_height = 540
        self.bg_color = (0, 34, 56)

        # Button Settings
        self.button_font = pygame.font.SysFont("sans-serif", 32)


        # Target Settings
        self.target_max_size = 30
        self.growth_rate = 0.275
        self.target_color1 = (255, 0, 0)
        self.target_color2 = (255, 255, 255)

        # Custom events
        self.TARGET_INCRESING = 400
        self.TARGET_EVENT = pygame.USEREVENT
        self.TARGET_PADDING = 20
        
        # Game Stats
        self.elapsed_time = 0
        self.target_pressed = 0
        self.clicks = 0
        self.misses = 0
        self.lives = 3
        self.start_time = time.time()

class Button():

    def __init__(self, text, x, y, width= 100, height= 40, function = None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 87, 34)
        self.hover_color = (230,230,230)
        self.function = function
        self.rect = pygame.Rect(x, y, width, height)

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def draw(self, screen, font):
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
            # text_surface = font.render(self.text, True, (0, 0, 0))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            # text_surface = font.render(self.text, True, (255, 255, 255))
        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x + (self.width - text_surface.get_width()) // 2, self.y + (self.height - text_surface.get_height()) // 2))
    

class Label():

    def __init__(self, x, y, text, font=None, font_size=32, color=(255, 0, 0), Flag=False):
        self.font = font
        self.text = self.font.render(text, True, color)
        self.position = (x, y)

    def update_text(self, text, color=(255, 0, 0)):
        self.text = self.font.render(text, True, color)

    def draw(self, screen):
        screen.blit(self.text, self.position)