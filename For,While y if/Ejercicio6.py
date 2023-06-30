for i in range(2):
    letra = input(f"Ingrese la {i+1}ra letra: ")
    while len(letra) != 1:
        print("Error: ingrese un caracter")
        letra = input(f"Ingrese la {i+1}ra letra: ")
    if i == 0:
        letra1 = letra
    else:
        letra2 = letra
if letra1 == letra2:
    print("Las dos letras son iguales")
else:
    print("Las dos letras no son iguales")