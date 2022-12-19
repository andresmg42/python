# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 16:47:17 2022

@author: andres
"""
from tkinter import *
def new_frame(gui,string):
    frame=Frame(gui)
    var=StringVar()
    var.set(string)
    entry=Entry(frame,textvariable=var)
    entry.place(x=10,y=10)
    #entry.pack()
    frame.place(x=10,y=100)
def entrada():
    window=Tk()
    window.geometry('200x300')
    width=StringVar()
    height=StringVar()
    l_width=Label(window,text='width').place(x=10,y=10)
    l_height=Label(window,text='height').place(x=10,y=40)
    e_width=Entry(window,textvariable=width).place(x=50,y=10)
    e_height=Entry(window,textvariable=height).place(x=55,y=40)
    button=Button(window,text='PRESS',command=lambda:new_frame(window,height.get()))
    button.pack(side='bottom')
   
    mainloop()
    
entrada()