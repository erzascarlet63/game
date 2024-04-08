import tkinter as tk
import math
from tkinter import messagebox
#Ahmad Irfan Nabihan bin Shukri 2212159
class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.mode = None
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        mode_label = tk.Label(master, text="Select Mode:")
        mode_label.grid(row=3, column=0, columnspan=3)
        
        

        self.bot_mode_button = tk.Button(master, text="Bot vs Human", command=self.select_bot_mode)
        self.bot_mode_button.grid(row=4, column=0)

        self.two_player_mode_button = tk.Button(master, text="2 Player", command=self.select_two_player_mode)
        self.two_player_mode_button.grid(row=4, column=1)
        
        self.resetbutton = tk.Button(master, text="Reset", command=self.reset_board)
        self.resetbutton.grid(row=4, column=2)
        
        

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text='', width=15, height=5,
                                                command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].config(state=tk.DISABLED)
                
        messagebox.showinfo("Tic Tac Toe","Select your mode!")
        

    def select_mode(self, mode):
        self.mode = mode
        self.bot_mode_button.config(state=tk.DISABLED)
        self.two_player_mode_button.config(state=tk.DISABLED)
        self.enable_board_buttons()

    def select_bot_mode(self):
        self.select_mode('bot')

    def select_two_player_mode(self):
        self.select_mode('two_player')
        
    def enable_board_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.NORMAL)       

    def make_move(self, row, col):
        if self.mode == 'bot' and self.current_player == 'O':
            return
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if not self.is_game_over():
                if self.mode == 'bot':
                    if self.current_player == 'X':
                        self.current_player = 'O'
                    self.bot_move()
                elif self.mode == 'two_player':
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                self.show_result()
        else:
            messagebox.showerror("Tic Tac Toe", "Invalid move! Try again")

    def bot_move(self):
        best_score = -math.inf
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = 'O'
        self.buttons[best_move[0]][best_move[1]].config(text='O')
        if not self.is_game_over():
            self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.is_winner(board, 'X'):
            return -10 + depth
        elif self.is_winner(board, 'O'):
            return 10 - depth
        elif self.is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def is_winner(self, board, player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
            if all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def show_result(self):
        if self.is_winner(self.board, 'X'):
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
        elif self.is_winner(self.board, 'O'):
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
        elif self.is_board_full(self.board):
            messagebox.showinfo("Tic Tac Toe", "Tie !")
        self.reset_board()
        
    def is_board_full(self, board):
        for row in board:
            if ' ' in row:
                return False
        return True

    def is_game_over(self):
        return self.is_winner(self.board, 'X') or \
               self.is_winner(self.board, 'O') or \
               self.is_board_full(self.board)
               
    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
                self.buttons[i][j].config(state=tk.DISABLED)
        self.current_player = 'X'
        self.mode = None
        self.bot_mode_button.config(state=tk.NORMAL)
        self.two_player_mode_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
