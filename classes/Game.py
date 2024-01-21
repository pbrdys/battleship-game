from classes.Board import Board
from classes.Player import Player
from colorama import Fore, Style

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
        """
        Start the Battleship game, allowing players to place their ships and initiating turns.
        """

        # Display a welcome message and game instructions
        print("*" * 67)
        print("**                 Welcome to Battleship Game!             **")
        print("**                                                         **")
        print("**  Prepare for an exciting naval battle against the       **")
        print("**  computer opponent. Strategically place your fleet,     **")
        print("**  unleash powerful attacks, and sink your opponent's     **")
        print("**  ships to claim victory. Enjoy the thrill of the high   **")
        print("**  seas right from your console!                          **")
        print("*" * 67)
        print("\n")
        print("*" * 67)
        print("**                 Are you ready to fight pirate?          **")
        print("-" * 67)
        print("**  1 Ready the cannons (start game)                       **")
        print("**  2 Every man for himself! Swim for yer lives (end game) **")
        print("*" * 67)

        # Allow players to choose between starting the game or ending it
        while True:
            try:
                # Get the player's choice
                start_action = int(input("Enter your choice: \n"))

                if start_action == 1:
                    self.display_player_boards()
                    break
                elif start_action == 2:
                    # end the game
                    self.end_game()
                    break
                else:
                    raise ValueError
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid integer (1, 2).")
                print(Style.RESET_ALL)
                continue
            except Exception:
                print(Fore.GREEN + "Your random values can not crash this battleship.")
                print("Try again and make your move ;) \n")
                print(Style.RESET_ALL)
                continue

    def end_game(self):
        """
        Quit the console
        """
        print(Fore.YELLOW + "You quit the game! Enjoy your day outside!")
        print(Style.RESET_ALL)
        quit()

    def place_ships_for_player(self, player):
        print("place_ships_for_player")

    def display_player_boards(self):
        """
        Display the game boards of all players.
        """
        
        # Iterate through each player in the game
        for player in self.players:
            # Determine whether to show ships on the board or not
            show_ships = False if player.name == "Computer" else True

            # Display the name of the player's board and the board itself
            print(f"\n {player.name}'s Board:")
            player.board.display_board(show_ships)

            # Print a separator line between player boards
            print("\n" + "=" * 40 + "\n")

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