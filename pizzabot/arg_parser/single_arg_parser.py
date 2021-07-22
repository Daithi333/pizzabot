import re

from pizzabot.arg_parser.abstract_arg_parser import AbstractArgParser
from pizzabot.constants import GRID_REGEX, COORDS_REGEX
from pizzabot.error import ValidationError
from pizzabot.logger import Logger


class SingleArgParser(AbstractArgParser):

    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__)

    def extract_grid_and_coords(self, raw_args: str) -> ((int, int), list[(int, int)]):
        grid_dims = self._extract_grid(raw_args)
        coordinates = self._extract_coords(raw_args)
        self.logger.info(f'Valid grid dimensions and delivery coordinates found in input string')
        return grid_dims, coordinates

    def _extract_grid(self, raw_args: str) -> (int, int):
        raw_grid = re.findall(GRID_REGEX, raw_args)
        if len(raw_grid) == 0:
            raise ValidationError(f'Grid dimensions not found in input string [{raw_args}]. Expected format: "5x5"')

        raw_grid = raw_grid[0]
        dimensions = [int(s.strip()) for s in raw_grid.split('x') if s.strip().isdigit()]
        return dimensions[0], dimensions[1]

    def _extract_coords(self, raw_args: str) -> list[(int, int)]:
        raw_coords = re.findall(COORDS_REGEX, raw_args)
        if len(raw_coords) == 0:
            raise ValidationError('No delivery coordinates were found in input string')

        coords = []
        for rc in raw_coords:
            # s.strip()[1:] allows negative numbers to pass validation
            coord = [int(s.strip()) for s in rc.split(',') if s.strip().isdigit() or s.strip()[1:].isdigit()]
            coords.append(tuple(coord))

        if len(coords) == 0:
            raise ValidationError('No valid coordinates found')

        return coords
