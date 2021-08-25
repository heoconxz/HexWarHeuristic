class Player:
    """
    Class representing a player.
    You need to inherit from this class.
    """
    def __init__(self, size):
        self.name = "Player"
        self._size = size

    def step(self):
        """
        The function needs to return the coordinates of the next move of the player.
        It should call your algorithm. Don't forget to memorize your move.
        :return: Coordinates following the data structure: [x,y]
        """
        pass

    def update(self, move_other_player):
        """
        The game will call this function with the move of the other player.
        :param move_player: Move of the other player in this format: [x, y]
        :return: Nothing
        """
        pass