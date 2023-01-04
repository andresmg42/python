# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:13:18 2022

@author: user
"""

"""
Created on Wed Feb 23 18:10:42 2022

@author: Andres Ortega
"""

import reduccion as up
import determinante as du
import copy
from tkinter import *



gui=Tk()
text_area=Text(gui,wrap=WORD,width=50,height=50,font=('Times New Roman',15))

# def kinter():
#     frame=Tk()
#     frame.mainloop()
    
def iniciar():
    print('WELCOME TO A.O. MATRIX REDUCER PROGRAM')
    print('-------------------------------------------------------------------------')
    print('!GOOD LUCK¡')
    print('--------------------------------------------------------------------------')
    n=int(input("please type the number of rows : "))
    m=int(input("please type the number of columns :"))
    print('--------------------------------------------------------------------------')
    matriz=up.create_matrix(n, m)
    
    
    
    flag=True
    
    while flag:
        
      
        # try:
        print('menu------------------------------------------------------------------')
        print('''
        0. REDUCE A MATRIX
        1. FIND THE INVERSE
        2.FIND THE DETERMINANT BY STAGGERED WAY
        3.INPUT A NEW MATRIX
        4.EXIT''')
           
        o=int(input('''please type one option :'''))
        print()
    

    



        if o==0:
            print('-------------------------SOLUTION---------------------------------')
            print()
            print()
            matrix=copy.deepcopy(matriz)
            print(up.Mostrar(matrix))
            #text=up.Mostrar(matrix)+'\n'
            # text_area.insert(END,text)
            # try:
            #up.redux(matrix, n)
            # text=up.redux(matrix,n)+'\n'
            print(up.redux(matrix,n))
            # text_area.insert(END,text)
            # text_area.pack()
            # text_area.mainloop()
            # except:
            #     print('!!! THE MATRIX IS NOT INVERTIBLE OR HAVE INFINITE SOLUTIONS ¡¡¡')
            
        
        elif o==1:
            print('-------------------------SOLUTION---------------------------------')
            matrix=copy.deepcopy(matriz)
            matrix=up.add_identity(matrix)
            print()
            print()
    
            print(up.Mostrar(matrix))
            try:
                print(up.redux(matrix,n))
            except:
                print('!!! THE MATRIX IS NOT INVERTIBLE OR HAVE INFINITE SOLUTIONS ¡¡¡')
            
        elif o==2:
            print('-------------------------SOLUTION---------------------------------')
            matrix=copy.deepcopy(matriz)
            print(du.mean(matrix))
            
        elif o==3:
            print('--------------------------------------------------------------------------')
            n=int(input("please type the number of rows : "))
            m=int(input("please type the number of columns :"))
            print('--------------------------------------------------------------------------')
    
            matriz=up.create_matrix(n, m) 
            
    
        elif o==4:
            print('GOOD BYE!-----------------------------------------------------------------')
            flag=False
        
        else:
            print()
            print('PLEASE TYPE A VALID OPTION!!!')
            print()
            
       
            
        #     print()
        #     print('PLEASE TYPE A VALID OPTION!!!')
        #     print()
        #     pass

iniciar()