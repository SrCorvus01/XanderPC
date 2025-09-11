import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Valor de la posicion 1: ",lista[1]) #Imprime el valor que almacena la posicion 1 de la lista

print("Lista A: ",lista[0:7]) #Imprime la lista desde la posicon 0 - 7 de la lista
print("___________________________________________________________________________________________________________\n") #Estetica


#Listas pueden almacenar diferentes tipos de valores en la misma
lista2 = ["Xander", "Jehova", 4, 420, ["Day","Dayanna","Dayarana"], True]
print("Lista B: ",lista2)
print("\nLista B desde poscion 3 hasta posicion 5:")
print(lista2[3:6])

print("\nImprimimos solo el valor de la posicion 4: ",lista2[4])
print("___________________________________________________________________________________________________________\n") #Estetica


#Agregamos un nuevo valor UNICAMENTE al final de la nueva lista
lista3 = ["Goku", "Vegeta"]
print("Agregaremos un valor a esta Nueva lista: ",lista3)
lista3.append("ZATANAS")
print("\nLa Nueva lista actualizada: ",lista3)
print("___________________________________________________________________________________________________________\n") #Estetica


#Ahora agregaremos un nuevo valor en la posicion que queramos:
lista3.insert(2,"NUMERO 3")  
#"2" es la posision en la que insertamos el nuevo valor

print("La nueva lista actualizada: ",lista3)

#Agregamos varios elementos de golpe en la nueva lista SOLO AL FINAL
lista3.extend([42.66,"Martes"])
print("\nAgregando varios elementos de golpe a la vez, la lista queda:", lista3)
print("___________________________________________________________________________________________________________\n") #Estetica

#Sumamos las listas, se encadenan ejemplo:
SumaListas = lista + lista2 + lista3
print(SumaListas)
print("___________________________________________________________________________________________________________\n") #Estetica

#Buscar Martes seria asi:
print(f"BUSCAR Martes: {"Martes" in SumaListas}")
#OBTENEMOS FALSE O TRUE

#Posicion de Martes:
print(f"POSICION Martes: {SumaListas.index("Martes")} ")

#Cuantas veces aparece Martes en la lista:
print(f"CANTIDAD de Martes [ {SumaListas.count("Martes")} ] veces en la lista")

print("___________________________________________________________________________________________________________\n") #Estetica

#Eliminar elementos usamos:
print(f"El elemento posicion 11 de la lista es: {SumaListas[11]}")
SumaListas.pop(11) #Hemos eliminado el elemento de la posicion 0 ("Day","Dayanna","Dayarana")
print("\nEliminando el elemento de la posicion 11 de la lista: ",SumaListas)

#Remover algun elemento en especifico
SumaListas.remove("Lunes")
print("\nEliminamos Lunes: ",SumaListas)

print("___________________________________________________________________________________________________________\n") #Estetica

#Eliminar toda la lista
SumaListas.clear()
print("ELiminar toda la lista:",SumaListas)

print("___________________________________________________________________________________________________________\n") #Estetica

#Multiplicamos los elementos de una lista:
ListaPanacho = ["Pan","Buñuelo",-2]*3  #Multiplicamos por la lista por 3
print("Lista Multiplicada",ListaPanacho)

print("___________________________________________________________________________________________________________\n") #Estetica

#Ordenar una lista 
listaNumeros = [1, 4, 2, -1, 0, 3]
print("Lista desordenada: ",listaNumeros)

listaNumeros.sort()
print("\nLista orden ascendente: ",listaNumeros)

listaNumeros.sort(reverse=True)
print("\nLista orden descendente: ",listaNumeros)


print("\nFIN\n")
