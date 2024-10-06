
clientes = [{"nombre": "santiago","id": 123, "dinero": 0}, 
            {"nombre": "ramiro",  "id": 456, "dinero": 0}]



total = int(input("Ingrese el monto: "))
for i in clientes:
    if 123 == i["id"]:
        ingreso = i
        dinero = ingreso["dinero"]
        suma = dinero + total
        i["dinero"] = suma
        print(i)
    if not i:
        print("no entré")

#ingreso = clientes[0]
#dinero = ingreso["dinero"]
#print(dinero)

