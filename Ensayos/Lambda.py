import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Sumar dos numeros
#Forma normal
def sumar(n1,n2):
    return n1 + n2

print("Funcion Normal: ",sumar(20,2))

#Formal Lambda
sumaremos = lambda x,y: x + y
print("Usando Lambda: ",sumaremos(20,4))