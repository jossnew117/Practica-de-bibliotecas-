"""Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo.
 El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, 
 si es equilátero, isósceles o escaleno."""
lado_1 = float(input("introduce el lado 1 del triangulo: "))
lado_2 = float(input("introduce el lado 2 del triangulo: ")) 
lado_3 = float(input("introduce el lado 3 del triangulo: "))       
if lado_1 + lado_2> lado_3 or lado_1+lado_3> lado_2 or lado_2+lado_3> lado_1 or lado_2+lado_1> lado_3 or lado_3+lado_1> lado_2 or lado_3+lado_2> lado_1:
    print ("los lados introducidos pueden formar un triangulo")
    if lado_1 == lado_2 and lado_1 == lado_3:
        print("el triangulo es equilatero")
    elif lado_1 == lado_2 or lado_1== lado_3 or lado_2 == lado_3:
        print("el triangulo es isosceles")
    elif lado_1 != lado_2 and lado_1!= lado_3 and lado_2 !=lado_3:
        print("el triangulo es escaleno")  
    