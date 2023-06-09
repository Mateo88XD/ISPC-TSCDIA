#El precio del Dolar es de $500 pesos

print("Que cambio quiere hacer?")
print("1_ Dolar --> Pesos")
print("2_ Pesos --> Dolar")
x = int(input("Ingrese el numero de la opcion requerida: "))
if x == 1:
    cantidad = float(input("Ingrese la cantidad de dolares: "))
    print(f"${(cantidad * 500):.2f} pesos")
elif x ==2:
    cantidad = float(input("Ingrese la cantidad de pesos: "))
    print(f"${(cantidad / 500):.2f} dolares")
else:
    print("Error: la opcion colocada no existe")