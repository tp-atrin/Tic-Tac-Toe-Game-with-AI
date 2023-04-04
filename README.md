# Tic-Tac-Toe-Game-with-AI
This is a Python implementation of the classic game of Tic-Tac-Toe, where you can play against an AI that uses the minimax algorithm to make its moves.

## Requirement

* Python 3.x

* Random

## Installation

1. Install Python 3.x on your computer if it's not already installed.

2. Install the **random** library if it's not already installed by using following command:
```
pip install random
```
3. Download the `tic_tac_toe_ai.py` file and save it to a directory of your choice.

4. Open a terminal or command prompt and navigate to the directory where you saved the `tic_tac_toe_ai.py` file.

5. Run the following command to start the game:
```
python tic_tac_toe_ai.py
```

## Game Rules
The game is played on a 3x3 board. You are X, and the computer is O. To make a move, enter the number of the square you want to place your X in (1-9), as shown below:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

The game ends when either you or the computer get three X's or O's in a row (horizontally, vertically, or diagonally), or if the board is full and no one has won. If you win, the program will print "Congratulations! You won!" and if the computer wins, it will print "Sorry, you lost." If the game ends in a tie, the program will print "Tie game!"

## Implementation Details

The AI uses the minimax algorithm to determine its moves. The minimax function is a recursive function that evaluates all possible moves on the current board and chooses the best move based on the current player's turn. The algorithm assumes that the computer is the "maximizing" player (trying to maximize its score), while the player is the "minimizing" player (trying to minimize the computer's score).
