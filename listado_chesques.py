import sys

nombrDelArchivo = sys.argv[1]
""" dni=sys.argv[2]
salida=sys.argv[3]
tipoDeCheque=sys.argv[4]
estadoDelCheque=sys.argv[5]
rangoFecha=sys.argv[6]  """
num = 0

NroDeChequesDic = {}
CodigoBanco = {}
CodigoScurusal = {}
NumeroCuentaOrigen = {}
NumeroCuentaDestino = {}
Valor = {}
FechaOrigen = {}
FechaPago = {}
dni = {}
Estado = {}

cheques = open(nombrDelArchivo, "r")
next(cheques, None)

for cheque in cheques:
    num += 1
    cheque = cheque.rstrip("\n")
    chequeSeparado = cheque.split(";")
    NroDeChequesDic[str(num)] = chequeSeparado[0]
    CodigoBanco[str(num)] = chequeSeparado[1]
    CodigoScurusal[str(num)] = chequeSeparado[2]
    NumeroCuentaOrigen[str(num)] = chequeSeparado[3]
    NumeroCuentaDestino[str(num)] = chequeSeparado[4]
    Valor[str(num)] = chequeSeparado[5]
    FechaOrigen[str(num)] = chequeSeparado[6]
    FechaPago[str(num)] = chequeSeparado[7]
    dni[str(num)] = chequeSeparado[8]
    Estado[str(num)] = chequeSeparado[9]


# cheques.close()

# print (NroDeChequesDic)
# print(CodigoBanco)
# print(CodigoScurusal)
# print(NumeroCuentaOrigen)
# print(NumeroCuentaDestino)
# print(Valor)
# print(FechaOrigen)
# print(FechaPago)
# print(dni)
# print(Estado)

# f = open("test_file.csv", "a")
# print("nombre")
# tup1 = input(str)
# print("edad")
# tup2 = input(int)
# writer = csv.writer(f)
# writer.writerow(tup1)
# writer.writerow(tup2)
# f.close()

# with open("cuentas.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=";")

#     with open("puntajes.csv", "w") as new_file:

#         fieldnames = ["NroCheque", "CodigoBanco", "CodigoScurusal", "NumeroCuentaOrigen",
#                       "NumeroCuentaDestino", "Valor", "FechaOrigen", "FechaPago", "DNI", "Estado"]
#         csv_writer = csv.DictWriter(
#             new_file, fieldnames=fieldnames, delimiter=";")
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)

with open("Cuentasinput.csv", "a+") as new_file:
    myFile = csv.writer(new_file, delimiter=";")
    myFile.writerow(["NroCheque", "CodigoBanco",
                    "CodigoScursal", "NumeroCuentaOrigen", "NumeroCuentaDestino", "Valor", "FechaOrigen", "FechaPago", "DNI", "Estado"])
    NroCheque = input("por favor ingrese su numero de cheque: ")
    CodigoBanco = input("por favor ingrese su codigo de banco: ")
    CodigoSucursal = input("por favor ingrese su codigo de sucursal: ")
    NumeroCuentaOrigen = input("por favor ingrese su numero de Cuenta: ")
    NumeroCuentaDestino = input(
        "por favor ingrese el numero de la cuenta receptora: ")
    Valor = input("por favor ingrese el valor del cheque: ")
    FechaOrigen = input("por favor ingrese La fecha de origen: ")
    FechaPago = input("por favor ingrese La fecha de pago: ")
    dni = input("por favor ingrese su DNI: ")
    Estado = input("por favor ingrese el estado del cheque: ")
    myFile.writerow([NroCheque, CodigoBanco, CodigoSucursal, NumeroCuentaOrigen,
                    NumeroCuentaDestino, Valor, FechaOrigen, FechaPago, dni, Estado])
Salida_Pantalla = input(
    "por favor escriba 'pantalla' si quiere imprimir en consola o 'csv' si quiere un acrhivo.csv: ")

with open("Cuentasinput.csv", "r") as File_Read:
    csv_reader = csv.reader(File_Read, delimiter=";")

    if Salida_Pantalla == "pantalla":
        for line in File_Read:
            print(line)
    elif Salida_Pantalla == "csv":
        print("adios")
    else:
        print("Error")
