from pizzabot.constants import X_START, Y_START
from pizzabot.grid import Grid
from pizzabot.logger import Logger
from pizzabot.validator import Validator


class Controller:

    def __init__(self):
        self.logger = Logger.get_logger(__name__)
        self.validator = Validator()

    def process_deliveries(self, grid_dims: (int, int), coords: list[(int, int)]) -> str:
        self.logger.info(f'Processing deliveries for grid dimensions [{grid_dims}] and [{len(coords)}] co-ordinates')
        try:
            grid = Grid(grid_dims[0], grid_dims[1], X_START, Y_START)
            valid_coords = self.validator.validate_coords(grid, coords)
            delivery_route = grid.determine_route(valid_coords)
            return delivery_route

        except Exception as err:
            self.logger.error(f'Error while processing deliveries: {err}')
            raise
