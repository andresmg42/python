# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:03:30 2022

@author: andres
"""
from fractions import Fraction


import reduccion as nt
import copy


def determinant(matriz):
    mult=1
    for i in range(len(matriz)):
       mult*=matriz[i][i]
    return mult
       

def staggered(row,matriz):
    
    column=row+1
    string=''
    while column<len(matriz):
       
        
        num=matriz[column][row]*-1*(1/matriz[row][row])
        if num>0:
            sign='+'
            string+='R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign)+'\n'
        elif num<0:
            sign=''
            string+='R{2}--->R{2} {3} {1}R{0}'.format(row+1,str(Fraction(num).limit_denominator()),column+1,sign)+'\n'
        new_list=nt.multiply_row(matriz[row],num )
        matriz[column]=nt.add_lists(matriz[column],new_list)
        
        column+=1
    
    return matriz,string

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
    string=''
    for i in range(row,len(matriz)-1):
        counter = 1
        
        while matriz[i][row] == 0 and i+counter < len(matriz):
            if unique_0(matriz, i, row):
                matriz[i], matriz[len(matriz)-1] = matriz[len(matriz)-1], matriz[i]
                signs.append(-1)
                string+="R{0}<-->R{1}".format(i+1, len(matriz))+'\n'
                
            elif matriz[i+counter][row]!=0:
                matriz[i], matriz[i+counter] = matriz[i+counter], matriz[i]
                signs.append(-1)
                string+="R{0}<-->R{1}".format(i+1, i+counter+1)+'\n'
                
                
            counter += 1
    
    string+=str(show_signs(signs))+'\n'
    string+=nt.Mostrar(matriz)+'\n'         
    
    return matriz,signs,string

def mean(matriz):
    signsk=[]
    strings=''
          
    for i in range(len(matriz)-1):
        if matriz[i][i]==0:
            matriz,signs,text=swap_rows(matriz,i)
            strings+=text
            signsk+=signs
            
            
        if matriz[i][i]!=0:
            compare=copy.deepcopy(matriz)
            matriz,text1=staggered(i, matriz)
            strings+=text1
            
            
            
        if matriz!=compare:
            
            strings+=str(show_signs(signsk))+'\n'
            strings+=nt.Mostrar(matriz)+'\n'
    det=determinant(matriz)*show_signs(signsk)

    string='det= '+str(show_signs(signsk))+' x '
    for i in range(len(matriz)):
        if i!=len(matriz)-1:
            string+=str(Fraction(matriz[i][i]).limit_denominator()) +' x '
        else:
            string+=str(Fraction(matriz[i][i]).limit_denominator())
    string+=' = '+ str(Fraction(det).limit_denominator())
    strings+=string+'\n'
    
    return strings
    
    
