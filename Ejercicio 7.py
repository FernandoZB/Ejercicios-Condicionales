# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:50:21 2023

@author: fzapber
"""

edad = int(input("Ingresa tu edad: "))
ingresos = int(input("Ingresa tus ingresos mensuales en €: "))

if (edad > 16 and ingresos >= 1000):
    print("Debes tributar.")
else:
    print("No debes tributar.")
