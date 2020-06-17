import pygame
import random
from pygame.locals import *
from settings import *

class Snake():
    def __init__(self, game):
        self.game = game
        self.x = random.randrange(game.rect.left+1, game.rect.right-CELL_SIZE, CELL_SIZE)
        self.y = random.randrange(game.rect.top+1, game.rect.bottom-CELL_SIZE, CELL_SIZE)
        self.body = []
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE-1, CELL_SIZE-1)
        self.rect.x = self.x
        self.rect.y = self.y
        self.length = 1
        self.dir = [0, 0]
        self.frame_rate = 105
        self.last_update = pygame.time.get_ticks()
        self.treshold = 50

    def get_body(self):
        self.body.insert(0, [self.x, self.y])
        self.body = self.body[:self.length]

    def draw(self):
        for part in self.body:
            pygame.draw.rect(self.game.screen,
                             SNAKE_COLOR,
                             (part[0], part[1], CELL_SIZE-1, CELL_SIZE-1))

    def eat(self):
        if self.rect.colliderect(self.game.apple.rect):
            self.game.window.pickup_snd.play()
            self.game.apple = Apple(self.game)
            for part in self.body:
                if self.game.apple.rect.collidepoint(part[0], part[1]):
                    self.game.apple = Apple(self.game)

            self.length += 1
            self.game.score += 10

    def update(self):
        if self.game.score > self.treshold:
            self.frame_rate -= 5
            self.treshold += 50

        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.eat()
            self.get_body()

            self.x += self.dir[0]*CELL_SIZE
            self.y += self.dir[1]*CELL_SIZE

            if self.rect.right > self.game.rect.right:
                self.game.die()
            if self.rect.bottom > self.game.rect.bottom:
                self.game.die()
            if self.rect.left < self.game.rect.left:
                self.game.die()
            if self.rect.top < self.game.rect.top:
                self.game.die()

            self.rect.x = self.x
            self.rect.y = self.y

            if self.length > 1:
                for pos in self.body:
                    if self.rect.collidepoint(pos[0], pos[1]):
                        self.game.die()

    def move(self, dx, dy):
        self.dir = [dx, dy]

class Apple():
    def __init__(self, game):
        self.game = game
        self.x = random.randrange(game.rect.left+1, game.rect.right-CELL_SIZE, CELL_SIZE)
        self.y = random.randrange(game.rect.top+1, game.rect.bottom-CELL_SIZE, CELL_SIZE)
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE-1, CELL_SIZE-1)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.game.screen, APPLE_COLOR, self.rect)

    def update(self):
        pass
