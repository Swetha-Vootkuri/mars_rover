import unittest


class Rover:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def get_position(self):
        return self.position_x, self.position_y


class InitialiseRoverTest(unittest.TestCase):

    def test_initialise_rover(self):
        rover = Rover(2, 3)
        self.assertEqual((2, 3), rover.get_position())
