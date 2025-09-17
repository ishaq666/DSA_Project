# ===================================
# GUI-based Tic Tac Toe using Tkinter
# ===================================

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        """Initialize game window and board."""
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Track current player (X starts)
        self.current_player = "X"

        # Create 3x3 grid of buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def check_winner(self):
        """Check if current player has won."""
        # Rows and columns
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True

        # Diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        """Check if the board is full and no winner (draw)."""
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def on_click(self, row, col):
        """Handle button click for a move."""
        if self.buttons[row][col]["text"] == "":
            # Place move
            self.buttons[row][col]["text"] = self.current_player

            # Check win/draw
            if self.check_winner():
                messagebox.showinfo("Game Over", f"🎉 Player {self.current_player} wins!")
                self.root.quit()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.quit()
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"

    def run(self):
        """Run the Tkinter event loop."""
        self.root.mainloop()


# Run only if file is executed directly
if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
