import unittest
from unittest.mock import patch, ANY

from pizzabot.controller import Controller
from pizzabot.grid import Grid
from pizzabot.logger import Logger
from pizzabot.validator import Validator


class TestController(unittest.TestCase):
    grid_dims = (5, 5)
    simple_coords = [(1, 1), (1, 2)]

    @classmethod
    def setUpClass(cls) -> None:
        with patch.object(Logger, 'get_logger') as mock_logger:
            cls.controller = Controller()

    def test_process_deliveries_returns_string_response(self):
        result = self.controller.process_deliveries(self.grid_dims, self.simple_coords)
        self.assertEqual(type(result), str)

    def test_process_deliveries_calls_validator_with_expected_coords(self):
        expected = [(1, 1), (1, 2)]
        with patch.object(Validator, 'validate_coords') as mock_validate_coords:
            self.controller.process_deliveries(self.grid_dims, self.simple_coords)
            mock_validate_coords.assert_called_with(ANY, expected)

    def test_process_deliveries_calls_determine_route_with_expected_coords(self):
        expected = [(1, 1), (1, 2)]
        with patch.object(Grid, 'determine_route') as mock_determine_route:
            self.controller.process_deliveries(self.grid_dims, self.simple_coords)
            mock_determine_route.assert_called_with(expected)

    def test_process_deliveries_returns_expected_route(self):
        expected = 'ENDND'
        with patch.object(Grid, 'determine_route') as mock_determine_route:
            mock_determine_route.return_value = 'ENDND'
            result = self.controller.process_deliveries(self.grid_dims, self.simple_coords)
            self.assertEqual(result, expected)

    def test_exception_during_process_deliveries_is_caught(self):
        with patch.object(Grid, 'determine_route') as mock_determine_route:
            mock_determine_route.side_effect = KeyError()
            with self.assertRaises(KeyError):
                self.controller.process_deliveries(self.grid_dims, self.simple_coords)
