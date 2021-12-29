from abc import abstractmethod


class Movable:
    def __init__(self, x_position, y_position, size, color, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def calculate_position(self, screen_top, bottom, time):
        self.x_position = self.x_position + self.x_velocity * time
        if self.y_position > bottom:
            self.y_position = bottom
            self.y_velocity = 0
            print("first")
        elif self.y_position < screen_top:
            self.y_velocity = - self.y_velocity
            self.y_position = self.y_position - self.y_velocity * time - 0.5 * 9.8 * (time ** 2)
            print("second")
        elif self.y_velocity != 0:
            self.y_position = self.y_position - self.y_velocity * time - 0.5 * 9.8 * (time ** 2)
            self.y_velocity = self.y_velocity - time * 9.8
            print("third")

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_x_velocity(self):
        return self.x_velocity

    def set_x_velocity(self, x_velocity):
        self.x_velocity = x_velocity

    def get_y_velocity(self):
        return self.y_velocity

    def set_y_velocity(self, y_velocity):
        if self.y_velocity == 0:
            self.y_velocity = y_velocity

    # @abstractmethod
    # def draw(self):
    #     pass