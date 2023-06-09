for i in range(3):
    lado = float(input(f"Ingrese el {i + 1}ro lado: "))
    if i == 0:
        l1 = lado
    elif i == 1:
        l2 = lado
    else:
        l3 = lado

if l1 == l2 and l2 == l3:
    print("Es un triangulo Equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Es un triangulo Isósceles")
else:
    print("Es un triangulo Escaleno")