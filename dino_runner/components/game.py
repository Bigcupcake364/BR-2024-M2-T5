import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinossaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = 'freesansbold.ttf'

half_screen_heigth = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2
center = [half_screen_width, half_screen_heigth]

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.record = 0
        self.text_score = f"Score: {self.score}", True, (0, 255, 0)
        self.game_speed = 20
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0: 
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def stamp(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(self.text_screen[0], True, self.text_screen[2])
        text_rect = text.get_rect()
        text_rect.center = (self.text_position)
        self.screen.blit(text, text_rect)

    def draw_score(self):
        self.text_screen = [f"Your HighScore: {self.record}\nScore: {self.score}", True, (0, 255, 0)]
        self.text_position = 1000, 50
        self.stamp()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((0, 255, 255))

        if self.death_count == 0:
            self.text_screen = ["Press any key to start", True, (255, 0, 0)]
            self.text_position = center
            self.stamp()
        else:
            self.screen.blit(ICON, (half_screen_width - 60, half_screen_heigth - 140))
            self.text_screen = [f"Your last score was {self.last_score}\nThis is your death count: 💀{self.death_count}\nSo press any key if you want to restart", True, (0, 0, 255)]
            self.text_position = center
            self.stamp()

        pygame.display.update()
        self.handle_events_on_menu()