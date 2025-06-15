#estructura: for elemento in conjunto.
#en combniación con range() para iterar un número determinado de veces
for notas in range (1,4):
##el primer numero lo incluye y el segundo no
 nota_1= float(input("introduce la nota 1: "))
 nota_2= float(input("introduce la nota 2: "))
 print(f"el promedio de las notas es {(nota_1 + nota_2)/2}")
#en este caso el for itera 3 veces, y en cada iteración pide dos notas y calcula el promedio