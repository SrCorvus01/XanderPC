import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

### Funciones puras e inmutabilidad
#en programacion funcional, la inmutabilidad quiere decir que los datos no cambian despues de ser creados
#en lugar de modificar estructuras de datos (listas, diccionarios, etc), se crean nuevas estructuras de datos con los cambios deseados

lista_nombres = ["Diego", "Diana", "Maria", "Pedro", "Juan"]
lista_nombres = lista_nombres + ["Camila"] # Vulnera la inmutabilidad
lista_nombres_nueva = lista_nombres + ["Mariana"] #Conserva la inmutabilidad - mejor practica

print(lista_nombres)
print(lista_nombres_nueva)



### Funciones puras
#siempre devuelve el mismo resultado para los mismos argumentos
#no produce efectos secundarios (no modifica variables externas, no imprime, no escribe en archivos, etc)
#contenedor de informacion

def cube(x):
    return x * x * x

print(f"El cubo de 3 es: {cube(3)}")

#Funcion pura: devuelve una copia del argumento con un nuevo elemento agregado
def CRUD_add(lista, nuevo_elemento):
    return lista + [nuevo_elemento] #no modifica la lista original, devuelve una nueva lista

print(f"Nueva lista: {CRUD_add(lista_nombres, 'Valentina')}")

#version no pura: modifica la lista original
def CRUD_add_no_pura(lista, nuevo_elemento):
    lista.append(nuevo_elemento) #modifica la lista original
    return lista

#funcion pura con diccionarios:
def CRUD_UPDATE_Diccionario(diccionario, clave, nuevo_valor):
    nuevo_diccionario = diccionario.copy() #copia el diccionario original
    nuevo_diccionario[clave] = nuevo_valor #modifica la copia
    return nuevo_diccionario #devuelve la copia modificada

diccionario = { "nombre": "Diego",
                "edad": 30,
                "estatura": 1.75,
                "peso": 70
                }

print(f"Nuevo diccionario: {CRUD_UPDATE_Diccionario(diccionario, 'edad', 31)}")
print(f"Diccionario original: {diccionario}")