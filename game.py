import tkinter as tk
from tkinter import ttk
import random

class Board:
    def __init__(self,root):
        self.root = root
        self.mainframe = ttk.Frame(self.root,padding="10 10 10 10")
        self.mainframe.grid(row=0,column=0,sticky='nsew')
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(0,weight=1)

        self.board = [1,2,3,4,5,6,7,8,0]
        self.initial_board = self.board[:]
        self.buttons=[]
        
        self.root.geometry("400x400")
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 25))
        self.setup_grid()

    def setup_grid(self):
        for i in range(3):
            self.mainframe.rowconfigure(i, weight=1, uniform="row")
            self.mainframe.columnconfigure(i, weight=1, uniform="col")
        for i in range(9):
            btn = ttk.Button(self.mainframe,
                            text=self.get_button_text(i),
                            command=lambda idx=i: self.handle_click(idx)
                            )
            btn.grid(row=i//3, column=i%3, sticky='nsew')
            self.buttons.append(btn)

        self.mainframe.rowconfigure(3, weight=0)
        self.control_frame = ttk.Frame(self.mainframe, padding="5")
        self.control_frame.grid(row=3, column=0, columnspan=3, sticky="s")

        self.scramble_btn = ttk.Button(self.control_frame, text="Scramble", command=self.scramble)
        self.scramble_btn.pack(side="left", padx=5)
        self.reset_btn = ttk.Button(self.control_frame, text="Reset", command=self.reset_scramble)
        self.reset_btn.pack(side="left", padx=5)
    def get_button_text(self,i):
        text = self.board[i]
        return str(text) if text!=0 else ''

    def handle_click(self,idx):
        print(f'clicked button {idx}')
        if self.board[idx] == 0:
            return
        zero_idx = self.board.index(0)
        if idx in self.valid_moves(zero_idx):

            #swap the clicked button with the zero button
            self.swap(idx,zero_idx)
            self.update_btn_ui()

    def update_btn_ui(self):
        #update the button text based on the current board state
        for i,btn in enumerate(self.buttons):
            btn.config(text = self.get_button_text(i))

    def valid_moves(self,i):
        #given the index of the zero button, return the indices of the buttons that can be swapped with it
        r,c = divmod(i,3)
        adj_posn = [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]
        valid_indices = []

        for r_new,c_new in adj_posn:
            if 0 <= r_new <3 and 0 <= c_new < 3:
                idx = r_new*3 + c_new
                valid_indices.append(idx)
        return valid_indices
    def swap(self,idx,zero_idx):
        self.board[idx], self.board[zero_idx] = self.board[zero_idx],self.board[idx]


    def is_solvable(self,board_state):
        #checks if the given board state is solvable by counting the number of inversions
        inversion=0
        flat_board = [num for num in board_state if num!=0]
        for i in range(len(flat_board)):
            for j in range(i+1,len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversion += 1
        return inversion % 2 == 0
    #gives scrambled solvable board
    def scramble(self):
        new_board = self.board[:]
        while True:
            random.shuffle(new_board)
            if self.is_solvable(new_board) and new_board != [1,2,3,4,5,6,7,8,0]: 
                break
        self.board = new_board
        self.initial_board = new_board[:]
        self.update_btn_ui()
    def is_solved(self):
        return self.board == [1,2,3,4,5,6,7,8,0]
    #resets the board to the initial scrambled state
    def reset_scramble(self):
        self.board = self.initial_board[:]
        self.update_btn_ui()
if __name__== '__main__':
  root = tk.Tk()
  root.title('8 Puzzle Game')
  app = Board(root)
  root.mainloop()