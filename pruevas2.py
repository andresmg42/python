# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:47:23 2022

@author: andres
"""
from tkinter import *

win=Tk()

def pressedkey(enter):
    print('enter')
    
text=Entry(win)
text.bind("<Return>",pressedkey)

text.pack()
win.mainloop()