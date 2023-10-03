# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:06:58 2023

@author: fzapber
"""

val1 = int(input('Primer numero: '))
val2 = int(input('Segundo numero: '))
val3 = int(input('Tercer numero: '))

if (val1 > val2 and val1 > val3):
    print("El valor mas grande es", val1)
elif (val2 > val1 and val2 > val3):
    print("El valor mas grande es", val2)
else:
    print("El valor mas grande es", val3)