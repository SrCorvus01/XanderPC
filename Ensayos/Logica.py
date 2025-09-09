import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Pedimos los valores de cada variable 
a = float(input("Digite valor de A: "))
b = float(input("Digite valor de B: "))

#Realizamos la operacion y usamos logica para saber si el resultado es true o false
#<>
resultado = ((3+5*8)<3) and (( (-6/3) * 4  + 2<2 )) or (a>b)

print(resultado)
