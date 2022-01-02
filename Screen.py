import pygame

# from Ball import Ball


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

    @staticmethod
    def update_ball_pos(time, ball):
        Screen.static_screen.update_x_position(time, ball)
        Screen.static_screen.calculate_y_position(time, ball)

    def update_x_position(self, time, ball):
        (new_x_position, new_x_velocity) = ball.calculate_x_pos_vol(time)
        if new_x_position > Screen.static_screen.right - ball.get_size():
            ball.set_x_position(Screen.static_screen.right - ball.get_size())
            ball.set_x_velocity(0)
            print("screen x first")
        elif new_x_position < Screen.static_screen.left + ball.get_size():
            ball.set_x_position(Screen.static_screen.left + ball.get_size())
            ball.set_x_velocity(0)
            print("screen x second")
        else:
            ball.set_x_position(new_x_position)
            ball.set_x_velocity(new_x_velocity)
            print("screen x third")

    def calculate_y_position(self, time, ball):
        (new_y_position, new_y_velocity) = ball.calculate_y_pos_vol(time)
        if new_y_position > Screen.static_screen.bottom - ball.get_size():
            ball.set_y_position(Screen.static_screen.bottom - ball.get_size())
            ball.set_y_velocity(0)
            print("screen y first")
        elif new_y_position < Screen.static_screen.top + ball.get_size():
            new_y_velocity = - new_y_velocity
            ball.set_y_position(ball.get_y_position() + new_y_velocity * time +
                                0.5 * 9.8 * (time ** 2))
            ball.set_y_velocity(new_y_velocity + time * 9.8)
            print("screen y second")
        else:
            ball.set_y_position(new_y_position)
            ball.set_y_velocity(new_y_velocity)
            print("screen y third")
