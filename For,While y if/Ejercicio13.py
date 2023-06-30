importe = float(input("Ingrese el monto: "))

print("     ///MENU///    ")
print("1_ Pagar en Contado (-10%)")
print("2_ Pagar con Tarjta (+10%)")
print("3_ Pagar con Debito (-5%)")

opc = int(input("Ingrese la opcion deseada: "))
if opc == 1:
    print(f"El monto a pagar en contado es de {(importe * 0.9):.2f}")
elif opc == 2:
    print(f"El monto a pagar con tarjeta es de {(importe *  1.10):.2f}")
elif opc == 3:
    print(f"El monto a pagar con debito es de {(importe * 0.95):.2f}")
else:
    print("La opcion elegida no existe")