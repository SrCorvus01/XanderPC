import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Hacer un programa que simule un cajero automatico con un saldo 
#inicial de 1000 y tendra el siguiente menu de opciones:

saldo = 1000
print("____BANCOLOMBIA____")
print("1.Ingresar dinero\n2.Retirar dinero\n3.Mostrar dinero\n4.Salir")

opcion = int(input("\nDeseas: "))


if opcion == 1:
    ingresar = float(input(("¿Cuanto dinero desea ingresar?")))
    if ingresar > 0:
        saldo =+ ingresar
        print(f"has ingresado {ingresar:.3f} correctamente")
    else: exit

elif opcion == 2:
    retirar = float(input(("¿Cuanto dinero desea Retirar?")))
    if retirar <= saldo:
        saldo =+ retirar
        print(f"has retirado {retirar:.3f} coprrectamente")
    saldo =+ retirar

elif opcion == 3:
    print(f"Tu nuevo saldo es de: {saldo:.3f}")

elif opcion == 4:
    print("Saliendo del cajero automatico, por favor espere")
    


#FALTA COMPLETAR CODIGO CON UN BUCLE