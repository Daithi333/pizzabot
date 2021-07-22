import unittest
from unittest.mock import patch

from pizzabot.arg_parser.single_arg_parser import SingleArgParser
from pizzabot.error import ValidationError
from pizzabot.logger import Logger


class TestSingleArgParser(unittest.TestCase):
    valid_arg_basic = '5x5 (1,2) (2,3)'
    valid_arg_with_spaces = '5 x 5 ( 1, 2 ) ( 2 , 3 )'
    invalid_arg_missing_grid = '(1,2) (2,3)'
    invalid_arg_invalid_grid = ' 5y5 (1,2) (2,3)'
    invalid_arg_missing_coords = '5x5'
    valid_arg_some_invalid_coords = '5x5 (1,2) (2,3), (x,y) (4 4) (5.5)'
    negative_coords = '5x5 (-1,-2) (-2,-3)'
    negative_coords_with_spaces = '5 x 5 (- 1, - 2) (- 2 ,- 3 )'

    @classmethod
    def setUpClass(cls) -> None:
        with patch.object(Logger, 'get_logger') as mock_logger:
            cls.parser = SingleArgParser()

    def test_valid_arg_basic_returns_grid_and_coords(self):
        expected = ((5, 5), [(1, 2), (2, 3)])
        result = self.parser.extract_grid_and_coords(self.valid_arg_basic)
        self.assertEqual(result, expected)

    def test_valid_arg_with_spaces_returns_grid_and_coords(self):
        expected = ((5, 5), [(1, 2), (2, 3)])
        result = self.parser.extract_grid_and_coords(self.valid_arg_with_spaces)
        self.assertEqual(result, expected)

    def test_invalid_arg_with_no_grid_raises_exception(self):
        with self.assertRaises(ValidationError):
            self.parser.extract_grid_and_coords(self.invalid_arg_missing_grid)

    def test_invalid_arg_invalid_grid_raises_exception(self):
        with self.assertRaises(ValidationError):
            self.parser.extract_grid_and_coords(self.invalid_arg_invalid_grid)

    def test_invalid_arg_with_no_coords_raises_exception(self):
        with self.assertRaises(ValidationError):
            self.parser.extract_grid_and_coords(self.invalid_arg_missing_coords)

    def test_valid_arg_with_some_invalid_coords_returns_grid_and_valid_coords(self):
        expected = ((5, 5), [(1, 2), (2, 3)])
        result = self.parser.extract_grid_and_coords(self.valid_arg_some_invalid_coords)
        self.assertEqual(result, expected)

    def test_invalid_arg_with_no_coords_raises_exception(self):
        with self.assertRaises(ValidationError):
            self.parser.extract_grid_and_coords(self.invalid_arg_missing_coords)

    def test_negative_coords_with_spaces_will_not_be_parsed_from_input_string(self):
        with self.assertRaises(ValidationError):
            self.parser.extract_grid_and_coords(self.negative_coords_with_spaces)
