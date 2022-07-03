import time
import csv
from datetime import datetime
import sys

from listado_chesques import FechaOrigen

t = datetime.now()
times = t.date()
dia = time.localtime().tm_mday
""" hora=time.localtime().tm_hour 
mes=time.localtime().tm_mon
año=time.localtime().tm_year """  # timestamps

posicionDni = []  # LISTA con diccionarios de los cheques del usuario filtrados
ndc = []  # Todos los numero de cheque del usuario
emiOdepo = []  # los cheques ya filtrados por el estado depositado o emitido
chequeEstado = []  # Los cheques filtrados por el estado
nombrDelArchivo = sys.argv[1]
dniParametro = sys.argv[2]
salida = sys.argv[3]
tipoDeCheque = sys.argv[4]
estadoDelCheque = sys.argv[5]
rangoFecha = sys.argv[6]

with open(nombrDelArchivo, "r") as f:
    csv_cheques = csv.DictReader(f, delimiter=";")
    todosCheques = list(csv_cheques)

f.close()

# recorro todoCheques y voy comparando dni con dni parametro, si son iguales, agrego a una lista ese diccionario (posicionDNI)


def filtroDNIyCodigoBanco():

    for dni in todosCheques:

        if dniParametro == dni["DNI"]:
            print(dni["DNI"])
            posicionDni.append(dni)

    for ndr in posicionDni:
        print(ndr["NroCheque"])
        ndc.append(int(ndr["NroCheque"]))


# en la lista ndc guarde todos los numeros de cheques correspondiente a ese dni, para ver que no se repitan, compare el len de la lista vs el len de la lista con un set, el exit para la ejecucion del programa

def numeroDeCheque():
    print(ndc)
    print(set(ndc))
    if len(ndc) != len(set(ndc)):
        print("ERROR: Numero de chueque duplicado")
        exit()


def emitidoYdepositados():
    for emi in posicionDni:
        if emi["tipo"] == tipoDeCheque:
            emiOdepo.append(emi)

    print(emiOdepo)


def estadosCheques():
    for x in emiOdepo:
        if x["Estado"] == estadoDelCheque:
            chequeEstado.append(x)
        elif estadoDelCheque == "NONE":
            chequeEstado.append(x)

    print(chequeEstado)


""" def fecha ():
    f=rangoFecha.split(":")
    fechaInf=f[0]
    fechaSup=f[1]
    print(fechaInf)
    print(fechaSup)
    for y in chequeEstado:
        una_fecha = y["FechaOrigen"]
        fecha_dt = datetime.strptime(una_fecha,'%Y-%m-%d') """


# ver por donde imprimir los parametro, pantalla o csv

def pantalla_CSV():
    if salida == "PANTALLA":
        for Datos in chequeEstado:
            print(Datos["FechaOrigen"]+";"+Datos["FechaPago"]+";" +
                  Datos["Valor"]+";"+Datos["NumeroCuentaOrigen"]+"\n")
    elif salida == "CSV":
        print("creando archivo csv")
        with open(f"{dniParametro}-{times}.csv", "a") as h:
            h.write("FechaOrigen;FechaPago;Valor;NumeroCuentaOrigen\n")
            for k in chequeEstado:
                h.write(k["FechaOrigen"]+";"+k["FechaPago"]+";" +
                        k["Valor"]+";"+k["NumeroCuentaOrigen"]+"\n")
        h.close


filtroDNIyCodigoBanco()
numeroDeCheque()
emitidoYdepositados()
estadosCheques()
""" fecha() """
pantalla_CSV()
