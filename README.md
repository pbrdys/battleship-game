# Console Battleship Game

## Introduction
Welcome to the Console Battleship Game, an exciting battle brought to life in your console! This Python-based game pits you against a computer opponent in a strategic showdown on the high seas.

![Gameplay gif](./doc/gameplay.gif)

You can play this game at [https://pbrdys-battleship-game-e5bf19d085e1.herokuapp.com/](https://pbrdys-battleship-game-e5bf19d085e1.herokuapp.com/)

## How to play
You open the link above to open the console web application. 
The first thing you will see is a welcoming screen wether you can choose to start the game or end it 
imediately. 

* Choose "1" to start the game or "2" to end the game.
* After you decide to play the game: your board (player's board) and the computer's board are being displayed.
* Ships are being displayed on the player's board. On the computer'S board are no ships visible.
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
The user can see a menu where he can chose if he wants to start or end the game.

### Display initial boards for both players

![Initial-Player1-Board](./doc/initial-player-board.jpg)


![Initial-Computer-Board](./doc/initial-computer-board.jpg)


### Play turn
Player 1 starts the game. Player 1 is chosing his coordinates to attack the computers board. 
![Player1-Turn](./doc/play-turn-player1.jpg)

Computer is chosing the coordinates to attack the players board. 
![Computer-Turn](./doc/play-turn-computer.jpg)

Like this both players play their turns back and forth until the game is over. 

### End the game 
There are two ways to end the game before a winner was determined.
Either in the beginning when the [Welcome Screen](#Welcome-Screen) is being displayed, 
or after every second turn. Basically always after the computer made his attack, the player can chose wether he wants to continue the game or end the game. 

Welcome Screen - End Game: 
![Welcome-Screen-End-Game](./doc/end-game-message.jpg)
To end the game at the welcome screen the player has to chose "2". 

During the game - End Game: 
![During-the-game-End-Game](./doc/quit-game-message.jpg)
To end the game during the game, after the computers turn, the player has to chose "q" for quit. 

### Determine the winner
This is the third way to end the game. After both players have played turn by turn against each other, the player who first has destroyed all ships of his opponend wins the game. 

![Display-Winner](./doc/display-winner.jpg)
In the moment the last ship was destroyed, the winner is being displayed and the game is over. 

### Future Features

## Data Model
classes etc.

### ShipType
Enumeration 

## Flow Diagram

# Testing

## Validator Testing
PEP8 ... 

# Deployment


# Credits
Thank you Daisy McGirr