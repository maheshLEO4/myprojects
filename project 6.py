# Tic Tac Toe Game 
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Set background color for the main window
        self.root.config(bg="lightblue")

        self.create_board()

        # Bind Ctrl+M to minimize the window
        self.root.bind("<Control-m>", self.minimize_window)
        
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('normal', 20), width=5, height=2, 
                               command=lambda i=i: self.on_button_click(i),bg="Tan") 
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.buttons[index]["text"] == "" and self.current_player:
            self.buttons[index]["text"] = self.current_player
            self.board[index] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button["text"] = ""

    def minimize_window(self, event=None):
        self.root.iconify()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
