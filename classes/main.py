from colorama import Fore, Style
from classes.Game import Game

def main():
    """
    The main function responsible for running the Battleship game.

    This function creates a new instance of the Game class, starts the game, and
    iteratively plays turns until one player's ships are all sunk. The winning
    player is then determined, and the game is over.

    Raises:
    - Exception: Any unexpected error during the execution of the game.

    Note:
    The main function handles exceptions and provides guidance in case of errors.
    """
    while True:
        try:
            # new Game instance
            game = Game()
            # Start the game by placing ships for both players and displaying the initial boards
            game.start_game()

            # Initialize defeat flags for both players
            player1_defeated, computer_defeated = False, False

            # Continue playing turns until one player is defeated
            while not player1_defeated and not computer_defeated:
                game.play_turn()
                # Check if a one player was defeated
                player1_defeated = game.players[0].board.all_ships_sunken()
                computer_defeated = game.players[1].board.all_ships_sunken()

            # Determine the winning player
            if game.players[0].board.all_ships_sunken():
                winning_player = game.players[1]
            else:
                winning_player = game.players[0]

            # Display the winning player
            print(Fore.GREEN + f"Congratulations {winning_player.name}, you have won the game!")
            print(Style.RESET_ALL)
            break
        except Exception:
            print(Fore.GREEN + "Your random values can not crash this battleship.")
            print("Try again and make your move ;) \n")
            print(Style.RESET_ALL)
            continue