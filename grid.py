import numpy as np


class Grid:
    """
    Class representing the grid of the HexWar.
    """
    def __init__(self, size):
        self._size = size
        self._grid = np.zeros(shape=(self._size, self._size))

    def get_size(self):
        return self._size

    def set_hex(self, player, coordinate):
        self._grid[coordinate[1], coordinate[0]] = player

    def get_hex(self, coordinate):
        return self._grid[coordinate[1], coordinate[0]]

    def get_grid(self):
        return self._grid

    def neighbors(self, coordinates):
        neighbors = []
        directions = [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0]]

        for dir in directions:
            new_coordinates = [coordinates[0]+dir[0], coordinates[1]+dir[1]]
            if 0 <= new_coordinates[0] < self._size and 0 <= new_coordinates[1] < self._size:
                neighbors.append(new_coordinates)

        return neighbors

