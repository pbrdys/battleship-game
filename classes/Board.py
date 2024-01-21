class Board:
    """
    Represents a game board in the Battleship game.

    Attributes:
    - width (int): The width of the board.
    - height (int): The height of the board.
    - ships (list): List of ships on the board.
    - attacks (set): Set of coordinates that have been attacked.
    - already_sunk_ships: List of ships already destroyed.
    """

    def __init__(self, width, height):
        """
        Initialize a game board with the given width and height.

        Parameters:
        - width (int): The width of the board.
        - height (int): The height of the board.
        """
        self.width = width
        self.height = height
        self.ships = []
        self.attacks = set()
        self.already_sunk_ships = []

    def place_ship(self, ship):
        print("place_ship")

    def receive_attack(self, x, y):
        print("receive_attack")

    def display_board(self, show_ships):
        print("display_board")

    def get_cell_content(self, x, y, show_ships):
        print("get_cell_content")
        
    def all_ships_sunken(self):
        print("all_ships_sunken")