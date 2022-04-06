from tkinter import *
import sudoku_functions
import pandas as pd
import random

def get_board():
    df = pd.read_csv("sudoku.csv")
    quiz = df.iloc[0]['quizzes']
    row_num = 0
    board = [[] for i in range(9)]
    for i in range(0, 81, 9):
        row = (quiz[i:i + 9])
        col = 0
        for num in row:
            board[row_num].append(int(num))
        row_num += 1
    return board,df

def get_current_board(entrys):
    board = [[] for i in range(9)]
    row_num = 0
    for row in entrys:
        for entry in row:
            if entry.get(1.0) == '\n':
                board[row_num].append(0)
            else:
                board[row_num].append(int(entry.get(1.0)))
        row_num +=1
    return board

def create_board():
    board,df = get_board()
    entrys = list()
    for x in range(9):
        temp_list = []
        for i in range(9):
            temp_list.append(i)
        entrys.append(temp_list)

    root =Tk()
    root.title("Sudoku Solver")
    playing_board = Frame(root,padx=5,pady=5,bd=3,width=27,height=18)
    playing_board.grid(row=0,column=0)
    for row in range(9):
        for col in range(9):
            e = Text(playing_board, height=2, width=3,padx=5,pady=5,bd=4)
            entrys[row][col] = e
            if board[row][col] != 0:
                e.insert(END,board[row][col])
            e.config(state=DISABLED)
            e.grid(row=row,column=col)

    button_frame = Frame(root).grid(row=0,column=0)
    get_current_board(entrys)
    b_solve = Button(playing_board,text = "Solve",width=6,pady=5,command=lambda:sudoku_functions.solve(get_current_board(entrys),entrys)).grid(row=9,column=3)
    b_new = Button(playing_board, text="New",width=6,pady=5,command=lambda:new_board(entrys,df)).grid(row=9,column=5)
    root.mainloop()

def update_square(row,col,value,entrys):
    entrys[row][col].config(state="normal")
    entrys[row][col].delete(1.0,END)
    entrys[row][col].insert(END,value)
    entrys[row][col].config(state=DISABLED)

def new_board(entrys,df):
    n = random.randint(0, 99999)
    quiz = df.iloc[n]['quizzes']
    row_num = 0
    board = [[] for i in range(9)]
    for i in range(0, 81, 9):
        row = (quiz[i:i + 9])
        col = 0
        for num in row:
            board[row_num].append(int(num))
        row_num += 1

    for row in range(9):
        for col in range(9):
            entrys[row][col].config(state="normal")
            entrys[row][col].delete(1.0, END)
            if board[row][col] != 0:
                entrys[row][col].insert(END,board[row][col])
            entrys[row][col].config(state=DISABLED)

if __name__ == '__main__':
    create_board()
