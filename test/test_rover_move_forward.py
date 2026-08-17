import unittest

from parameterized import parameterized
import parametrize

from src.direction import Direction
from src.rover import Rover


class RoverMoveForward(unittest.TestCase):

    @parameterized.expand([(Direction.NORTH, (1, 2)),
                           (Direction.EAST, (2, 1)),
                           (Direction.SOUTH, (1, 0))])
    def test_move_forward(self, direction, expected_final_position):
        rover = Rover(1, 1, direction)
        rover.receive_command("F")
        self.assertEqual(expected_final_position, rover.get_position())
