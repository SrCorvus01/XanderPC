import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Pedimos los valores de cada variable 
a = float(input("Digite valor de A: "))
b = float(input("Digite valor de B: "))
c = float(input("Digite valor de C: "))

#imprimimos Resultado
resultado = (a**3 * (b**2 - 2*a*c)  /  2*b )
print(f"el resultado es: {resultado}") 