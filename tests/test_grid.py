import unittest

from pizzabot.grid import Grid


class TestGrid(unittest.TestCase):
    simple_coords = [(1, 1), (2, 2)]
    all_hq_coords = [(0, 0), (0, 0), (0, 0)]
    same_coords_deliveries = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 1), (1, 1)]
    all_zero_x_coords = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 1), (0, 0)]
    all_zero_y_coords = [(1, 0), (2, 0), (3, 0), (4, 0), (1, 0), (0, 0)]

    def setUp(self) -> None:
        self.grid = Grid(5, 5, 0, 0)

    def test_determine_route_with_simple_coords(self):
        expected = 'ENDEND'
        result = self.grid.determine_route(self.simple_coords)
        self.assertEqual(result, expected)

    def test_determine_route_with_all_hq_coords(self):
        expected = 'DDD'
        result = self.grid.determine_route(self.all_hq_coords)
        self.assertEqual(result, expected)

    def test_determine_route_with_multiple_deliveries_at_same_location(self):
        expected = 'ENDDDENDENDEND'
        result = self.grid.determine_route(self.same_coords_deliveries)
        self.assertEqual(result, expected)

    def test_determine_route_with_coords_all_have_zero_x_axis(self):
        expected = 'DNDDNDNDND'
        result = self.grid.determine_route(self.all_zero_x_coords)
        self.assertEqual(result, expected)

    def test_determine_route_with_coords_all_have_zero_y_axis(self):
        expected = 'DEDDEDEDED'
        result = self.grid.determine_route(self.all_zero_y_coords)
        self.assertEqual(result, expected)
