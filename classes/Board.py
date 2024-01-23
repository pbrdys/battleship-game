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
        """
        Receive an attack at the specified coordinates.

        Parameters:
        - x (int): The x-coordinate of the attack.
        - y (int): The y-coordinate of the attack.

        Returns:
        - bool: True if the attack hits a ship, False otherwise.
        """

        # Check if the attack coordinates are within the valid board range
        if 0 <= x < self.width and 0 <= y < self.height:
            # Check if the coordinates have not been attacked before
            if (x, y) not in self.attacks:
                # Mark the coordinates as attacked
                self.attacks.add((x, y))

                # Check if the attack hits any ship on the board
                for ship in self.ships:
                    if (x, y) in ship.positions:
                        # record the Hit and return True
                        ship.hits.append((x, y))
                        return True

                # Miss
                return False
            else:
                print("You've already attacked these coordinates.")
        else:
            raise ValueError("Invalid attack coordinates.")

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

            # Iterate through each column in the row
            for x in range(self.width):
                # Get the content of the current cell based
                cell_content = self.get_cell_content(x, y, show_ships)
                # Customize cell content display based on the type of content
                if cell_content == "X":
                    # Display hit in green
                    row_str += f" {Fore.GREEN + cell_content + Style.RESET_ALL} |"
                elif cell_content == "/":
                    # Display miss in red
                    row_str += f" {Fore.RED + cell_content + Style.RESET_ALL} |"
                else:
                    # Display ship in yellow
                    row_str += f" {Fore.YELLOW + cell_content + Style.RESET_ALL} |"
            
            # Print the current row and separator line
            print(row_str)
            print("   +" + "+".join(["---" for _ in range(self.width)]) + "+")

    def get_cell_content(self, x, y, show_ships):
        """
        Get the content of a cell on the board for display purposes.

        Parameters:
        - x (int): The x-coordinate of the cell.
        - y (int): The y-coordinate of the cell.
        - show_ships (bool): True to display ships, False to hide them.

        Returns:
        - str: The content of the cell.
        """

        # Iterate through each ship on the board
        for ship in self.ships:
            # Check if the current cell is part of the ship's positions
            if (x, y) in ship.positions:
                # Display 'X' for hit ship, otherwise display the ship's length
                if (x, y) in ship.hits:
                    return "X"
                return str(ship.ship_type.value) if show_ships else " "

        # Check if the cell has been attacked
        if (x, y) in self.attacks:
            # Display "/" if the attack missed all ships
            if not any((x, y) in ship.hits for ship in self.ships):
                return "/"
            
        # If the cell has no ship and has not been attacked
        return " "
        
    def all_ships_sunken(self):
        """
        Check if all ships on the board are sunk.

        Returns:
        - bool: True if all ships are sunk, False otherwise.
        """
        return all(ship.is_sunk() for ship in self.ships)