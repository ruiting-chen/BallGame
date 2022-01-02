import pygame

from Ball import Ball
from Screen import Screen


class Block:
    ball: Ball

    def __init__(self, top, bottom, left, right, color, ball):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.color = color
        self.ball = ball

    def draw(self):
        pygame.draw.rect(Screen.get_screen(), self.color,
                         ((self.right + self.left) // 2, (self.bottom + self.top) // 2,
                          self.right - self.left, self.bottom - self.top))

    def update_ball_pos(self, time, ball):
        radius = ball.get_size()
        old_x_position = ball.get_x_position()
        old_x_velocity = ball.get_x_velocity()
        old_y_position = ball.get_y_position()
        old_y_velocity = ball.get_y_velocity()
        (new_x_position, new_x_velocity) = ball.calculate_x_pos_vol(time)
        (new_y_position, new_y_velocity) = ball.calculate_y_pos_vol(time)
        if old_x_position + radius < self.left < new_x_position + radius:
            if self.top < new_y_position < self.bottom:
                ball.set_x_position(self.left - ball.get_size())
                ball.set_x_velocity(0)
                print("block x first")
        elif new_x_position - radius < self.right < old_x_position - radius:
            if self.top < new_y_position < self.bottom:
                ball.set_x_position(self.right + ball.get_size())
                ball.set_x_velocity(0)
                print("block x second")
        elif self.left < new_x_position < self.right:
            if old_y_position + radius < self.top < new_y_position + radius:
                ball.set_y_position(self.bottom - ball.get_size())
                ball.set_y_velocity(0)
                print("block y first")
            elif new_y_position - radius < self.bottom < old_y_position - radius:
                new_y_velocity = - new_y_velocity
                ball.set_y_position(ball.get_y_position() + new_y_velocity * time +
                                    0.5 * 9.8 * (time ** 2))
                ball.set_y_velocity(new_y_velocity + time * 9.8)
                print("screen y second")
        else:
            ball.set_x_position(new_x_position)
            ball.set_x_velocity(new_x_velocity)
            ball.set_y_position(new_y_position)
            ball.set_y_velocity(new_y_velocity)
            print("else")

