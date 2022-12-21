# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:16:22 2022

@author: andres
"""

from tkinter import *
import reduccion as rd
import determinante as dt
from fractions import Fraction
window = Tk()
window.title("Matrix")
window.geometry("650x500+120+120")
window.configure(bg='blue')
window.resizable(False, False)
import copy

# empty arrays for your Entrys and StringVars
text_var = []
entries = []

# callback function to get your StringVars

    
def get_mat(rows,cols):
    global matriz
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(float(Fraction(text_var[i][j].get())))
    return matrix

def reducir(rows,cols):
    'hacer validaciones'
    matriz=get_mat(rows,cols)
    matrix=copy.deepcopy(matriz)
    text=rd.Mostrar(matrix)+'\n'
    text+=rd.redux(matrix,rows)
    kinter(text)

def determinante(rows,cols):
    'hacer validaciones'
    matriz=get_mat(rows, cols)
    matrix=copy.deepcopy(matriz)
    text=rd.Mostrar(matrix)+'\n'
    text=dt.mean(matrix)
    kinter(text)

def kinter(text):
    
    window=Tk()
    text_area=Text(window,wrap=WORD,width=50,height=50,font=('Times New Roman',15))
    text_area.insert(END,text)
    text_area.pack()
    text_area.mainloop()
    
def create_mat(rows,cols,gui):
    frame=Frame(gui)
   
    for i in range(rows):
        # append an empty list to your two arrays
        # so you can append to those later
        text_var.append([])
        entries.append([])
        for j in range(cols):
            # append your StringVar and Entry
            text_var[i].append(StringVar())
            entries[i].append(Entry(frame, textvariable=text_var[i][j],width=3))
            # entries[i][j].place(x=50 + x2, y=150 + y2)
            entries[i][j].grid(row=i,column=j,padx=3,pady=3)
            
    frame.place(x=10,y=150)
    

Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), 
      ).place(x=20, y=100)

heigth=StringVar()
width=StringVar()

l_width=Label(window,text='width').place(x=10,y=10)
l_height=Label(window,text='height').place(x=10,y=40)
e_width=Entry(window,textvariable=width).place(x=50,y=10)
e_height=Entry(window,textvariable=heigth).place(x=55,y=40)





button_c=Button(window,text='create',width=15,command=lambda:create_mat(int(heigth.get()),int( width.get()),window))
button_c.place(x=10,y=70)        
b_reducir= Button(window,text="redux", width=15, command=lambda:reducir(int(heigth.get()),int(width.get())))
b_reducir.place(x=260,y=400)
b_determinante=Button(window,text='find det.',width=15,command=lambda:determinante(int(heigth.get()),int( width.get())))
b_determinante.place(x=260,y=200)


window.mainloop()
