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
                         (self.left, self.top, self.right - self.left, self.bottom - self.top))

    def update_ball(self, time, ball):
        radius = ball.get_size()
        old_x_position, old_y_position = ball.get_curr_x_position(), ball.get_curr_y_position()
        new_x_position, new_x_velocity = ball.get_next_x_position(), ball.get_next_x_velocity()
        new_y_position, new_y_velocity = ball.get_next_y_position(), ball.get_next_y_velocity()
        if self.left <= new_x_position <= self.right:
            if old_y_position + radius < self.top < new_y_position + radius:
                ball.set_next_y_position(self.top - ball.get_size())
                ball.set_next_y_velocity(0)
                print("block y first")
            elif new_y_position - radius < self.bottom < old_y_position - radius:
                new_y_velocity = - new_y_velocity
                ball.set_next_y_position(ball.get_curr_y_position() + new_y_velocity * time +
                                         0.5 * 9.8 * (time ** 2))
                ball.set_next_y_velocity(new_y_velocity + time * 9.8)
                print("screen y second")
        else: # new_x_position < self.left or new_x_position > self.right
            if old_x_position + radius < self.left < new_x_position + radius:
                if self.top < new_y_position < self.bottom:
                    ball.set_next_x_position(self.left - ball.get_size())
                    ball.set_next_x_velocity(0)
                    print("block x first")
            elif new_x_position - radius < self.right < old_x_position - radius:
                if self.top < new_y_position < self.bottom:
                    ball.set_next_x_position(self.right + ball.get_size())
                    ball.set_next_x_velocity(0)
                    print("block x second")
            elif new_x_position - radius > self.right > old_x_position - radius or \
                    old_x_position + radius > self.left > new_x_position + radius:
                ball.set_next_y_velocity(new_y_velocity + time * 9.8)


