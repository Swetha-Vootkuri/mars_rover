import unittest

from src import rover
from src.direction import Direction
from src.rover import Rover


class RoverMoveForward(unittest.TestCase):

    def test_move_forward_facing_north(self):
        rover = Rover(1, 1, Direction.NORTH)
        rover.receive_command("F")
        self.assertEqual((1, 2), rover.get_position())
