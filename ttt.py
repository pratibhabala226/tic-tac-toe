import os

def print_board(board):
    """Function to print the game board."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen for better visibility
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Function to check if a player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def check_draw(board):
    """Function to check if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def player_move(board, player):
    """Function to handle a player's move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                raise ValueError("Invalid move. Please enter a number between 1 and 9.")
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This spot is already taken. Please choose another.")
        except ValueError as e:
            print(e)

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize the game board
    current_player = "X"
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
