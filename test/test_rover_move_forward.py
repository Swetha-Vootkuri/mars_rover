import unittest

from parameterized import parameterized
import parametrize

from src.direction import Direction
from src.rover import Rover


class RoverMoveForward(unittest.TestCase):

    def test_move_forward_facing_north(self):
        rover = Rover(1, 1, Direction.NORTH)
        rover.receive_command("F")
        self.assertEqual((1, 2), rover.get_position())

    def test_move_forward_facing_east(self):
        rover = Rover(1, 1, Direction.EAST)
        rover.receive_command("F")
        self.assertEqual((2, 1), rover.get_position())

    def test_move_forward_facing_south(self):
        rover = Rover(1, 1, Direction.SOUTH)
        rover.receive_command("F")
        self.assertEqual((1, 0), rover.get_position())

    @parameterized.expand([(Direction.NORTH, (1, 2)),
                           (Direction.EAST, (2, 1)),
                           (Direction.SOUTH, (1, 0))])
    def test_move_forward(self, direction, expected_final_position):
        rover = Rover(1, 1, direction)
        rover.receive_command("F")
        self.assertEqual(expected_final_position, rover.get_position())
