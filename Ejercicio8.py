letra = input("Ingrese f/m para saber la mesa de votacion: ")
while letra.lower() != 'f' and letra.lower() != 'm':
    print("Error: Ingrese la letra 'f' o 'm' ")
    letra = input("Ingrese f/m para saber la mesa de votacion: ")
if letra.lower() == 'm':
    print("Votas en la mesa Masculina")
else:
    print("Votas en la mesa Femenina")