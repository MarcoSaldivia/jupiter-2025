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
