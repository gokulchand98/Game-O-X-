import numpy as np

# Define the grid size.
grid_size = (6, 7)

# Create the grid.
grid = np.zeros(grid_size, dtype=str)

# Define the players' symbols.
players = ['O', 'X']

# Define the winning conditions.
winning_conditions = [
   # Horizontal wins.
   [(0, 0), (0, 1), (0, 2), (0, 3)],
   [(1, 0), (1, 1), (1, 2), (1, 3)],
   [(2, 0), (2, 1), (2, 2), (2, 3)],
   [(3, 0), (3, 1), (3, 2), (3, 3)],
   [(4, 0), (4, 1), (4, 2), (4, 3)],
   [(5, 0), (5, 1), (5, 2), (5, 3)],
   # Vertical wins.
   [(0, 0), (1, 0), (2, 0), (3, 0)],
   [(1, 0), (2, 0), (3, 0), (4, 0)],
   [(2, 0), (3, 0), (4, 0), (5, 0)],
   [(3, 0), (4, 0), (5, 0), (6, 0)],
   [(4, 0), (5, 0), (6, 0), (7, 0)],
   # Diagonal wins.
   [(0, 0), (1, 1), (2, 2), (3, 3)],
   [(1, 0), (2, 1), (3, 2), (4, 3)],
   [(2, 0), (3, 1), (4, 2), (5, 3)],
   [(3, 0), (4, 1), (5, 2), (6, 3)],
   [(0, 3), (1, 2), (2, 1), (3, 0)],
   [(1, 3), (2, 2), (3, 1), (4, 0)],
   [(2, 3), (3, 2), (4, 1), (5, 0)],
   [(3, 3), (4, 2), (5, 1), (6, 0)],
]


# Function to check if a player has won.
def check_win(grid, player):
   """
   Checks if a player has won the game.

   Args:
       grid (np.ndarray): The game grid.
       player (str): The player to check for a win.

   Returns:
       bool: True if the player has won, False otherwise.
   """
   # Iterate over the winning conditions.
   for condition in winning_conditions:
       # Check if all the squares in the condition are marked by the player.
       if all(grid[r, c] == player for r, c in condition):
           return True

   # If no winning condition is met, return False.
   return False


# Function to get the available moves for a player.
def get_available_moves(grid):
   """
   Gets the available moves for a player.

   Args:
       grid (np.ndarray): The game grid.

   Returns:
       list: A list of tuples representing the available moves.
   """
   # Initialize the list of available moves.
   available_moves = []

   # Iterate over the columns.
   for c in range(grid_size[1]):
       # Check if the lowest space in the column is empty.
       if grid[grid_size[0] - 1, c] == ' ':
           # If it is, add the move to the list of available moves.
           available_moves.append((grid_size[0] - 1, c))

   # Return the list of available moves.
   return available_moves


# Function to make a move.
def make_move(grid, player, move):
   """
   Makes a move on the game grid.

   Args:
       grid (np.ndarray): The game grid.
       player (str): The player making the move.
       move (tuple): The move

**Ratings:**
- Rate the overall response quality (keeping in mind your answers to the questions above)::
    OK
     **
- To what extent does the response follow the role and guidelines set in the System (🌐) instructions?:
    Moderately
     **

#### Chatbot Response 2:
```python
import numpy as np

# Define the game board dimensions
ROWS = 6
COLS = 7

# Create a function to initialize the game board
def create_board():
   # Create an empty NumPy array (6 rows, 7 columns)
   return np.zeros((ROWS, COLS), dtype=int)

# Create a function to display the game board
def display_board(board):
   # Print the column numbers
   print(" ".join(map(str, range(1, COLS + 1))))
   # Print the game board
   for row in board:
       print("|".join(["O" if cell == 1 else "X" if cell == 2 else " " for cell in row]))

# Create a function to check if a player has won
def check_win(board, player):
   # Check for horizontal wins
   for row in range(ROWS):
       for col in range(COLS - 3):
           if board[row][col:col + 4].sum() == player * 4:
               return True

   # Check for vertical wins
   for col in range(COLS):
       for row in range(ROWS - 3):
           if board[row:row + 4][col].sum() == player * 4:
               return True

   # Check for diagonal wins (positive slope)
   for row in range(ROWS - 3):
       for col in range(COLS - 3):
           if np.diag(board[row:row + 4, col:col + 4]).sum() == player * 4:
               return True

   # Check for diagonal wins (negative slope)
   for row in range(3, ROWS):
       for col in range(COLS - 3):
           if np.diag(np.fliplr(board[row - 3:row + 1, col:col + 4])).sum() == player * 4:
               return True

   # No winner found
   return False

# Create a function to play the game
def play_game():
   # Initialize the game board
   board = create_board()

   # Set up the players
   player1 = 1
   player2 = 2

   # Start the game loop
   current_player = player1
   while True:
       # Display the game board
       display_board(board)

       # Get the player's move
       column = int(input(f"Player {current_player}, enter column: ")) - 1

       # Check if the move is valid
       if column < 0 or column >= COLS or board[0][column] != 0:
           print("Invalid move. Try again.")
           continue

       # Find the lowest empty row in the column
       row = np.argmax(board[:, column] == 0)

       # Mark the square with the player's symbol
       board[row][column] = current_player

       # Check if the player has won
       if check_win(board, current_player):
           # Display the winner
           display_board(board)
           print(f"Player {current_player} wins!")
           break

       # Check if the board is full (tie game)
       if np.all(board != 0):
           display_board(board)
           print("Tie game!")
           break

       # Switch players
       current_player = player2 if current_player == player1 else player1

# Play the game
play_game()
Example games:

# Example 1:
Player 1 wins horizontally

1 | 2 | 3 | 4 | 5 | 6 | 7
-------------------------
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |
| O |   |   |   |   |   |
| O | O | O | O |   |   |

# Example 2:
Player 2 wins diagonally (negative slope)

1 | 2 | 3 | 4 | 5 | 6 | 7
-------------------------
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   | O |   |   |
|   |   | O | X |   |   |
|   | O |
