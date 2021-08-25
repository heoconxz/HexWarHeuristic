from grid import Grid
from gui import GUI


class Controller:
    def __init__(self, size, player1, player2):
        self._grid = Grid(size)
        self._player1 = player1
        self._player2 = player2
        self._current_player = 1
        self._winner = 0

    def update(self):
        if self._current_player == 1:
            coordinates = self._player1.step()
            self._grid.set_hex(self._current_player, coordinates)
            self._current_player = 2
            self._player2.update(coordinates)
        else:
            coordinates = self._player2.step()
            self._grid.set_hex(self._current_player, coordinates)
            self._current_player = 1
            self._player1.update(coordinates)

        if self._check_win()[0]:
            self._winner = 1
        elif self._check_win()[1]:
            self._winner = 2
        else:
            self._winner = 0

    def _check_win(self):
        """
        Check the winning condition for both player.
        :return: Tuple (player1, player)
        """
        player1 = False
        player2 = False

        neighbors1 = []
        neighbors2 = []
        for y in range(self._grid.get_size()):
            if self._grid.get_hex([0, y]) == 1:
                neighbors1.append([0, y])

        for x in range(self._grid.get_size()):
            if self._grid.get_hex([x, 0]) == 2:
                neighbors2.append([x, 0])

        if len(neighbors1) == 0 and len(neighbors2) == 0:
            return (player1, player2)

        # Checking if Player 1 won
        for neighbor in neighbors1:
            neighbors = self._grid.neighbors(neighbor)
            for next_neighbor in neighbors:
                if self._grid.get_hex(next_neighbor) == 1 and (next_neighbor not in neighbors1):
                    if next_neighbor[0] == self._grid.get_size()-1:
                        player1 = True
                        return (player1, player2)
                    else:
                        neighbors1.append(next_neighbor)

        # Check if Player 2 won.
        for neighbor in neighbors2:
            neighbors = self._grid.neighbors(neighbor)
            for next_neighbor in neighbors:
                if self._grid.get_hex(next_neighbor) == 2 and (next_neighbor not in neighbors2):
                    if next_neighbor[1] == self._grid.get_size()-1:
                        player2 = True
                        return (player1, player2)
                    else:
                        neighbors2.append(next_neighbor)

        return (player1, player2)
