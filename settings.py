from os import path

# SCREEN SETTINGS
SCREEN_WIDTH = 16*60
SCREEN_HEIGHT = 16*45

# GENERAL SETTINGS
FPS = 30
FONT_PATH = path.join(path.dirname(__file__), "From Cartoon Blocks.ttf")
TEXT_SIZE = 54
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
SNAKE_COLOR = (0, 204, 68)
APPLE_COLOR = (204, 41, 0)
FIELD = (198, 140, 83)
BG_COLOR = (77, 51, 25)
GREY = (204, 204, 204)
TEXT_COLOR = GREY

# images

BG_PATH = path.join(path.dirname(__file__), "mosaic.jpg")
