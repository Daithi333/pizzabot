import unittest
from unittest.mock import Mock

from pizzabot.grid import Grid
from pizzabot.validator import Validator


class TestValidator(unittest.TestCase):
    __grid = Grid(5, 5, 0, 0)
    __valid_coords = [(0, 0), (3, 2), (5, 5)]
    __one_invalid_x_axis_coord = [(0, 0), (3, 2), (5, 5), (-1, 3)]
    __one_invalid_y_axis_coord = [(0, 0), (3, 2), (5, 5), (1, 6)]
    __all_invalid_coords = [(-1, 0), (7, 2), (5, -2), (1, 6)]

    def setUp(self) -> None:
        self.validator = Validator()
        self.logger = self.validator.logger
        self.validator.logger = Mock()

    def tearDown(self) -> None:
        self.validator.logger = self.logger

    def test_all_valid_returns_whole_list(self):
        expected = [(0, 0), (3, 2), (5, 5)]
        result = self.validator.validate_coords(self.__grid, self.__valid_coords)
        self.assertEqual(result, expected)

    def test_one_invalid_x_coord_returns_list_without_it(self):
        expected = [(0, 0), (3, 2), (5, 5)]
        result = self.validator.validate_coords(self.__grid, self.__one_invalid_x_axis_coord)
        self.assertEqual(result, expected)

    def test_one_invalid_y_coord_returns_list_without_it(self):
        expected = [(0, 0), (3, 2), (5, 5)]
        result = self.validator.validate_coords(self.__grid, self.__one_invalid_y_axis_coord)
        self.assertEqual(result, expected)

    def test_all_invalid_returns_empty_list(self):
        expected = []
        result = self.validator.validate_coords(self.__grid, self.__all_invalid_coords)
        self.assertEqual(result, expected)
