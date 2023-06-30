# Es un programa que codifica
def decorativa(func):
    def wrapper(*args):
        texto = str(*args)
        codificado = func(*args)

        print(f"Este es el texto sin codificar: {texto}")
        print(f"Este es la codificación: {codificado}")

    return wrapper

@decorativa
def codificador(texto):
    nuevo_texto = ""
    for letra in texto:
        if letra.lower() == 'a':
            nuevo_texto += '@'
        elif letra.lower() == 'e':
            nuevo_texto += '#'
        elif letra.lower() == 'i':
            nuevo_texto += '$'
        elif letra.lower() == 'o':
            nuevo_texto += '%'
        elif letra.lower() == 'u':
            nuevo_texto += '*'
        else:
            nuevo_texto += letra
    return nuevo_texto

texto = input("Ingrese el texto a codificar: ")
codificador(texto)

