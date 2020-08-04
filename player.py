class Player:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0

    def get_position(self):
        return self.x_position, self.y_position

    def go_up(self):
        self.x_position += 1

    def go_left(self):
        self.y_position -= 1

    def go_down(self):
        self.x_position -= 1

    def go_right(self):
        self.y_position += 1

