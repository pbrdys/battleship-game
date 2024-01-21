from colorama import Fore, Style
from classes.Game import Game

def main():
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
                next_turn = str(input("Next turn? (y/n) \n")).lower()
                if next_turn == "y":
                    continue
                elif next_turn == "n":
                    player1_defeated, computer_defeated = True, True
                    break
                else:
                    print("Type in correct value (y/n)")
                    continue

            break
        except Exception:
            print(Fore.GREEN + "Your random values can not crash this battleship.")
            print("Try again and make your move ;) \n")
            print(Style.RESET_ALL)
            continue