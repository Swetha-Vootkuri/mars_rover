import unittest

from src.direction import Direction
from src.rover import Rover


class InitialiseRoverTest(unittest.TestCase):

    def test_initialise_rover(self):
        rover = Rover(2, 3, Direction.NORTH)
        self.assertEqual((2, 3), rover.get_position())

    def test_initialise_rover_heading(self):
        rover = Rover(2, 3, Direction.NORTH)
        self.assertEqual(Direction.NORTH, rover.get_heading())

