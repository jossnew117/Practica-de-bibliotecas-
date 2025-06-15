import math

numeros = [2, 8, 15, 23, 91, 112, 256]

for numero in numeros:
    raizNumeros = math.sqrt(numero)
    if raizNumeros.is_integer():
        print(f"La raíz cuadrada de {numero} es {int(raizNumeros)} (entero).")
