from pizzabot.grid import Grid
from pizzabot.logger import Logger


class Validator:
    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def validate_coords(self, grid: Grid, coords: list[(int, int)]):
        invalid = [c for c in coords
                   if (c[0] < grid.x_start or c[0] > grid.x_end)
                   or (c[1] < grid.y_start or c[1] > grid.y_end)]

        log_msg = f'All [{len(coords)}] coordinates valid within grid range' if len(invalid) == 0 \
            else f'[{len(invalid)}] coordinates were outside expected range and will be ignored: {invalid}'
        self.logger.info(log_msg)
        return [c for c in coords if c not in invalid]
