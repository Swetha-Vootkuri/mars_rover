import unittest

from src.rover import Rover


class InitialiseRoverTest(unittest.TestCase):

    def test_initialise_rover(self):
        rover = Rover(2, 3)
        self.assertEqual((2, 3), rover.get_position())
