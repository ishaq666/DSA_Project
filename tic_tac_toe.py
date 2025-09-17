# ================================
# Console-based Tic Tac Toe Game
# ================================

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    """Check if the given player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board):
    """Check if the game is a draw (all cells filled)."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Main game loop for Tic Tac Toe (console version)."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")

        try:
            # Take input for row and column
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        # Validate move
        if row not in range(3) or col not in range(3):
            print("Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        # Place the move
        board[row][col] = current_player

        # Check win/draw
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run if this file is executed directly
if __name__ == "__main__":
    tic_tac_toe()
