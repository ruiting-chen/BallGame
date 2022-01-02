class Movable:
    def __init__(self, x_position, y_position, size, color, x_velocity, y_velocity):
        self.x_position = x_position
        self.y_position = y_position
        self.size = size
        self.color = color
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def calculate_position(self, time):
        self.calculate_x_pos_vol(time)
        self.calculate_y_pos_vol(time)

    def calculate_x_pos_vol(self, time):
        if self.x_velocity != 0:
            direction = - self.x_velocity // abs(self.x_velocity)
            resistance = direction * 3

            new_x_position = self.x_position + self.x_velocity * time + \
                              0.5 * resistance * (time ** 2)

            temp_x_velocity = self.x_velocity + time * resistance
            if temp_x_velocity * self.x_velocity > 0:
                new_x_velocity = temp_x_velocity
                print("if")
            else:
                new_x_velocity = 0
                print("else")
            print(f"new_x_position {new_x_position}, new_x_velocity {new_x_velocity}")
            return (new_x_position, new_x_velocity)
        print(f"new_x_position {self.x_position}, new_x_velocity {self.x_velocity}")
        return (self.x_position, self.x_velocity)

    def calculate_y_pos_vol(self, time):
        if self.y_velocity != 0:
            new_y_position = self.y_position + self.y_velocity * time + 0.5 * 9.8 * (time ** 2)
            new_y_velocity = self.y_velocity + time * 9.8
            print(f"new_y_position {new_y_position}, new_y_velocity {new_y_velocity}")
            return (new_y_position, new_y_velocity)
        print(f"new_y_position {self.y_position}, new_y_velocity {self.y_velocity}")
        return (self.y_position, self.y_velocity)

    def get_x_position(self):
        return self.x_position

    def set_x_position(self, x_position):
        self.x_position = x_position

    def get_y_position(self):
        return self.y_position

    def set_y_position(self, y_position):
        self.y_position = y_position

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
        self.y_velocity = y_velocity

    def ball_jump(self, y_velocity):
        if self.y_velocity == 0:
            self.y_velocity = y_velocity
