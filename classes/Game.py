from classes.Board import Board
from classes.Player import Player
from classes.ShipType import ShipType
from classes.Ship import Ship
from colorama import Fore, Style
import random

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
                     # if start game then place ships and display boards
                    self.place_ships_for_player(self.players[0])
                    self.place_ships_for_player(self.players[1])
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
        """
        Place ships on the board for the specified player.

        Parameters:
        - player (Player): The player for whom ships are to be placed.
        """
        
        # List of ship types to be placed for the player
        ship_types = [
            ShipType.PATROL_BOAT,
            ShipType.SUBMARINE,
            ShipType.BATTLESHIP,
            ShipType.CARRIER
            ]

        # Iterate through each ship type and place a ship on the player's board
        for ship_type in ship_types:
            ship = Ship(ship_type)
            player.board.place_ship(ship)

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
        """
        Play a turn in the game, allowing players to make moves.
        """

        # Increment the turn counter
        self.turn += 1

        # Display turn information
        print("\n" + "%" * 40)
        if self.turn < 10:
            print("%" * 15 + f" Turn Nr {self.turn} " + "%" * 14)
        else:
            print("%" * 14 + f" Turn Nr {self.turn} " + "%" * 14)
        print("%" * 40 + "\n")

        # Determine current and other player based on the turn number
        if not self.turn % 2 == 0: 
            # Player turn
            current_player = self.players[0]
            other_player = self.players[1]
        else:
            # Computer turn
            current_player = self.players[1]
            other_player = self.players[0]

        # Display the name of the player whose turn it is
        print(f"{current_player.name}'s Turn")
        
        # Get attack coordinates
        x, y = self.determine_coordinates(current_player)
        
        print("Determined coordinates: " + x, y)

    def determine_coordinates(self, current_player):
        print("determine_coordinates")
        """
        Determine the coordinates for an attack based on the player.

        Parameters:
        - current_player (Player): The player making the attack.

        Returns:
        - tuple: The x, y coordinates for the attack.
        """

        # Continue prompting for coordinates until valid input is provided
        while True:
            try:
                if current_player.name == "Computer":
                    # Generate random coordinates for the computer
                    other_player = self.players[0]
                    x, y = self.generate_random_attack_coordinates()
                    print(f"Computer chose coordinates: ({x}, {y})")
                else:
                    # Promt player input for x and y coordinates
                    other_player = self.players[1]
                    x = int(input("Enter the x-coordinate for your attack:\n"))
                    y = int(input("Enter the y-coordinate for your attack:\n"))

                # Check if the chosen coordinates are within the board boundaries
                if (0 <= x < other_player.board.width and
                        0 <= y < other_player.board.height):
                    # Break the loop if coordinates haven't been attacked before, then return them
                    if (x, y) not in other_player.board.attacks:
                        break
                    else:
                        print(Fore.YELLOW + "You've already attacked these coordinates.")
                        print(Style.RESET_ALL)
                else:
                    print(Fore.RED + "Please choose coordinates within the board (0 - 8).")
                    print(Style.RESET_ALL)

            except ValueError:
                print(Fore.RED + "Please enter valid integers for x and y coordinates.")
                print(Style.RESET_ALL)
                continue
            except Exception:
                print(Fore.GREEN + "Your random values can not crash this battleship.")
                print("Try again and make your move ;) \n")
                print(Style.RESET_ALL)
                continue
        return x, y

    def generate_random_attack_coordinates(self):
        """
        Generate random attack coordinates.

        Returns:
        - tuple: The randomly generated x, y coordinates for an attack.
        """

        # Generate random x and y coordinates within the board boundaries
        x = random.randint(0, self.players[0].board.width - 1)
        y = random.randint(0, self.players[0].board.height - 1)

        # Ensure the generated coordinates have not been attacked before
        while (x, y) in self.players[0].board.attacks:
            # Regenerate coordinates if they have been attacked before
            x = random.randint(0, self.players[0].board.width - 1)
            y = random.randint(0, self.players[0].board.height - 1)
        return x, y

    def check_sunk_ships_for_player(self, player):
        print("check_sunk_ships_for_player")

    def show_continue_message(self):
        print("show_continue_message")