from Players.RandomPlayer import RandomPlayer
from controller import Controller
from gui import GUI

player1 = RandomPlayer(11)
player2 = RandomPlayer(11)
controller = Controller(11, player1, player2)
gui = GUI(controller)