def decorativo(func):
    def wrapper(*args):    
        binario,hexagecimal = func(*args)
        num = args[0]
        print(f"El número {num} en Binario es: {binario} y en Hexagecimal es: {hexagecimal}")

    return wrapper



@decorativo
def cambioDeSistema(num):
    binario = bin(num)[2:]
    hexadecimal = hex(num)[2:]
    return binario, hexadecimal

num = int(input("Ingrese un numero: "))
cambioDeSistema(num)


