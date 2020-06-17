from settings import *
import pygame

class Button():
    def __init__(self, screen, x, y, width, height, color, hcolor, text, func):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hcolor = hcolor
        self.text = text
        self.func = func
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)
        self.font = pygame.font.Font(pygame.font.match_font(FONT), TEXT_SIZE)

    def highlighted(self):
        mouse_pos = pygame.mouse.get_pos()
        costraint = [range(self.rect.left, self.rect.right-1),
                     range(self.rect.top, self.rect.bottom-1)]
        if mouse_pos[0] in costraint[0] and mouse_pos[1] in costraint[1]:
            return True
        return False

    def draw_text(self, text, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x, self.y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        if self.highlighted():
            pygame.draw.rect(self.screen, self.hcolor, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)

        self.draw_text(self.text, WHITE)

    def update(self):
        mouse_events = pygame.mouse.get_pressed()
        if mouse_events[0] and self.highlighted():
            self.func()
