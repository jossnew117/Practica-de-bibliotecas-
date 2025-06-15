"""Python nos ayuda a importar bibliotecas de manera sencilla,
con la palabra clave import, seguida del nombre de la biblioteca o módulo que queremos importar."""

"""Para instalar o actualizar una biblitoteca, usamos el gestor de paquetes pip en la terminal. https://pypi.org/"""
# Luego debemos importar la biblioteca con import (nombre_biblioteca)
import matplotlib
import matplotlib.pyplot as plot
estudiantes = ["Joseth", "Juan", "Maria", "Pedro"]
notas = [7.6, 9, 7, 9.2]
"""matplotlib es una biblioteca de Python para crear gráficos y visualizaciones de datos.
   matplotlib.pyplot es un módulo de matplotlib que proporciona una interfaz similar a MATLAB para crear gráficos."""
#plot.bar() es una función de matplotlib.pyplot que crea un gráfico de barras.
plot.bar(estudiantes, notas)
plot.show()  # muestra el gráfico

estudiantes_2 = ["Joseth", "Juan", "Maria", "Pedro","Esthela"]
# para seleccionar un elemento aleatorio de una lista, podemos usar la función choice() del módulo random.
import random
from random import choice
estudiantes_2 = choice(estudiantes_2)