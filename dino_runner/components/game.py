import pygame
from pygame import mixer 

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SPEED_TYPE, PLAY_MUSIC, MAIN_MUSIC
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

mixer.init()  
mixer.music.set_volume(0.3) 


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.game_speed_backup = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.death_message = ""
        self.high_score = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        

    def execute(self):
        self.running = True
        mixer.music.load(MAIN_MUSIC)
        mixer.music.play()
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        self.player.life = 2
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
        self.power_up_manager.update(self)

        if self.player.type == SPEED_TYPE:
            self.game_speed = 100
            self.score += 14
        else:
            self.game_speed = self.game_speed_backup

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 0, 0)) #FFFFFF
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, 0))
        self.screen.blit(BG, (image_width + self.x_pos_bg, 0))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, 0))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed 

    def draw_score(self):
        draw_message_component(
            f"HighScore: {self.high_score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=30,
            font_color=("#e5e619")
        )
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=70
        )

        draw_message_component(
        f"Lifes: {self.player.life}",
        self.screen,
        pos_x_center=550,
        pos_y_center=30,
        font_color=("#FF6961")
        )
            

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen,
                    font_size = 25,
                    pos_x_center = 550,
                    pos_y_center = 70
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                mixer.music.load(PLAY_MUSIC) 
                mixer.music.play()
                self.run()

    def show_menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(BG, (0, 0))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_widht = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component("Press any key to start", self.screen)
        else:
            draw_message_component(
                self.death_message, 
                self.screen, 
                pos_y_center=50
            )
            draw_message_component(
                f"Your HighScore!: {self.high_score}",
                self.screen,
                pos_y_center=half_screen_height - 200,
                font_color=("#e5e619")
            )
            draw_message_component(
                f"Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,
                pos_y_center=half_screen_height - 100,
                font_color=("#FF0000")
            )
            draw_message_component(
                "Press any key to restart", 
                self.screen, 
                pos_y_center=half_screen_height + 180)
            self.screen.blit(ICON, (half_screen_widht - 50, half_screen_height)
            )
        
        pygame.display.update()

        self.handle_events_on_menu()