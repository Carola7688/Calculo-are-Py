# Vamos a calcular del area de un circulo, segun el radio ingresado por el usuario

import math


Radio = float(input("Ingrese el radio de la circunferencia: "))

Area = math.pi * (Radio**2)

print("El area de la circunferencia de radio", Radio, "es: ", Area)