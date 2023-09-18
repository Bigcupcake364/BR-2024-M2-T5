import pygame
import os

pygame.mixer.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_SHIELD_ACT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1ShieldU.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2ShieldU.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]
JUMPING = [pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png")),
           pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
]
JUMPING_SHIELD = [pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png")),
                  pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
]
JUMPING_SHIELD_ACT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShieldU.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShieldU.png"))
]

JUMPING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
]
JUMPING_SPEED = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpSpeed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump2Speed.png")),
]

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_SHIELD_ACT = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1ShieldU.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2ShieldU.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_SPEED = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Speed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Speed.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CACTUS_DEATH = [
    "I think you can't touch the sparks",
    "That must hurt",
    "Stay away from sparks!"
]

BIRD_DEATH = [
    "You shouldn't ride on it",
    "You were pecked to death", 
    "You died of bird flu"
]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/speed.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
DINO_DAMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDamage.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

FONT_FILE = os.path.join(IMG_DIR, 'Other/bebasNeue.ttf')

PLAY_MUSIC = os.path.join(IMG_DIR, 'Other/castlevania.mp3')
MAIN_MUSIC = os.path.join(IMG_DIR, 'Other/melancolic.mp3')
DEATH_SOUND = os.path.join(IMG_DIR, 'Other/death_sound.mp3')
MENU_MUSIC = os.path.join(IMG_DIR, 'Other/castlevania2.mp3')

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
FLY_TYPE = "fly"
SPEED_TYPE = "speed"
HEART_TYPE = "heart"

