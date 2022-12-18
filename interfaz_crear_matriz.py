# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:16:22 2022

@author: andres
"""

from tkinter import Tk, Label, StringVar, Button, Entry
window = Tk()
window.title("Matrix")
window.geometry("650x500+120+120")
window.configure(bg='blue')
window.resizable(False, False)

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

# callback function to get your StringVars

    
def get_mat():
    global matriz
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())

    

Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), 
      bg="green").place(x=20, y=100)

x2 = 0
y2 = 0
rows, cols = (2,2)
l_width=Label(window,text='width').place(x=10,y=10)
l_height=Label(window,text='height').place(x=10,y=40)
e_width=Entry(window).place(x=50,y=10)
e_height=Entry(window).place(x=50,y=40)

for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(StringVar())
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=50 + x2, y=150 + y2)
        x2 += 30

    y2 += 30
    x2 = 0
button= Button(window,text="Submit", bg='bisque3', width=15, command=get_mat)
button.place(x=260,y=400)


window.mainloop()
