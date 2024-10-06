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
#----------------------------------------------------------------------------------

from random import *
import os

cliente = []
corriente = []
ahorro = []

personas = {"nombre": None,
            "apellido": None,
            "id": None,
            "telefono": None}

cuentaCorriente = {"numero": None,
                   "saldo": None,
                   "tipo": None,
                   "idCliente": None,
                   "limiteSobregiro": 100000000,
                   "saldoMinimo": 1000000}

cuentaAhorro = {"numero": None,
                "saldo": None,
                "tipo": None,
                "idCliente": None,
                "saldoMinimo": 50000}

#Funcion para guardar el nombre, apellido, id, telefono de un cliente en un diccionario
def abrirCuenta():
    consola1 = input("ingrese su nombre: ")
    consola2 = input("ingrese su apellido: ")
    consola3 = int(input("ingrese su id: "))
    consola4 = int(input("Ingrese su telefono: "))
    personas["nombre"] = consola1
    personas["apellido"] = consola2
    personas["id"] = consola3
    personas["telefono"] = consola4
    cliente.append(personas)
    menu()

#Funcion para definir Cuenta Corriente
def abrirCorriente():
    consola1 = int(input("Ingrese su Dinero: "))
    consola2 = int(input("Ingrese su Identificacion: "))
    cuentaCorriente["numero"] = randint(100, 10000)
    cuentaCorriente["saldo"] = consola1
    cuentaCorriente["idCliente"] = consola2
    corriente.append(cuentaCorriente)
    os.system("cls")
    menu()

#Funcion para definir cuenta Ahorros
def abrirAhorros():
    consola1 = int(input("Ingrese su Dinero: "))
    consola2 = int(input("Ingrese su Identificacion: "))
    cuentaAhorro["numero"] = randint(10001, 100000)
    cuentaAhorro["saldo"] = consola1
    cuentaAhorro["idCliente"] = consola2
    ahorro.append(cuentaAhorro)
    menu()

#funcion para seleccionar la cuenta a depositar
def seleccionarDeposito():
    print("========================")
    print("  SELECCIONE SU CUENTA  ")
    print("1. Cuenta Corriente \n"
          "2. Cuenta Ahorros \n")
    consola = int(input("Ingrese el numero de la opcion: "))

    if consola == 1:
        abrirCorriente()
    elif consola == 2:
        abrirAhorros()
    else:
        print("Opcion erronea, Intente nuevamente")
    os.system("cls")
    menu()

#buscar cliente
def buscar():
    consola = input(int("Ingrese el Identificador"))
    for buscador in cliente:
        if consola == buscador["id"]:
            print(buscador)
    if not buscador:
            print("Cliente NO Registrado")
    os.system("cls")
    menu() 

#====================================================================
def menu():
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
        opcion = int(input("Ingrese la opcion: "))
        os.system("cls")

        if opcion == 1:
            abrirCuenta()
        elif opcion == 2:
            depositar()
        elif opcion == 7:
            buscar()

print(menu())       
#======================================================================