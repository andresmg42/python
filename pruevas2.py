# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:47:23 2022

@author: andres
"""
from tkinter import *
from fractions import Fraction

win=Tk()

def pressedkey(enter):
    global text
    print(text.get())
    text.delete(0,'end')
    
text=Entry(win)
text.bind("<Return>",pressedkey)

text.pack()

# entry=Entry(win)
# var=entry.get()
# print(var)
# entry.pack()
win.mainloop()

def matriz(n,m):
    matriz=[[0]*m]*n
    return matriz
matrix=matriz(3,3)

def pressedkey(enter):
    global text
    global matrix
    global e_row_column
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row_column.set(f'row {i+1}, column {j+1}')
            matrix[i][j]=float(Fraction(e_row_column.get()))
            e_row_column.delete(0,'end')
    return matrix


def create_matrix(n, m):
    matrix = [[0]*m]*n

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            global e_row_column
            global row_column
            row_column.set(f'row {i+1}, column {j+1}')
            entrada=e_row_column.get()
            e_row_column.delete('1.0','end')
            num = float(Fraction(entrada))
            matrix[i][j] = num
    return matrix