class Ship:
    """
    Represents a ship in the Battleship game.

    Attributes:
    - ship_type (ShipType): The type of the ship.
    - positions (list): List of positions occupied by the ship.
    - hits (list): List of positions where the ship has been hit.
    """

    def __init__(self, ship_type):
        """
        Initialize a ship with the given type.

        Parameters:
        - ship_type (ShipType): The type of the ship.
        """
        self.ship_type = ship_type
        self.positions = []
        self.hits = []

    def is_sunk(self):
        print("is_sunk")