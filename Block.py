import pygame

from Screen import Screen


class Block:
    def __init__(self, top, bottom, left, right, color):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.color = color

    def draw(self):
        pygame.draw.rect(Screen.get_screen(), self.color,
                         ((self.right + self.left) // 2, (self.bottom + self.top) // 2,
                          self.right - self.left, self.bottom - self.top))
