from Players.MinimaxPlayer import MinimaxPlayer
from Players.RandomPlayer import RandomPlayer
from controller import Controller
from gui import GUI

player1 = MinimaxPlayer(9, 1, 2)
player2 = MinimaxPlayer(9, 2, 1)
controller = Controller(9, player1, player2)
gui = GUI(controller)