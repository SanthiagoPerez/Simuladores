

personas = {"nombre": None,
            "id": None}
clientes = [{"nombre": "santiago","id": 123, "dinero": 0}, 
            {"nombre": "ramiro",  "id": 456, "dinero": 0}]

def depositar():
    consola1 = int(input("Ingrese su Identificacion: "))
    consola2 = int(input("Ingrese la cantida a despositar: "))
    for buscador in clientes:
        if consola1 == buscador["id"]:
            acceder = clientes[buscador]
            dinero = acceder["dinero"]
            print(buscador)
    if not buscador:
            print("no llego")
depositar()

