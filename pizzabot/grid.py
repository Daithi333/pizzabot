from pizzabot.constants import BOT_START_COORD, EAST, WEST, NORTH, SOUTH, DELIVER


class Grid:

    def __init__(self, width: int, height: int, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_start + width
        self.y_end = x_start + height
        self.start_coord = BOT_START_COORD

    def determine_route(self, coords: (int, int)) -> str:
        """
        Generate string representation of route for bot to make deliveries for passed in coordinates.
        Coordinates are sorted which will prioritise the x coordinate.
        Directional priority given to x axis based on order the directions are appended to the results list
        """
        route = []
        coords.sort()
        coords.insert(0, self.start_coord)

        for i in range(len(coords) - 1):
            x_directions, y_directions = '', ''
            x_movement = coords[i+1][0] - coords[i][0]
            y_movement = coords[i+1][1] - coords[i][1]

            if x_movement != 0:
                x_directions = (EAST * x_movement) if x_movement > 0 else (WEST * abs(x_movement))

            if y_movement != 0:
                y_directions = (NORTH * y_movement) if y_movement > 0 else (SOUTH * abs(y_movement))

            route.append(x_directions + y_directions + DELIVER)

        return ''.join(route)
