# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:03:30 2022

@author: andres
"""
from fractions import Fraction

import numpy as np
import copy
# type the number of row 1, column 1 :0

# type the number of row 1, column 2 :3

# type the number of row 1, column 3 :2

# type the number of row 2, column 1 :0

# type the number of row 2, column 2 :2

# type the number of row 2, column 3 :5

# type the number of row 3, column 1 :6

# type the number of row 3, column 2 :0

# type the number of row 3, column 3 :8

matriz=[[0,0,2,0],
        [0,0,4,7],
        [0,2,0,5],
        [1,3,4,0]]

# matriz=[[0,3,2],
#         [0,7,5],
#         [6,2,8]]
# def Mostrar(matriz):
#     print('the matrix is as follows :')
#     a = np.array(matriz)

#     s = [[str(Fraction(e).limit_denominator()) for e in row] for row in a]
#     lens = [max(map(len, col)) for col in zip(*s)]
#     fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
#     table = [fmt.format(*row) for row in s]
#     print('\n'.join(table))
#     print()

# def swap_rows(matriz,column):
#     signs=[]
#     for i in range(column,len(matriz)):
#         counter = 1
        
#         while matriz[i][column] == 0 and i+counter < len(matriz):
#             if matriz[i+counter][column]!=0:
#                 matriz[i], matriz[i+counter] = matriz[i+counter], matriz[i]
#                 signs.append(-1)
#                 print("R{0}<-->R{1}".format(i+1, i+counter+1))
#                 Mostrar(matriz)
#             counter += 1
                

    
#     return matriz

# swap_rows(matriz, 0)



def add_lists(list1, list2):
    new = []
    for i in range(len(list1)):
        numero = list1[i]+list2[i]
        new.append(numero)
    return new

def multiply_row(row, num):
    new_row = []
    for i in range(len(row)):
        new_num = row[i]*num
        new_row.append(new_num)
    return new_row

def part_list(list1, num):
    if num != 0:
        new = []
        for i in list1:
            new_num = i/num
            new.append(new_num)
    else:
        new = list1
    return new

def Mostrar(matriz):
    print('the matrix is as follows :')
    a = np.array(matriz)

    s = [[str(Fraction(e).limit_denominator()) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print()
    
def redux(row,column,matriz):
    num=matriz[column][row]*-1*(1/matriz[row][row])
    if num>0:
        sign='+'
        print('R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign))
    elif num<0:
        sign=''
        print('R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign))
    
    
    # print('R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(matriz[column][row]*-1).limit_denominator()),column+1,sign))
    new_list=multiply_row(matriz[row],num )
    matriz[column]=add_lists(matriz[column],new_list)
    return matriz

def determinant(matriz):
    mult=1
    for i in range(len(matriz)):
       mult*=matriz[i][i]
    return mult
       

# def swap_rows(matriz):
#     nums=[]
#     for i in range(len(matriz)-1):
#         counter = len(matriz)-1
#         while matriz[i][i] == 0 and counter-i >-1:
#             matriz[i], matriz[counter-i] = matriz[counter-i], matriz[i]
#             nums.append(-1)
#             print("R{0}<-->R{1}".format(i, counter-i))
#             counter-= 1

#     return (matriz,nums)



# num=matriz[0][0]
# matriz[0]=part_list(matriz[0],matriz[0][0])
# Mostrar(matriz)

# new_list=multiply_row(matriz[0], matriz[1][0]*-1)
# matriz[1]=add_lists(matriz[1],new_list)
# Mostrar(matriz)

# new_list2=multiply_row(matriz[0],matriz[2][0]*-1)
# matriz[2]=add_lists(matriz[2],new_list2)
# Mostrar(matriz)
# '---------------------------------------------------------'
# num2=matriz[1][1]
# matriz[1]=part_list(matriz[1], matriz[1][1])
# Mostrar(matriz)

# new_list3=multiply_row(matriz[1], matriz[2][1]*-1)
# matriz[2]=add_lists(matriz[2],new_list3)
# Mostrar(matriz)

# determinant=num*num2*matriz[0][0]*matriz[1][1]*matriz[2][2]
# determinant=str(Fraction(determinant).limit_denominator())
# Mostrar(matriz)


def staggered(i,matriz):
    # print(str(Fraction(matriz[i][i]).limit_denominator()))
    # num=matriz[i][i]
    # matriz[i]=part_list(matriz[i],matriz[i][i])
    # Mostrar(matriz)
    column=i+1
    
    while column<len(matriz):
       
        matriz=redux(i,column,matriz)
        column+=1
        #Mostrar(matriz)
    return (matriz)

def show_signs(signs):
    sign=1
    for i in signs:
        sign*=i
    return sign

def unique_0(matriz,row,column):
    for i in range(row,len(matriz)):
        if matriz[i][column]==0:
            unique=False
        else:
            unique=True
    return unique
            
            
            
def swap_rows(matriz,row):
    signs=[]
    for i in range(row,len(matriz)-1):
        counter = 1
        
        while matriz[i][row] == 0 and i+counter < len(matriz):
            if unique_0(matriz, i, row):
                matriz[i], matriz[len(matriz)-1] = matriz[len(matriz)-1], matriz[i]
                signs.append(-1)
                print("R{0}<-->R{1}".format(i+1, len(matriz)))
                
            elif matriz[i+counter][row]!=0:
                matriz[i], matriz[i+counter] = matriz[i+counter], matriz[i]
                signs.append(-1)
                print("R{0}<-->R{1}".format(i+1, i+counter+1))
                
                
            counter += 1
    print('primera imprecion')
    print(show_signs(signs))
    Mostrar(matriz)         
    
    
           

    return matriz,signs
def mean(matriz):
    signsk=[]
          
    for i in range(len(matriz)-1):
        if matriz[i][i]==0:
            matriz,signs=swap_rows(matriz,i)
            signsk+=signs
            # if show_signs(signs)==-1:
            #     print(-1)
            
        if matriz[i][i]!=0:
            compare=copy.deepcopy(matriz)
            matriz=staggered(i, matriz)
            # nums.append()
            
            
        if matriz!=compare:
            print('segunda imprecion')
            print(show_signs(signsk))
            Mostrar(matriz)
    det=determinant(matriz)*show_signs(signsk)

    string='det= '+str(show_signs(signsk))+' x '
    for i in range(len(matriz)):
        if i!=len(matriz)-1:
            string+=str(Fraction(matriz[i][i]).limit_denominator()) +' x '
        else:
            string+=str(Fraction(matriz[i][i]).limit_denominator())
    string+=' = '+ str(Fraction(det).limit_denominator())
    print(string)
    # position=len(matriz)-1
    # string='det= '+str(Fraction(matriz[position][position]).limit_denominator()) +' x '
    # for i in range(len(nums)):
    #     if i!=len(nums)-1:
    #         sign=' x '
    #     else:
    #         sign=''
    #     string+=str(Fraction(nums[i]).limit_denominator())+sign
    # string+=' = '+str(Fraction(det).limit_denominator())
    # print(string)
    


