import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')
#<>

#Crear un programa que pida 3 numero y determine cual es el mayor
x = int(input("Digite primer valor: "))
y = int(input("Digite segundo valor: "))
z = int(input("Digite tercer valor: "))

if x > y and x > z:
    print(f"el numero mayor es: {x}")
elif y > x and y > z:
    print(f"el numero mayor es: {y}")
elif z > x and z > y:
    print(f"el numero mayor es: {z}")
else: 
    print("No hay un solo numero mayor")