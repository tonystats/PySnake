import pygame
from settings import *
from buttons import Button
from game import Game

class Window():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.running = True
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(pygame.font.match_font(FONT), TEXT_SIZE)
        self.make_buttons()
        self.state = 'intro'

    def new(self):
        self.game = Game(self, CELL_SIZE*4, CELL_SIZE*4,
                         SCREEN_WIDTH - CELL_SIZE*8,
                         SCREEN_HEIGHT - CELL_SIZE*8)

    def run(self):
        while self.running:
            self.get_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def get_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            if self.state == 'play':
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    self.game.snake.move(1, 0)
                if keys[pygame.K_LEFT]:
                    self.game.snake.move(-1, 0)
                if keys[pygame.K_UP]:
                    self.game.snake.move(0, -1)
                if keys[pygame.K_DOWN]:
                    self.game.snake.move(0, 1)


    def update(self):
        if self.state == 'intro':
            self.play_button.update()
        elif self.state == 'play':
            self.game.update()

    def make_buttons(self):
        self.play_button = Button(self.screen, self.width//2, self.height//2,
            16*8, 16*5, GREEN, LIGHTGREEN, "PLAY", self.play)

    def draw(self):
        self.screen.fill(WHITE)
        if self.state == 'intro':
            self.play_button.draw()
        elif self.state == 'play':
            self.game.draw()
        pygame.display.flip()

    def play(self):
        self.state = 'play'
        self.new()

    def quit(self):
        self.running = False

    def play_again(self):
        self.game = Game(self, CELL_SIZE*4, CELL_SIZE*4,
                         SCREEN_WIDTH - CELL_SIZE*8,
                         SCREEN_HEIGHT - CELL_SIZE*8)

if __name__ == "__main__":
    win = Window()
    win.run()
