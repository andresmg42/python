# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 14:16:22 2022

@author: andres
"""
"corregir el tamaño de la caja de texto para las matrices 4x4"
from tkinter import *
from tkinter import messagebox
import reduccion as rd
import determinante as dt
from fractions import Fraction
from PIL import ImageTk,Image
import copy



def start():
    presentation()
    global window 
    window = Tk()
    window.geometry("800x500+120+120")
    window.wm_attributes('-transparentcolor', '#ab23ff')
    image_=Image.open('./univalle4.jpg')
    bg=ImageTk.PhotoImage(image_)
    l_image=Label(window,image=bg)
    l_image.place(x=0,y=0)
    window.title("Matrix")
    l_title=Label(text='Welcome to Matrix Calculator',bg='red',fg='white',font=('Times New Romman',15))
    l_title.place(x=220,y=30)
    window.resizable(False, False)
    global text_var
    text_var=[]
    global entries
    entries = []
    Label(window, text="OPTIONS:", font=('arial', 10, 'bold'), 
          bg='red',fg='white').place(x=20, y=100)

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

def warning(num):
    if num==1:
        messagebox.showwarning(title='warning',message='the matrix is invalid,\nplease type a valid matrix')
    else:
        messagebox.showwarning(title='warning',message='the matrix is not square')
    
def get_mat(rows,cols):
    global matriz
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(float(Fraction(text_var[i][j].get())))
    return matrix

def reducir(rows,cols):
    try:
        matriz=get_mat(rows,cols)
        matrix=copy.deepcopy(matriz)
        text=rd.Mostrar(matrix)+'\n'
        text+=rd.redux(matrix,rows)
        kinter(text)
    except:
        # text='!!! THE MATRIX IS NOT VALID OR HAVE INFINITE SOLUTIONS ¡¡¡'
        # messagebox.showwarning(title='warning',message='the matrix is not valid\nplease type a valid matrix')
        warning(1)
    

def determinante(rows,cols):
    
    try:
        if rows==cols:
            matriz=get_mat(rows, cols)
            matrix=copy.deepcopy(matriz)
            text=rd.Mostrar(matrix)+'\n'
            text=dt.mean(matrix)
            kinter(text)
        else:
            # text='IT IS NOT A SQUARE MATRIX'
            # messagebox.showwarning(title='warning',message='the matrix is not square')
            warning(2)
    except:
        # text='!!!THE MATRIX IS NOT VALID!!!\nPLEASE TYPE A VALID MATRIX'
        # messagebox.showwarning(title='warning',message='!the matrix is not valid¡\nplease type a valid matrix')
        warning(1)
    
    # kinter(text)


def inversa(rows,cols):
    if rows==cols:
        try:
            matriz=get_mat(rows, cols)
            matrix=copy.deepcopy(matriz)
            text=rd.Mostrar(matrix)+'\n'
            matrix=rd.add_identity(matrix)
            text+=rd.redux(matrix,rows)
            kinter(text)
        except:
            # text='THE MATRIX IS NOT INVERTIBLE'
            # messagebox.showwarning(title='warning',message='The matrix is invalid, please type a valid matrix')
            warning(1)
    else:
        # text='THE MATRIX IS NOT SQUARE'
        # messagebox.showwarning(title='warning',message='the matrix is not square')
        warning(2)
    # kinter(text)
    


def kinter(text):
    
    window=Tk()
    scroll=Scrollbar(window,orient=HORIZONTAL,troughcolor='red',width=30)
    scroll.pack(side=BOTTOM,fill=X)
    text_area=Text(window,width=20,height=30,wrap=NONE,font=('Courier',15),fg='red',bg='black',xscrollcommand=scroll.set)
    text_area.insert(END,text)
    text_area.config(state=DISABLED)
    text_area.pack(expand=True,fill=BOTH)
    scroll.config(command=text_area.xview)
    button=Button(window,text='close',command=lambda:destroy(window),bg='red',fg='black')
    button.pack(side=BOTTOM)
    mainloop()
    
def destroy(window):
    window.destroy()

def presentation():
    window=Tk()
    text=Text(window,width=70,height=20,bg='black',fg='red',)
    string="""
VALLEY UNIVERSITY\n
SISTEM ENGINEERING\n
members:\n
Andres David Ortega Arteaga- 2241885
Juan David Pinto Rodríguez- 2240440
Santiago Ruiz Cortes- 2241586\n
This program can reduce, find inverse and find the determinant of a matrix up to 8x8 in size. To type a new matrix press the restart button and type a new size. To start the program just press continue\n                               !WARNING¡\nThis program only work whit matrix that have one solution or infinite solutions."""
    
    text.insert(END,string)
    text.tag_configure('tag name',justify='center')
    text.config(state=DISABLED)
    button=Button(window,text='continue',command=lambda: destroy(window),bg='red',fg='black')
    text.pack()
    button.place(x=250,y=270)
    mainloop()

    
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
                    entries[i].append(Entry(frame, textvariable=text_var[i][j],width=5,font=('Times New Roman',18)))
                    # entries[i][j].place(x=50 + x2, y=150 + y2)
                    entries[i][j].grid(row=i,column=j,padx=3,pady=3)
            label=Label(window,text='enter your matrix:',bg='red',fg='white')
            label.place(x=230,y=180)
            frame.place(x=230,y=200)
        else:
            text='!PLEASE TYPE A SIZE GREATER THAN 1¡'
            messagebox.showwarning(title='warning',message=text)
            # kinter(text)
    except:
        text='!PLEASE TYPE A SIZE VALUE¡'
        # kinter(text)
        messagebox.showwarning(title='warning',message=text)
    
start()

