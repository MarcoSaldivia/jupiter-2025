# APUNTES PARA JUPITER

#modularidad = hacer bloques independientes
#retilizacion = se puede compiar y pegar
#encapsulamiento = se oculta al usuario 


# Creando una funcion (Ejemplos sencillos)
# 1.
def funcion(x):
	return x + 10

y = funcion(5)
print(f"El resultado de la funcion es {y}")

# 2.
def saludo(nombre):
	print(f"Hola, mi nombre es + {nombre}")

saludo("Tomas")
#Saludo: La llamada a la funcion, imprime "Hola, mi nombre es Tomas


# Argumentos posicionales

def suma(a, b):
    return a + b 

# La llamada a la funcion con argumentos posicionales
resultado = suma(2, 3) # Orden si importa, a = 2 - b = 3
print(resultado)
# En este ejemplo los argumetos a y b son argumentos posicionales



#### Ir a google drive e instalar la extension Colaboratory
# Instalar en VSCODE: Todas las extensiones de Jupyter(certificadas por microsoft)

# Librerias: Numpy (),Pandas (Dataframes y Series)
# Matplotlib

# Pandas = Preparacion y filtrado de datos, Lectura de Archivos, Data Science Machine Learning
#          Carga, Modelar, Analizar, Manipular y    Datos



lista = list(range(1, 11))
print(lista) # Se llama solo a la lista 

lista = list(range(1, 11))
lista # Se llama solo a la lista 


# Dimensiones
# 2 dimenciones = Matrices (2D)
# 3 dimenciones = Tensores (3D) (Series de tiempo)
# 4 dimenciones = Tensores (4D) (Videos)

# Funciones Numpy
# argmax() - argmin()
# median()
# mean()
# var() 
# percentile() 
# sqrt() 
# std() 

#FUNCIONES
#-Argumentos Posicionales 
#-Argumentos Con Valor por Defecto
#-Argumentos por nombres (Keywords)

#Recursividad 
# Función se llama a sí misma para resolver un problema dividiéndola lo subdivisiónes.
# características clave:
# Caso base: Condición que detiene las llamadas recursivas (evita un ciclo infinito).
# Caso recursivo: La función se invoca a sí misma con un problema más pequeño.

#¿Por qué es útil?
# Simplifica problemas complejos que tienen una estructura repetitiva o anidada (como cálculos matemáticos o recorridos de estructuras).
#  Es especialmente útil para algoritmos como Fibonacci y Factorial,


#Ejemplo:
# Imagina que tienes una muñeca rusa (matryoshka):
""""Caso base: La muñeca más pequeña (no se puede abrir).
Caso recursivo: Abres una muñeca, y dentro hay otra igual pero más pequeña."""
# Así funciona la recursión: se descompone un problema hasta llegar a una versión del caso base.


###   factorial_recursivo()
#	RecursionError


#  Serie de Fibonacci
#  Otro ejemplo de recursividad
#  Cada número es la suma de los 2 números anteriores


##Bibliotecas
##Fundaciones de random





#Data sets
#  Series: la suma de 2 series
#  Dataframes: la suma de varias series

#  Series: estructuras unidimensionales de pandas(no es un arreglo)
#  Dataframes: estructura de datos bidimensionales

#  Dataframes: Tiene fila y columnas. Si es una matriz. Estructura de datos tabulares y etiquetados.
#  Datasets: No necesariamente puede contener información organizada. No es necesariamente una matriz. Abarca cualquier tipo de dato organizado.

# Funciones principales Pandas
""""head() Muestra las primeras filas
Info()
Describe()
Loc()
Query()
Drop()
Grouph()
Tail()
Unique()
Dropna()
Fillna()
Iloc()
Concat()
Merge()
Join()"""




#  Archivos JSON
#  Permite formatear o preformatear datos

