from classes.Board import Board
from classes.Player import Player

class Game:
    """
    Represents a Battleship game.

    Attributes:
    - players (list): List of players participating in the game.
    - turn (int): Current turn number.
    """

    def __init__(self):
        """
        Initialize a Battleship game with two players and initial turn settings.
        """
        self.players = [Player("Player 1", Board(9, 9)),
                        Player("Computer", Board(9, 9))]
        self.turn = 0

    def start_game(self):
        print("start_game")

    def end_game(self):
        print("end_game")

    def place_ships_for_player(self, player):
        print("place_ships_for_player")

    def display_player_boards(self):
        print("display_player_boards")

    def play_turn(self):
        print("play_turn")

    def determine_coordinates(self, current_player):
        print("determine_coordinates")

    def generate_random_attack_coordinates(self):
        print("generate_random_attack_coordinates")

    def check_sunk_ships_for_player(self, player):
        print("check_sunk_ships_for_player")

    def show_continue_message(self):
        print("show_continue_message")