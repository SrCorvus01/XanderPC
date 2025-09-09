import os
#Limpiamos terminal para que sea mas legible 
os.system('cls' if os.name == 'nt' else 'clear')

#Tienda hace 15% de descuento
precio = float(input("¿Cuanto costo todo el pedido? "))
descuento = precio * 0.15
precioTotal = precio - descuento

print(f"Aplicando el descuento del 15%, debes pagar: {precioTotal:.3f}")