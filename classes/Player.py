class Player:
    """
    Represents a player in the Battleship game.

    Attributes:
    - name (str): The name of the player.
    - board (Board): The game board associated with the player.
    """
    
    def __init__(self, name, board):
        """
        Initialize a player with the given name and game board.

        Parameters:
        - name (str): The name of the player.
        - board (Board): The game board associated with the player.
        """
        self.name = name
        self.board = board