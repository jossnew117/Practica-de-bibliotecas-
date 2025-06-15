"""las bibliotecas son colecciones de funciones y variables que podemos importar en nuestros programas
 para reutilizar código y evitar la repetición. 
En Python, las bibliotecas pueden ser módulos individuales o paquetes que contienen varios módulos."""
Joseth_datos = {
    "nombre": "Joseth",
    "edad": 24,
    "lenguajes": ["Python", "JavaScript", "C++"],
    "intereses": ["programación", "música", "videojuegos"]
}
print (Joseth_datos)
print ("intereses",Joseth_datos["intereses"])
"""agregar un nuevo elemento a la lista de intereses"""
Joseth_datos["comida favorita"] = "pizza"
print ("comida favorita",Joseth_datos["comida favorita"])
"""función len() sirve para contar el número de elementos en una lista o diccionario"""
print (len(Joseth_datos))
"""el pop() elimina un elemento de la lista o diccionario y lo devuelve"""
Joseth_datos.pop("edad")
print (Joseth_datos)
"""la funcion items() devuelve una lista de tuplas con los elementos del diccionario""" 
print (Joseth_datos.items())
"""la función keys() devuelve una lista con las claves del diccionario"""   
print (Joseth_datos.keys())
"""la función values() devuelve una lista con los valores del diccionario"""    
print (Joseth_datos.values())
""" lectura de lazo for para iterar"""
for llave in Joseth_datos.keys():
    print ("llave:", llave)

for llave, valor in Joseth_datos.items():
    print ( llave, "-->", valor)