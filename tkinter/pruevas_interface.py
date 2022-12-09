from tkinter import *


gui=Tk()

def kinter():
    frame=Tk()
    frame.mainloop()

text='me cago en la lechen\n'
text2='ME CAGO NE LA PAPA'
text_area = Text(gui,wrap =WORD,width = 40,height = 10,font = ("Times New Roman",15))
buton=Button(gui,text='sunday',command=kinter)
text_area.insert(END,text)
text_area.delete('1.0',END)
text_area.insert(END,text2)

buton.pack()
text_area.pack()
gui.mainloop()