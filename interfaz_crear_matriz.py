# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:16:22 2022

@author: andres
"""
"corregir el tamaño de la caja de texto para las matrices 4x4"
from tkinter import *
import reduccion as rd
import determinante as dt
from fractions import Fraction
from PIL import ImageTk,Image
import copy

def start():
    
    global window 
    window = Tk()
    window.geometry("650x500+120+120")
    window.wm_attributes('-transparentcolor', '#ab23ff')
    image_=Image.open('C:/Users/andres/Desktop/proyecto finnal/python/univalle4.jpg')
    bg=ImageTk.PhotoImage(image_)
    l_image=Label(window,image=bg)
    l_image.place(x=0,y=0)
    window.title("Matrix")
    l_title=Label(text='Welocome to Matrix Calculator',bg='red',fg='white',font=('Times New Romman',15))
    l_title.place(x=220,y=30)
    window.resizable(False, False)
    global text_var
    text_var=[]
    global entries
    entries = []
    Label(window, text="OPTIONS:", font=('arial', 10, 'bold'), 
          ).place(x=20, y=100)

    heigth=StringVar()
    width=StringVar()

    l_width=Label(window,text='width').place(x=10,y=10)
    l_height=Label(window,text='height').place(x=10,y=40)
    e_width=Entry(window,textvariable=width).place(x=50,y=10)
    e_height=Entry(window,textvariable=heigth).place(x=55,y=40)





    button_c=Button(window,text='create',width=15,bg='red',fg='white',command=lambda:create_mat(heigth.get(),width.get(),window))
    button_c.place(x=10,y=70)        
    b_reducir= Button(window,text="redux", width=15, bg='red',fg='white',command=lambda:reducir(int(heigth.get()),int(width.get())))
    b_reducir.place(x=10,y=250)
    b_determinante=Button(window,text='find det.',width=15,bg='red',fg='white',command=lambda:determinante(int(heigth.get()),int( width.get())))
    b_determinante.place(x=10,y=200)
    b_inversa=Button(window,text='inversa',width=15,bg='red',fg='white',command=lambda:inversa(int(heigth.get()),int(width.get())))
    b_inversa.place(x=10,y=150)
    b_reset=Button(window,text='restart',width=15,bg='red',fg='white',command=restart)
    b_reset.place(x=10,y=300)


    window.mainloop()

def restart():
    window.destroy()
    start()


    
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
    try:
        matriz=get_mat(rows,cols)
        matrix=copy.deepcopy(matriz)
        text=rd.Mostrar(matrix)+'\n'
        text+=rd.redux(matrix,rows)
    except:
        text='!!! THE MATRIX IS NOT VALID OR HAVE INFINITE SOLUTIONS ¡¡¡'
    kinter(text)

def determinante(rows,cols):
    'hacer validaciones'
    
    try:
        if rows==cols:
            matriz=get_mat(rows, cols)
            matrix=copy.deepcopy(matriz)
            text=rd.Mostrar(matrix)+'\n'
            text=dt.mean(matrix)
        else:
            text='IT IS NOT A SQUARE MATRIX'
    except:
        text='!!!THE MATRIX IS NOT VALID!!!\nPLEASE TYPE A VALID MATRIX'
    
    kinter(text)


def inversa(rows,cols):
    try:
        matriz=get_mat(rows, cols)
        matrix=copy.deepcopy(matriz)
        text=rd.Mostrar(matrix)
        matrix=rd.add_identity(matrix)
        text=rd.redux(matrix,rows)
    except:
        text='THE MATRIX IS NOT INVERTIBLE'
    kinter(text)
    
# def restart():
#     frame.d

def kinter(text):
    
    window=Tk()
    text_area=Text(window,width=50,height=30,font=('Times New Roman',15),fg='red',bg='black')
    text_area.insert(END,text)
    text_area.pack()
    text_area.mainloop()
    
def create_mat(rows,cols,gui):
    try:
        rows=int(rows)
        cols=int(cols)
        if rows>1 and cols>1:
            frame=Frame(gui)
           
            for i in range(rows):
                # append an empty list to your two arrays
                # so you can append to those later
                text_var.append([])
                entries.append([])
                for j in range(cols):
                    # append your StringVar and Entry
                    text_var[i].append(StringVar())
                    entries[i].append(Entry(frame, textvariable=text_var[i][j],width=3,font=('Times New Roman',18)))
                    # entries[i][j].place(x=50 + x2, y=150 + y2)
                    entries[i][j].grid(row=i,column=j,padx=3,pady=3)
            label=Label(window,text='enter your matrix:',bg='red',fg='white')
            label.place(x=280,y=180)
            frame.place(x=280,y=200)
        else:
            text='!PLEASE TYPE A SIZE GREATER THAN 1¡'
            kinter(text)
    except:
        text='!PLEASE TYPE A VALID VALUE¡'
        kinter(text)
    

start()
