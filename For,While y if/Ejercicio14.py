for i in range(3):
    x = int(input(f"Ingrese el {i + 1}ro número: "))
    if i == 0:
        n1 = x
    elif i == 1:
        n2 = x
    else:
        n3 = x

if n1 > n2:
    if n1 > n3:
        mayor = n1
    else:
        mayor = n3
else:
    if n2 > n3:
        mayor = n2
    else:
        mayor = n3

if mayor % 2 == 0:
    print(f"{mayor} Es el numero mas grande y es par")
else:
    print(f"{mayor} Es el numero mas grande y es impar")