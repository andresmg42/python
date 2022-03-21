# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:13:18 2022

@author: user
"""

"""
Created on Wed Feb 23 18:10:42 2022

@author: Andres Ortega
"""

import untitled0 as up
import determinante_ultimo_2 as du
import copy

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
    
  
        
    try:
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
            up.Mostrar(matrix)
            try:
                up.redux(matrix,n)
            except:
                print('!!! THE MATRIX IS NOT INVERTIBLE OR HAVE INFINITE SOLUTIONS ¡¡¡')
            
        
        elif o==1:
            print('-------------------------SOLUTION---------------------------------')
            matrix=copy.deepcopy(matriz)
            matrix=up.add_identity(matrix)
            print()
            print()
    
            up.Mostrar(matrix)
            try:
                up.redux(matrix,n)
            except:
                print('!!! THE MATRIX IS NOT INVERTIBLE OR HAVE INFINITE SOLUTIONS ¡¡¡')
            
        elif o==2:
            print('-------------------------SOLUTION---------------------------------')
            matrix=copy.deepcopy(matriz)
            du.mean(matrix)
            
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
        
   
        
    except:
        print()
        print('PLEASE TYPE A VALID OPTION!!!')
        print()
        pass
