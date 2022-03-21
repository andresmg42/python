# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 09:11:34 2022

@author: Andres Ortega
"""

from fractions import Fraction

import numpy as np


def add_lists(list1, list2):
    new = []
    for i in range(len(list1)):
        numero = list1[i]+list2[i]
        new.append(numero)
    return new


def part_list(list1, num):
    if num != 0:
        new = []
        for i in list1:
            new_num = i/num
            new.append(new_num)
    else:
        new = list1
    return new


def multiply_row(row, num):
    new_row = []
    for i in range(len(row)):
        new_num = row[i]*num
        new_row.append(new_num)
    return new_row


def turn_fractions(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = str(Fraction(str(matriz[i][j])))
    return matriz


def Mostrar(matriz):
    print('the matrix is as follows :')
    a = np.array(matriz)

    s = [[str(Fraction(e).limit_denominator()) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print()


def swap_rows(matriz):

    for i in range(len(matriz)-1):
        counter = 1
        while matriz[i][i] == 0 and i+counter < len(matriz):
            matriz[i], matriz[i+counter] = matriz[i+counter], matriz[i]
            print("R{0}<-->R{1}".format(i, i+counter))
            counter += 1

    return matriz


def add_identity(matriz):
    new_list = [0]*len(matriz)
    for i in range(len(matriz)):
        matriz[i] = matriz[i]+new_list
    counter = 0
    for i in range(len(matriz)):
        matriz[i][counter+len(matriz)] = 1
        counter += 1
    return matriz


def create_matrix(n, m):
    matrix = []

    for i in range(n):
        matrix.append([0]*m)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            num = float(
                Fraction(input("type the number of row {0}, column {1} :".format(i+1, j+1))))
            matrix[i][j] = num
    return matrix


def redux(matriz, n):
    array = []
    a = []

    for i in range(n):
        a.append(i)
        array.append([i])
        for j in array:
            for z in a:
                if z not in j:
                    j.append(z)

    for i in range(n):

        if matriz[array[i][0]][i] == 0:
            matriz = swap_rows(matriz)

            Mostrar(matriz)
            print()

        if matriz[array[i][0]][i] != 1:
            print("R{0}-->{1}R{0}".format(i+1, str(1 /
                  Fraction(matriz[array[i][0]][i]).limit_denominator())))
            list0 = part_list(matriz[i], matriz[array[i][0]][i])
            matriz[i] = list0

            Mostrar(matriz)

        j = 1
        while j < n:
            if Fraction(matriz[array[i][j]][i]*-1) > 0:
                sign = "+"
                print("R{2}-->R{2}{3}{1}R{0}".format(i+1, str(
                    Fraction(matriz[array[i][j]][i]*-1).limit_denominator()), array[i][j]+1, sign))
            elif Fraction(matriz[array[i][j]][i]*-1) < 0:
                sign = ""
                print("R{2}-->R{2}{3}{1}R{0}".format(i+1, str(
                    Fraction(matriz[array[i][j]][i]*-1).limit_denominator()), array[i][j]+1, sign))

            new_list2 = multiply_row(matriz[i], matriz[array[i][j]][i]*-1)
            matriz[array[i][j]] = add_lists(new_list2, matriz[array[i][j]])

            j += 1
        Mostrar(matriz)

        print("------------------------------------------------------------------")
        print()
