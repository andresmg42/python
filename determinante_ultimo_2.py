# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:03:30 2022

@author: andres
"""
from fractions import Fraction

import numpy as np
import copy

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
    string='the matrix is as follows :\n'
    a = np.array(matriz)

    s = [[str(Fraction(e).limit_denominator()) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    string+='\n'.join(table)+'\n'
    return string
    
def redux(row,column,matriz):
    string=''
    num=matriz[column][row]*-1*(1/matriz[row][row])
    if num>0:
        sign='+'
        string+='R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign)+'\n'
    elif num<0:
        sign=''
        string+='R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign)+'\n'
    
    
    
    new_list=multiply_row(matriz[row],num )
    matriz[column]=add_lists(matriz[column],new_list)
    return matriz

def determinant(matriz):
    mult=1
    for i in range(len(matriz)):
       mult*=matriz[i][i]
    return mult
       

def staggered(i,matriz):
    
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
    
    print(show_signs(signs))
    Mostrar(matriz)         
    
    
           

    return matriz,signs
def mean(matriz):
    signsk=[]
          
    for i in range(len(matriz)-1):
        if matriz[i][i]==0:
            matriz,signs=swap_rows(matriz,i)
            signsk+=signs
            
            
        if matriz[i][i]!=0:
            compare=copy.deepcopy(matriz)
            matriz=staggered(i, matriz)
            
            
            
        if matriz!=compare:
            
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
    
    


