"""Escribe un programa que pregunte sobre 
el precio de tres productos e indique cuál 
es el producto más barato para comprar."""

precio_1= float(input("introduce el precio del primer producto:"))
precio_2= float(input("introduce el precio del segundo producto:"))
precio_3= float(input("introduce el precio del tercero producto:"))
if precio_1 < precio_2 and precio_1 <precio_3:
    print(f"El precio más barato es el del primer producto: {precio_1}")
elif precio_2 < precio_1 and precio_2 < precio_3:
        print(f"el precio más barato del segundo producto es: {precio_2}")
else:
        print(f"el precio más barato del tercer producto es: {precio_3}")



