import pygame, sys, math, time

class Cursor():
    def __init__(self, image):
        self.image = pygame.image.load("assets/images/cursor.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = pygame.mouse.get_pos()


    def update_pos(self, pos):
        self.image_rect.center = pos

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)


class Target():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self, settings):
        if self.size + settings.growth_rate >= settings.target_max_size:
            self.grow = False
        
        if self.grow:
            self.size += settings.growth_rate
        else:
            self.size -= settings.growth_rate


    def collide(self, target):
        distance = math.sqrt((self.x - target[0]) ** 2 + (self.y - target[1]) ** 2)
        return distance <= self.size

    def draw(self, screen, settings):
        pygame.draw.circle(screen, settings.target_color1, (self.x, self.y), self.size)
        pygame.draw.circle(screen, settings.target_color2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(screen, settings.target_color1, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(screen, settings.target_color2, (self.x, self.y), self.size * 0.4)
        pygame.draw.circle(screen, settings.target_color1, (self.x, self.y), self.size * 0.2)

class HighScore():
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.score = float(file.read())
        except FileNotFoundError:
            self.score = 0.0

    def update(self, new_score):
        if new_score > self.score:
            self.score = new_score
            with open(self.filename, 'w') as file:
                file.write(str(self.score))


class Game():
    
        def __init__(self, settings, screen) -> None:
            self.settings = settings
            self.screen = screen
            self.cursor = Cursor("assets/images/cursor.png")
            self.heart_image = pygame.image.load("assets/images/heart.png")
            self.targets = []
            self.reset()

        def reset(self):
            self.targets = []
            self.settings.elapsed_time = 1
            self.settings.target_pressed = 0
            self.settings.clicks = 1
            self.settings.misses = 0
            self.settings.lives = 3
            self.settings.start_time = time.time()
            pygame.mouse.set_visible(True)

        
        def draw(self):
            for target in self.targets:
                target.draw(self.screen, self.settings)