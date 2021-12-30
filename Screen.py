import pygame


class Screen:
    static_screen = None

    def __init__(self, size, color):
        self.top = 0
        self.bottom = size[1]
        self.left = 0
        self.right = size[0]
        self.color = color
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(color)

    @staticmethod
    def create_screen(size: tuple[int, int], color: tuple[int, int, int]):
        Screen.static_screen = Screen(size, color)

    @staticmethod
    def get_screen():
        return Screen.static_screen.screen

    @staticmethod
    def get_color():
        return Screen.static_screen.color

    @staticmethod
    def get_top():
        return Screen.static_screen.top

    @staticmethod
    def get_bottom():
        return Screen.static_screen.bottom

    @staticmethod
    def get_left():
        return Screen.static_screen.left

    @staticmethod
    def get_right():
        return Screen.static_screen.right
