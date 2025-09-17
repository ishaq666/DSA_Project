# =========================================
# Main Menu - Run Console or GUI Tic Tac Toe
# =========================================

from tic_tac_toe import tic_tac_toe
from tic_tac_toe_gui import TicTacToeGUI

# Show menu
print("Choose version:")
print("1. Console")
print("2. GUI")

choice = input("Enter 1 or 2: ")

if choice == "1":
    # Run console version
    tic_tac_toe()
elif choice == "2":
    # Run GUI version
    game = TicTacToeGUI()
    game.run()
else:
    print("Invalid choice")
