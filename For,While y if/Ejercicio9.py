for i in range(2):
    x = int(input(f"Ingrese el {i + 1}ro numero: "))
    if i == 0:
        n1 = x
    else:
        n2 = x
if n1 > n2:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")