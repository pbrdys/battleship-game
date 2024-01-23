# Console Battleship Game

## Introduction
Welcome to the Console Battleship Game, an exciting battle brought to life in your console! This Python-based game pits you against a computer opponent in a strategic showdown on the high seas.

![Gameplay gif](./doc/gameplay.gif)

You can play this game at [https://pbrdys-battleship-game-e5bf19d085e1.herokuapp.com/](https://pbrdys-battleship-game-e5bf19d085e1.herokuapp.com/)

## How to play
You open the link above to open the console web application. 
The first thing you will see is a welcoming screen wether you can choose to start the game or end it 
imediately. 

* Choose '1' to start or '2' to end the game.
* After you decide to play the game: your board (player's board) and the computer's board are being displayed.
* Ships are being displayed on the player's board. On the computer's board are no ships visible.
    * There are different ships available in this game with different lengths. (More information in the [ShipType Section](#ShipType)). Every ship is being displayed as its length number.
* First turn is the players turn. 
* Attack by choosing an x-coordinate and an y-coordinate.
    * Coordinates can only be numbers within the board range.
* Turn change: computers turn, computer attacks.
* After 2 turns, both boards are being displayed.
    * Hits are displayed as an green "X"
    * Miss is being displayed as an red "/"
    * Ships are being displayed as an yellow number (2 - 5)
* Both players go like that back and forth until one player has destroyed all ships of his opponend. 
* Once a player won the game is over and you have tu run the application again.

## Features
### Existing Features

#### Welcome Screen

![Welcome Screen](./doc/welcome-screen.jpg)

At the start of the game users are welcomed and introduced to the game they are about to play.
The user can see a menu where he can chose if he wants to start or end the game. In order to start the game the user has to enter "1". He can also enter "2" to end the game. Any other values will resolve in an error message.

### Display Player Boards
After the game was started the first thing the user will see are the boards of both players (player 1 and computer). 

![Initial-Player1-Board](./doc/initial-player-board.jpg)

On the players board the ships are being displayed with yellow numbers. 
The number is refering to the length of the ship.

![Initial-Computer-Board](./doc/initial-computer-board.jpg)

The initial computer board is displayed with empty cells. The ships must be hidden for the player. 

Both boards are being [updated](#Update-Player-Boards) after they have been attacked.

### Place Ship
The ships are being placed randomly for both players.
The cirteria to place a ship are:
    * Ships are not allowed to share the same coordinate (they shouldn cross each other)
    * Ships must fit into the boards width and height. 

### Play turn
Player 1 starts the game. Player 1 is chosing his coordinates to attack the computers board. 
The criteria to match for the coordinates are:
    * must be a valid integer within the board size. Starting with the index of 0. 
    * no other values allowed like: strings, bool, etc. 

Choosing the wrong value will result in an [error message](#Display-Error-Messages).

![Player1-Turn](./doc/play-turn-player1.jpg)

In the next turn the computer is about to attack the players board.
The coordinates for the computer are being generated randomly. 
![Computer-Turn](./doc/play-turn-computer.jpg)

Like this both players play their turns back and forth until the game is over.

### Attack The Opponents Board
Each turn a player is about to attack the opponents board by choosing the coordinates for his attack as described in the section [Play turn](#Play-turn).

After a player attacked his opponents board he get's a info message wether he "hit" or "miss". 

#### Hit
![Hit](./doc/hit.jpg)

#### Miss
![Miss](./doc/miss.jpg)

### Continue or Quit the Game
After both players made their attack the user is being promted to choose wether to "continue" or "quit" the game.
![Continue-Quit](./doc/promt-continue-quit.jpg)

### Update Player Boards
The updated player boards contain:

![Updated-Player-Board](./doc/updated-player-board.jpg)
    * Player 1:
        * displaying ships as numbers (yellow)
        * displaying hits as X (green)
        * displaying miss as / (red)

![Updated-Computer-Board](./doc/updated-computer-board.jpg)
    * Computer:
        * displaying hits as X (green)
        * displaying miss as / (red)

### End the game 
There are three ways to end the game.
The first two are either in the beginning when the [Welcome Screen](#Welcome-Screen) is being displayed, 
or after every second turn. Basically always after the computer made his attack, the player can chose wether he wants to continue the game or end the game. 

#### End Game before you even start: 
![Welcome-Screen-End-Game](./doc/end-game-message.jpg)

To end the game at the welcome screen the player has to chose "2". 

#### End Game during the game: 
![During-the-game-End-Game](./doc/quit-game-message.jpg)

To end the game during the game, after the computers turn, the player has to chose "q" for quit. 

### Determine the winner
The third way to end the game is by winning or losing the game. After both players have played turn by turn against each other, the player who first has destroyed all ships of his opponend wins the game.

![Display-Winner](./doc/display-winner.jpg)

In the moment the last ship was destroyed, the winner is being displayed and the game is over. 

### Display Error Messages
Error messages play a crucial role in enhancing the gameplay experience as they provide users with feedback on their actions. This information helps users understand what is happening and guides them on the necessary steps. Additionally, effectively catching errors and delivering appropriate messages prevents the application from crashing.

#### Warning: Already attacked coordinates
When the user attempts to attack the same coordinate again, a relevant message is displayed, prompting the user to select different coordinates for their next attack.

![Already-Attacked-Message](./doc/already-attacked.jpg)

#### Error: Coordinates out of range
When the user attempts to attack coordinates that are not within the range (width, height) of the opponents board, a relevant message is being displayed, promting the user to select different coordinates.
* X-Coordinate: between 0 and max-board-width
* Y-Coordinate: between 0 and max-board-height

![Out-Of-Range-Message](./doc/coordinates-out-of-range.jpg)

#### Error: Invalid coordinates
When the entered coordinates don't match the criteria, a relevant message is displayed, prompting the user to select different coordinates for their next attack. 
* Coordinate criteria: 
    * Only numbers allowed, no strings or other values

![Invalid-Coordinates-Message](./doc/invalid-coordinates.jpg)

#### General Exception-Handling
In certain scenarios, the application may encounter unforeseeable input values. To safeguard against potential crashes, it is imperative to establish a comprehensive high-level exception handling mechanism at the application's core. This overarching exception handling will address any errors that may arise and are not specifically caught elsewhere within the application.

![Exception-Handling](./doc/exception-handling.jpg)



## Future Features
* Playing against another human
* Implement smarter strategies for attack coordinates of the computer. For instance, after a successful hit, the next set of coordinates could be chosen from the adjacent cells of the previous hit, optimizing the computer's targeting approach.
* Dynamic player name and board size.

## Data Model

### Game Class
+---------------------------------------------------+
* Game propertys:                                   |
    * players: list                                 |  
    * turn: int                                     |
+---------------------------------------------------+
* Game methods:                                     |
    * __init__()                                    |
    * start_game()                                  |
* end_game()                                        |
    * place_ships_for_player(player: Player)        |
    * display_player_boards()                       |
    * play_turn()                                   |
    * determine_coordinates(player: Player): tuple  |
    * generate_random_attack_coordinates(): tuple   |
    * check_sunk_ships_for_player(player: Player)   |
    * show_continue_message()                       |
+---------------------------------------------------+
### Player Class

### Board Class 

### Ship Class

### ShipType

### main()

### Orientation Class
Enumeration 

## Flow Diagram

# Testing

## Validator Testing
PEP8 ... 

# Deployment


# Credits
Thank you Daisy McGirr