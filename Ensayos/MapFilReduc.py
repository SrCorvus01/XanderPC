import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#MAP / FILTER / REDUCE


### MAP ###

#Elevar una lista de 20 numeros al cuadrado usando MAP 
#Creamos la lista
lista1 = list(range(1,21)) #Utilizamos range para establecer la longitud de la lista
print("Lista Normal:", lista1)  #Imprimimos la lista para observarla

#Definimos funcion de elevar al cuadrado
elevarCuadrado = lambda x: pow(x, 2)  #pow(x, 2) = x * x

#Si no colocamos list, entonces me dara las coordenadas del map (no me sirve)
listaElevada = list(map(elevarCuadrado, lista1))
print("\nLista Elevada:",listaElevada)



### FILTER ###
listaPar = list(filter(lambda num: num % 2 == 0, lista1 ))

#Imprimimos el filtro de la lista de numeros pares
print("\nLista Filtrada:",listaPar)



### REDUCE ###
import functools

letras = ["H", "O", "L", "A"]
palabra = functools.reduce(lambda x, y: x + y, letras)
print("\nMetodo Reduce en cadenas: ",palabra)

#Calculemos el factorial de 5
factorial = [5, 4, 3, 2, 1]
resultado = functools.reduce(lambda x, y: x * y, factorial)
print("Calculando factorial: ", resultado)

