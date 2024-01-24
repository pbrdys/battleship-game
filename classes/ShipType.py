from enum import Enum


class ShipType(Enum):
    """
    Enumeration defining types of ships with corresponding lengths.
    """
    PATROL_BOAT = 2
    SUBMARINE = 3
    BATTLESHIP = 4
    CARRIER = 5
