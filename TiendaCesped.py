## Haz un programa para una tienda que vende césped para jardines. 
# Esta tienda trabaja con jardines circulares y el precio del metro 
# cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular 
# y devuelve el valor en reales de cuánto tendrá que pagar.
radioMetros= float(input("¿Cúal es el radio de su cesped?"))
area = 3.14*(radioMetros**2)
PrecioFinal = area*25
print(f"El precio final es de R${PrecioFinal}")