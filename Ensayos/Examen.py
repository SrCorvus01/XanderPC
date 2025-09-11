import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')


### Usa map() y lambda para devolver una nueva lista que contenga el cuadrado de cada número.
numeros = [1, 2, 3, 4, 5]
cuadrado = lambda x: pow(x, 2)
print(list(map(cuadrado, numeros)),"\n")



### Usa filter() y lambda para quedarte solo con las palabras que empiecen con la letra "a".
palabras = ["auto", "avión", "barco", "bici", "acordeón"]
letraA = list(filter(lambda A: A.startswith("a"), palabras))
print(letraA,"\n")



### Usa reduce() y lambda para obtener el producto total de todos los números en la lista.
import functools
valores = [1, 2, 3, 4]
producto_Total = functools.reduce(lambda s, g: s * g, valores )
print(producto_Total, "\n")



### Escribe una función llamada aplicar_funcion que reciba una función y una lista, y devuelva una nueva lista con la función aplicada a cada elemento.
# Ejemplo esperado:
def doble(x):
    return x * 2

def aplicar_funcion(funcion, lista):
    return list(map(funcion, lista))

resultado = aplicar_funcion(doble, [1, 2, 3])
print(resultado,"\n")  # [2, 4, 6]



### Escribe una función que reciba una función y una lista, y devuelva una nueva lista con la función aplicada a cada elemento. 
def cuadruple(x):
    return pow(x, 4)

def aplicandoCuadruple(funcion, lista):
    return list(map(funcion, lista))

resultado2 = aplicandoCuadruple(cuadruple, [2,4,8,12,16]) 
print(resultado2)


#Usando filter, map y reduce, encadena funciones para:
#Filtrar los números pares.
#Elevarlos al cuadrado.
#Sumar todos los resultados.

lista = [1, 2, 3, 4, 5, 6]
print("\nLista original: ", lista)
numeroFiltrados = list(filter(lambda x: x % 2 == 0, lista))

print("Lista filtrada Pares: ", numeroFiltrados)

numerosElevados = list(map(lambda x: pow(x, 2), numeroFiltrados))
print("Lista elevada(2): ", numerosElevados)

sumaTotal = functools.reduce(lambda x,y: x + y, numerosElevados)
print("Lista Sumada: ", sumaTotal) 