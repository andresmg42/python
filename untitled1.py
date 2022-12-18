# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:46:31 2022

@author: andres
"""

from tkinter import *
from fractions import Fraction

win=Tk()
matriz=[[0]*2]*2
lista=[]

def  create_m():
    cr=Tk()



def pressedkey(enter):
    count=0
    global text
    global lista
    if count<4:
        lista.append(text.get())
        text.delete(0,'end')
        count+=1
           

text=Entry(win)
text.bind("<Return>",pressedkey)



text.pack()

win.mainloop()

contador=0
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j]=lista[contador]
        contador+=1      
print(matriz) 