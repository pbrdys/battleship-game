from colorama import Fore, Style 

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
        """
        Display the current state of the game board.

        Parameters:
        - show_ships (bool): True to display ships, False to hide them.
        """

        # Display column numbers at the top of the board
        print("     " + "   ".join(str(i) for i in range(self.width)))

        # Iterate through each row on the board
        for y in range(self.height):
            # Initialize the row string with the current row number
            row_str = f"{y:2d} |"

            # Print the current row and separator line
            print(row_str)
            print("   +" + "+".join(["---" for _ in range(self.width)]) + "+")

    def get_cell_content(self, x, y, show_ships):
        print("get_cell_content")
        
    def all_ships_sunken(self):
        """
        Check if all ships on the board are sunk.

        Returns:
        - bool: True if all ships are sunk, False otherwise.
        """
        return all(ship.is_sunk() for ship in self.ships)