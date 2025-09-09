import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Los valores fijos: 
a = 10
b = 5
print(f"Valor inicial de A y B es: {a} y {b}\n")
#Forma clasica de intercambio de variables:
c = a
a = b
b = c
print(f"(FORMA CLASICA) El nuevo valor de A y B es: {a} y {b}\n")
      
#Tambien se puede:
a , b = b , a
print(f"El nuevo valor de A y B es: {a} y {b}\n")