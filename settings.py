from os import path

# SCREEN SETTINGS
SCREEN_WIDTH = 16*60
SCREEN_HEIGHT = 16*45

# GENERAL SETTINGS
FPS = 30
FONT_DIR = path.join(path.dirname(__file__), "fonts")
FONT_PATH = path.join(FONT_DIR, "From Cartoon Blocks.ttf")
TEXT_SIZE = 60
CELL_SIZE = 24
TITLE = "SNAKE"
BORDER_THICKNESS = 4

# COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 179, 60)
LIGHTGREEN = (128, 255, 147)
RED = (204, 41, 0)
LIGHTRED = (249, 92, 92)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (249, 246, 202)
BLUE = (0, 0, 255)
LIGHTBLUE = (77, 148, 255)
SNAKE_COLOR = (0, 153, 51)
APPLE_COLOR = (204, 41, 0)
FIELD = (198, 140, 83)
BG_COLOR = (77, 51, 25)
GREY = (204, 204, 204)
TEXT_COLOR = GREY

# images
IMG_DIR = path.join(path.dirname(__file__), "images")
BG_PATH = path.join(IMG_DIR, "mosaic.jpg")

# sounds
SND_DIR = path.join(path.dirname(__file__), "sounds")
BG_MUSIC_PATH =  path.join(SND_DIR, "bg_track.ogg")
GAME_OVER_SND_PATH = path.join(SND_DIR, "Retro_No hope.wav")
PICKUP_SND_PATH =  path.join(SND_DIR, "pickup.wav")
WAIT_SND_PATH = path.join(SND_DIR, "Jazzy Vibes #36 - Loop.mp3")
PLAY_SND_PATH = path.join(SND_DIR, "play_snd.wav")
