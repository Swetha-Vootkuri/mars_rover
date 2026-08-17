from src.direction import Direction


class Rover:
    def __init__(self, position_x, position_y, heading):
        self.heading = heading
        self.position_x = position_x
        self.position_y = position_y

    def get_position(self):
        return self.position_x, self.position_y

    def get_heading(self):
        return self.heading

    def receive_command(self, command):
        if self.get_heading() == Direction.NORTH:
            self.position_y += 1
        elif self.get_heading() == Direction.EAST:
            self.position_x += 1
        else:
            self.position_y -= 1

