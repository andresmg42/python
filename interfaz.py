# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 12:29:40 2022

@author: andres
"""
import tkinter as tk
from fractions import Fraction

def matriz(n,m):
    matriz=[[0]*m]*n
    return matriz

def pressedkey(enter):
    global text
    global matrix
    global e_row_column
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row_column.set(f'row {i+1}, column {j+1}')
            matrix[i][j]=float(Fraction(e_row_column.get()))
            e_row_column.delete(0,'end')
    
    


gui=tk.Tk()

gui.title('Calculadora De Matrices')
gui.geometry('600x400')

f_ing=tk.Frame(gui)
f_createm=tk.Frame(gui)

l_width=tk.Label(f_ing,text='width = ')
l_height=tk.Label(f_ing,text='height = ')

# width_var=tk.StringVar()
# height_var=tk.StringVar()
row_column=tk.StringVar()

#row_column.set('row 1, column 1')


e_width=tk.Entry(f_ing)
e_height=tk.Entry(f_ing)



l_width.grid(row=0,column=0)
l_height.grid(row=1,column=0)

e_width.grid(row=0,column=1)
e_height.grid(row=1,column=1)

b_crear=tk.Button(f_ing,text='enter')
b_crear.grid(row=2,column=0)

l_row_column=tk.Label(f_createm,textvariable=row_column)
e_row_column=tk.Entry(f_createm)


l_row_column.grid(row=0,column=0)
e_row_column.grid(row=0,column=1)


f_ing.grid(row=0,column=0)
f_createm.grid(row=1,column=0)



e_row_column.bind("<Return>",pressedkey)



# tabcontrol=ttk.Notebook(gui)

# tab1=tk.Frame(tabcontrol)
# tab2=tk.Frame(tabcontrol)
# tab3=tk.Frame(tabcontrol)
# tabcontrol.add(tab1,text='reduce')
# tabcontrol.add(tab2,text='inverse')
# tabcontrol.add(tab3,text='determinant')
# tabcontrol.pack(expand=1,fill='both')
gui.mainloop()

matrix=matriz(int(e_width.get()),int(e_height.get()))
# print(matriz)