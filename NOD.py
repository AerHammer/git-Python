#coding:utf-8
'''
Это модуль в котором расчитывается наибольший обший делитель 2 чисел
'''
def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)

