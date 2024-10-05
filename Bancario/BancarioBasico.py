""""
Descripción General
Vas a desarrollar un simulador bancario en el que los usuarios pueden abrir cuentas, realizar depósitos, 
retiros, transferencias y consultar sus saldos. Este simulador será escrito sin clases, por lo que se basará 
en funciones y estructuras de datos como listas o diccionarios para almacenar la información de los clientes, cuentas y transacciones.

Requisitos del Simulador Bancario
1. Estructuras de Datos:
Usarás diccionarios y listas para manejar la información.

Clientes: Cada cliente será representado por un diccionario que contenga su nombre, apellido, número de identificación y teléfono.

Cuentas: Cada cuenta será un diccionario que almacena el número de cuenta, el saldo, el tipo de cuenta 
(ahorro o corriente), el ID del cliente al que pertenece, y otros datos relevantes como el límite de sobregiro 
o el saldo mínimo (según el tipo de cuenta).

Transacciones: Las transacciones se almacenarán en una lista, donde cada transacción será un diccionario 
que contenga el tipo de transacción (depósito, retiro, transferencia), el monto, la fecha y la cuenta involucrada.

2. Funcionalidades:
Abrir cuenta: Los usuarios podrán abrir una cuenta de ahorro o corriente.
Depositar dinero: Los usuarios podrán realizar depósitos en una cuenta.
Retirar dinero: Los usuarios podrán realizar retiros si tienen suficiente saldo (o dentro del límite de sobregiro en cuentas corrientes).
Transferencias: Los usuarios podrán transferir dinero entre cuentas del mismo banco.
Consultar saldo: Los usuarios podrán consultar el saldo de su cuenta.
Historial de transacciones: Los usuarios podrán ver el historial de transacciones de una cuenta específica.
Salir: Cerrar el programa guardando los datos.

3. Validaciones y Restricciones:
No se permitirá retirar más dinero del que se tiene en la cuenta de ahorro.
Las cuentas corrientes tendrán un límite de sobregiro.
Las cuentas de ahorro deben tener un saldo mínimo para recibir intereses (no es necesario aplicar interés en esta versión, pero se puede guardar el dato).
Se debe asegurar que los montos ingresados en las transacciones sean positivos.

4. Gestión de Datos:
Guardar y cargar los datos (clientes, cuentas, y transacciones) en un archivo de texto o CSV para que la información persista entre sesiones.
"""

while True:
    print("=================================")
    print("        Bienvenido al Banco      ")
    print("=================================")
    print()
    print("--- SELECCIONE UNA OPCION --- \n"
        "1. Abrir Cuenta \n"
        "2. Depositar Dinero \n"
        "3. Retirar Dinero \n"
        "4. Transfesir Dinero entre Cuentas \n"
        "5. Consultar Saldo \n"
        "6. Ver Historial de Transacciones \n"
        "7. Buscar Cliente \n"
        "8. Salir \n")
    opcion = int(input())

    if opcion == 7:
        break

#Funcion para guardar el nombre, apellido, id, telefono de un cliente en un diccionario
def abrirCuenta():
    abrirCuenta = {}
    while True:
        nombreConsola = input("Ingrese su Nombre: ")
        abrirCuenta[nombre] = nombreConsola 

