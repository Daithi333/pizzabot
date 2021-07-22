import sys

from pizzabot.arg_parser.single_arg_parser import SingleArgParser
from pizzabot.controller import Controller
from pizzabot.logger import Logger


def main():
    logger = Logger.get_logger(sys.argv[0])
    try:
        if len(sys.argv) > 1:
            raw_args = sys.argv[1]
            grid_dims, coordinates = SingleArgParser().extract_grid_and_coords(raw_args)
            delivery_route = Controller().process_deliveries(grid_dims, coordinates)
            logger.info(f'Delivery route: {delivery_route}')
            sys.exit(0)
        else:
            logger.error('No args detected and one is required, for example: "5x5 (1,1) (2,1)"')
            sys.exit(1)

    except Exception as e:
        logger.error(f'Encountered error in processing: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
