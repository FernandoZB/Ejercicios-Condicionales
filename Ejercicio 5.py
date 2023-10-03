# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:09:03 2023

@author: fzapber
"""

dia_semana = input("Ingresa un día de la semana en minúsculas: ")

if (dia_semana == "lunes"):
    print("Es lunes.")
elif (dia_semana == "viernes"):
    print("Es viernes.")
elif (dia_semana == "sábado" or dia_semana == "domingo"):
    print("Es fin de semana.")
else:
    print("No es lunes, viernes, sábado o domingo.")
