from Players.MinimaxPlayer import MinimaxPlayer
from Players.NegmaxPlayer import NegmaxPlayer
from Players.NegmaxABPlayer import NegmaxABPlayer

from Players.RandomPlayer import RandomPlayer
from controller import Controller
from gui import GUI

#player1 = MinimaxPlayer(9, 1, 2)
#player2 = MinimaxPlayer(9, 2, 1)

player1 = NegmaxABPlayer(5, 1, 2)
player2 = MinimaxPlayer(5, 2, 1)


#player1 = MinimaxPlayer(5, 1, 2)
#player2 = NegmaxABPlayer(5, 2, 1)

controller = Controller(5, player1, player2)
gui = GUI(controller)