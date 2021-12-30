from abc import abstractmethod


class Movable:
    def __init__(self, x_position, y_position, size, color, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def calculate_position(self, left, right, top, bottom, time):
        self.calculate_x_position(left, right, time)
        self.calculate_y_position(top, bottom, time)

    def calculate_x_position(self, left, right, time):
        if self.x_position > right - self.size:
            self.x_position = right - self.size
            self.x_velocity = 0
            print("x first")
        elif self.x_position < left + self.size:
            self.x_position = left + self.size
            self.x_velocity = 0
            print("x second")
        elif self.x_velocity != 0:
            direction = - self.x_velocity // abs(self.x_velocity)
            resistance = direction * 3

            self.x_position = self.x_position + self.x_velocity * time + \
                              0.5 * resistance * (time ** 2)

            temp_x_velocity = self.x_velocity + time * resistance
            if temp_x_velocity * self.x_velocity > 0:
                self.x_velocity = temp_x_velocity
                print("if")
            else:
                self.x_velocity = 0
                print("else")
            print("x third")

    def calculate_y_position(self, top, bottom, time):
        if self.y_position > bottom - self.size:
            self.y_position = bottom - self.size
            self.y_velocity = 0
            print("first")
        elif self.y_position < top + self.size:
            self.y_velocity = - self.y_velocity
            self.y_position = self.y_position + self.y_velocity * time + 0.5 * 9.8 * (time ** 2)
            self.y_velocity = self.y_velocity + time * 9.8
            print("second")
        elif self.y_velocity != 0:
            self.y_position = self.y_position + self.y_velocity * time + 0.5 * 9.8 * (time ** 2)
            self.y_velocity = self.y_velocity + time * 9.8
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
