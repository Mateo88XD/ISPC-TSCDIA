def decorativo(func):
    def wrapper(*args,**kwargs):
        sin = kwargs['monto']
        con = func(*args,**kwargs)
        print(f"El monto de ${sin} pasa a valer ${con}")
    return wrapper




@decorativo
def factura(monto,IVA):
    if IVA == 0:
        IVA = 0.21
    else:
        IVA = IVA / 100
    
    return monto +  IVA * monto


monto = int(input("Ingrese le monto: "))
IVA = int(input("Ingrese el IVA a sumar: "))
factura(monto = monto, IVA = IVA)