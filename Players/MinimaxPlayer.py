import numpy as np

from Players.Player import Player
from grid import Grid
import copy

class MinimaxPlayer(Player):
    def __init__(self, size, player_number, adv_number):
        super().__init__(size,  player_number, adv_number)
        self.name = "Minimax"
        self._possible_moves = []
        self.node = Grid()

    def step(self):
        best_move = []
        best = -np.inf
        for move in self.node.free_moves():
            new_node = copy.deepcopy(self.node)
            new_node.set_hex(move, self.player_number)
            value = self.alphaBeta(new_node, 5, -np.inf, np.inf, 2)
            if value > best:
                best_move = move
        return best_move

    def update(self, move_other_player):
        self.node.set_hex(move_other_player)

    def alphaBeta(self, node, depth, alpha, beta, player):
        if depth == 0 or node.check_win(1) or node.check_win(2):
            return self.heuristic(node)
        if player == self.player_number:
            value = -np.inf
            for move in node.free_moves():
                new_node = copy.deepcopy(node)
                new_node.set_hex(move, self.player_number)
                value = max(value, self.alphaBeta(new_node, depth-1, alpha, beta, self.adv_number))
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            value = np.inf
            for move in node.free_moves():
                new_node = copy.deepcopy(node)
                new_node.set_hex(move, self.player_number)
                value = min(value, self.alphaBeta(new_node, depth - 1, alpha, beta, self.player_number))
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value


    def heuristic(self, node):
