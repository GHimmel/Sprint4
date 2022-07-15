import time
import csv
from datetime import datetime
import sys

# Ej: python listado_chesques.py cuentas.csv 41917530 CVS EMITIDO APROBADO 12-05-2000:25-05-2000

t = datetime.now()
times = t.date()
dia = time.localtime().tm_mday


posicionDni = []  # LISTA con diccionarios de los cheques del usuario filtrados
ndc = []  # Todos los numero de cheque del usuario
emiOdepo = []  # los cheques ya filtrados por el estado depositado o emitido
chequeEstado = []  # Los cheques filtrados por el estado
ListaFecha = []  # lista de las fechas
nombrDelArchivo = sys.argv[1]
dniParametro = sys.argv[2]
salida = sys.argv[3]
tipoDeCheque = sys.argv[4]
estadoDelCheque = None
rangoFecha = None

if len(sys.argv) == 6:
    if sys.argv[5] == "APROBADO" or sys.argv[5] == "PENDIENTE" or sys.argv[5] == "RECHAZADO":
        estadoDelCheque = sys.argv[5]
    else:
        rangoFecha = sys.argv[5]

elif len(sys.argv) == 7:
    estadoDelCheque = sys.argv[5]
    rangoFecha = sys.argv[6]

with open(nombrDelArchivo, "r") as f:
    csv_cheques = csv.DictReader(f, delimiter=";")
    todosCheques = list(csv_cheques)

f.close()

# recorro todoCheques y voy comparando dni con dni parametro, si son iguales, agrego a una lista ese diccionario (posicionDNI)

def filtroDNIyCodigoBanco():

    for dni in todosCheques:

        if dniParametro == dni["DNI"] and tipoDeCheque == dni["tipo"]:
            if estadoDelCheque:
                if estadoDelCheque == dni["Estado"]:
                    posicionDni.append(dni)
            else: 
                posicionDni.append(dni)

# en la lista ndc guarde todos los numeros de cheques correspondiente a ese dni, para ver que no se repitan, compare el len de la lista vs el len de la lista con un set, el exit para la ejecucion del programa

def numeroDeCheque():
    vistos = set()
    for y in ListaFecha:
        nro_cheque = y["NroCheque"]
        nro_cuenta = y["NumeroCuentaOrigen"]
        dni = y["DNI"]
        if (nro_cheque, nro_cuenta, dni) in vistos:
            print("ERROR: Numero de chueque o de cuenta duplicado")
            exit()
        else:
            vistos.add((nro_cheque, nro_cuenta, dni))

# filtro para rango de fecha

def fecha():

    if rangoFecha:
        Fecha_Separada = rangoFecha.split(":")
        Fecha_Inicio = datetime.timestamp(
            datetime.strptime(Fecha_Separada[0], "%d-%m-%Y"))
        Fecha_Fin = datetime.timestamp(
            datetime.strptime(Fecha_Separada[1], "%d-%m-%Y"))
        for x in posicionDni:
            if Fecha_Inicio <= float(x["FechaOrigen"]) and Fecha_Fin >= float(x["FechaOrigen"]):
                ListaFecha.append(x)
    else:
        for x in posicionDni:
            ListaFecha.append(x)

# ver por donde imprimir los parametro, pantalla o csv

def pantalla_CSV():
    if salida == "PANTALLA":
        print("NroCheque;CodigoBanco;CodigoScurusal;NumeroCuentaOrigen;NumeroCuentaDestino;Valor;FechaOrigen;FechaPago;DNI;Estado;tipo")
        for Datos in ListaFecha:
            """  print(Datos["FechaOrigen"]+";"+Datos["FechaPago"]+";"+Datos["Valor"]+";"+Datos["NumeroCuentaOrigen"]) """
            print(list(Datos.values()))

    elif salida == "CSV":
        print("creando archivo csv")
        with open(f"archivosCSV/{dniParametro}-{times}.csv", "w") as h:
            h.write("FechaOrigen;FechaPago;Valor;NumeroCuentaOrigen\n")
            for k in ListaFecha:
                h.write(k["FechaOrigen"]+";"+k["FechaPago"]+";" +
                        k["Valor"]+";"+k["NumeroCuentaOrigen"]+"\n")
        h.close


filtroDNIyCodigoBanco()
fecha()
numeroDeCheque()
pantalla_CSV() 

