for i in range(2):
    palabra = input(f"Ingrese la {i + 1}ra palabra: ")
if i == 0:
    p1 = palabra
else:
    p2 = palabra

if p1 == p2:
    print("Las dos palabras son iguales")
else:
    print("Las dos palabras no son iguales")