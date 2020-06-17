import pygame
import random
from settings import *
from pygame.locals import *
from sprites import Snake, Apple
from buttons import Button

class Game():
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.borders = pygame.Rect(self.x - BORDER_THICKNESS+1,
                                   self.y - BORDER_THICKNESS+1,
                                   self.width + BORDER_THICKNESS*2-2,
                                   self.height + BORDER_THICKNESS*2-2)
        self.screen = window.screen
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.score = 0
        self.playing = True
        #self.rows = self.height//CELL_SIZE
        #self.cols = self.width//CELL_SIZE

    def update(self):
        if self.playing:
            self.snake.update()
            self.apple.update()
        else:
            self.quit_button.update()
            self.play_again_button.update()


    def draw_grid(self):
        for x in range(self.rect.left, self.rect.right+1, CELL_SIZE):
            pygame.draw.line(self.screen, BLACK,
                            (x, self.rect.top), (x, self.rect.bottom))
        for y in range(self.rect.top, self.rect.bottom+1, CELL_SIZE):
            pygame.draw.line(self.screen, BLACK,
                            (self.rect.left, y), (self.rect.right, y))

    def draw_text(self, text, color, x, y):
        text_surface = self.window.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        if self.playing:
            pygame.draw.rect(self.screen, FIELD, self.rect)
            pygame.draw.rect(self.screen, BLACK, self.borders, BORDER_THICKNESS)
            self.draw_grid()
            self.snake.draw()
            self.apple.draw()
            self.draw_text("{}".format(self.score), TEXT_COLOR, SCREEN_WIDTH//2, 32)
        else:
            self.screen.fill(BG_COLOR)
            self.draw_text("YOU DIED LOL", TEXT_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//4)
            self.draw_text("Your score: {}".format(self.score), TEXT_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
            self.quit_button.draw()
            self.play_again_button.draw()


    def die(self):
        pygame.time.wait(400)
        self.playing = False
        self.quit_button = Button(self.screen, SCREEN_WIDTH*3/4,
                                  SCREEN_HEIGHT*3/4, CELL_SIZE*6, CELL_SIZE*4, RED, LIGHTRED,
                                  "QUIT", self.window.quit)
        self.play_again_button = Button(self.screen, SCREEN_WIDTH//4,
                                  SCREEN_HEIGHT*3/4, CELL_SIZE*14, CELL_SIZE*4, GREEN, LIGHTGREEN,
                                  "PLAY AGAIN", self.window.play_again)
