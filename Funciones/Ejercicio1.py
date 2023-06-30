
# Costo mucho este :´´´´V

def decorador(func):
    def wrapper():
        tipo = func()
        print(f"El triángulo es un: {tipo}")
    return wrapper


@decorador
def equilatero():
    return "Equilatero"


@decorador
def isoceles():
    return "Isóceles"


@decorador
def escaleno():
    return "Escaleno"


lados = []
for i in range(3):
    lado = float(input(f"Ingrese el {i + 1}er lado: "))
    lados.append(lado)

if lados[0] == lados[1] == lados[2]:
    equilatero()
elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
    isoceles()
else:
    escaleno()
