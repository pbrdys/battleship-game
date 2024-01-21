from colorama import Fore, Style 
from classes.Orientation import Orientation
import random

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
        """
        Place a ship on the board randomly.

        Parameters:
        - ship (Ship): The ship to be placed on the board.
        """

        ship.positions = []  # Reset positions
        ship.hits = []       # Reset hits

        while True:
            # Choose a random orientation for the ship (horizontal or vertical)
            random_number = random.randint(0, 1)
            if random_number == 1:
                orientation = Orientation.VERTICAL
            else:
                orientation = Orientation.HORIZONTAL

            # Generate random coordinates x, y for the ship's starting position
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            # Check if the ship fits in the chosen orientation and starting position within the board boundaries
            is_horizontal = orientation == Orientation.HORIZONTAL
            fits_horizontally = x + ship.ship_type.value <= self.width
            is_vertical = orientation == Orientation.VERTICAL
            fits_vertically = y + ship.ship_type.value <= self.height

            if is_horizontal and fits_horizontally:
                # Generate positions for a horizontally placed ship
                positions = [(x + i, y) for i in range(ship.ship_type.value)]
            elif is_vertical and fits_vertically:
                # Generate positions for a vertically placed ship
                positions = [(x, y + i) for i in range(ship.ship_type.value)]
            else:
                # Try again if the ship doesn't fit in the chosen orientation
                continue

            overlap = any(
                pos in ship.positions
                for pos in positions
                for ship in self.ships
            )
            if not overlap:
                ship.positions = positions
                self.ships.append(ship)
                break

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