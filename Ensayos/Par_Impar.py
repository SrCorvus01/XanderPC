import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Pedir dos numeros al usuario y determinar si son pares o impares
x = int(input("Digite un numero: "))
y = int(input("Digite un numero: "))
if x%2 == 0 and y%2 == 0:
    print("Ambos son numeros pares\n")
elif x%2 == 0 and y%2 != 0:
    print(f"El numero {x} es par y {y} es impar\n")
elif x%2 != 0 and y%2 == 0:
    print(f"El numero {x} es impar y {y} es par\n")
elif x%2 != 0 and y%2 != 0:
    print("Ambos numeros son impares")