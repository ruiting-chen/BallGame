class Movable:
    def __init__(self, size, color, x_position, y_position, x_velocity, y_velocity):
        self.size = size
        self.color = color
        self.curr_x_position = x_position
        self.curr_y_position = y_position
        self.curr_x_velocity = x_velocity
        self.curr_y_velocity = y_velocity
        self.next_x_position = None
        self.next_y_position = None
        self.next_x_velocity = None
        self.next_y_velocity = None

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_curr_x_position(self):
        return self.curr_x_position

    def get_curr_x_velocity(self):
        return self.curr_x_velocity

    def get_next_x_position(self):
        return self.next_x_position

    def get_next_x_velocity(self):
        return self.next_x_velocity

    def get_curr_y_position(self):
        return self.curr_y_position

    def get_curr_y_velocity(self):
        return self.curr_y_velocity

    def get_next_y_position(self):
        return self.next_y_position

    def get_next_y_velocity(self):
        return self.next_y_velocity

    def set_curr_x_position(self, x_position):
        self.curr_x_position = x_position

    def set_curr_x_velocity(self, x_velocity):
        self.curr_x_velocity = x_velocity

    def set_next_x_position(self, x_position):
        self.next_x_position = x_position

    def set_next_x_velocity(self, x_velocity):
        self.next_x_velocity = x_velocity

    def set_curr_y_position(self, y_position):
        self.curr_y_position = y_position

    def set_curr_y_velocity(self, y_velocity):
        self.curr_y_velocity = y_velocity

    def set_next_y_position(self, y_position):
        self.next_y_position = y_position

    def set_next_y_velocity(self, y_velocity):
        self.next_y_velocity = y_velocity

    def ball_move(self, x_velocity):
        if -10 <= self.curr_x_velocity + x_velocity <= 10:
            self.curr_x_velocity = self.curr_x_velocity + x_velocity

    def ball_jump(self, y_velocity):
        if self.curr_y_velocity == 0:
            self.curr_y_velocity = y_velocity

    def calculate_pos_velo(self, time):
        self.calculate_x_pos_velo(time)
        self.calculate_y_pos_velo(time)

    def calculate_x_pos_velo(self, time):
        if self.curr_x_velocity != 0:
            direction = - self.curr_x_velocity // abs(self.curr_x_velocity)
            resistance = direction * 3

            self.next_x_position = self.curr_x_position + self.curr_x_velocity * time + \
                                   0.5 * resistance * (time ** 2)

            temp_x_velocity = self.curr_x_velocity + time * resistance
            if temp_x_velocity * self.curr_x_velocity > 0:
                self.next_x_velocity = temp_x_velocity
                print("if")
            else:
                self.next_x_velocity = 0
                print("else")
            # return self.next_x_position, self.next_x_velocity
            print("x if")
        else:
            self.next_x_position, self.next_x_velocity = self.curr_x_position, self.curr_x_velocity
            print("x else")
        print(f"new_x_position {self.next_x_position}, new_x_velocity {self.next_x_velocity}")
        # return self.curr_x_position, self.curr_x_velocity

    def calculate_y_pos_velo(self, time):
        if self.curr_y_velocity != 0:
            self.next_y_position = self.curr_y_position + self.curr_y_velocity * time + 0.5 * 9.8 * (time ** 2)
            self.next_y_velocity = self.curr_y_velocity + time * 9.8
            print("y if")
            # return self.next_y_position, self.next_y_velocity
        else:
            self.next_y_position, self.next_y_velocity = self.curr_y_position, self.curr_y_velocity
            print("y else")
        print(f"new_y_position {self.next_y_position}, new_y_velocity {self.next_y_velocity}")
        # return self.curr_y_position, self.curr_y_velocity

    def update_pos_velo(self):
        self.curr_x_position = self.next_x_position
        self.curr_y_position = self.next_y_position
        self.curr_x_velocity = self.next_x_velocity
        self.curr_y_velocity = self.next_y_velocity
        # self.next_x_position = None
        # self.next_y_position = None
        # self.next_x_velocity = None
        # self.next_y_velocity = None
