
# Vamos a calcular del area de un circulo, segun el radio ingresado por el usuario

import math

#Paso 1: Solicitar al usuario que ingrese el radio del circulo
Radio = float(input("Ingrese el radio de la circunferencia: "))

# Paso 2: Calcular el área del circulo utilizando la fórmula: área = π * radio^2
Area = math.pi * (Radio**2)

# Paso 3: Mostrar al usuario el área calculada
print("El area de la circunferencia de radio", Radio, "es: ", Area)