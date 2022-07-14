import time
import csv
from datetime import datetime
import sys
# PARA LA CONSOLA: python listado_chesques.py cuentas.csv 41347590 CSV DEPOSITADO APROBADO 20-08-2022:20-09-2022
# PARA LA CONSOLA: python listado_chesques.py cuentas.csv "DNI" "SALIDA" "TIPO" "ESTADO o NONE" "FECHA:FECHA"
# Ej: python listado_chesques.py cuentas.csv 41917530 CVS  EMITIDO APROBADO 12-05-2000:25-05-2000
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

# if len(sys.argv) == 6:
#     ChequeNone = sys.argv[5]

#  elif len(sys.argv) == 7:
#      ChequeNone = sys.argv[5]
#      rangoFecha = sys.argv[6]

# Pasar Fecha de string a Timestamp--
""" Fecha_Separada = rangoFecha.split(":")
Fecha_Inicio = datetime.timestamp(
    datetime.strptime(Fecha_Separada[0], "%d-%m-%Y"))
Fecha_Fin = datetime.timestamp(
    datetime.strptime(Fecha_Separada[1], "%d-%m-%Y")) """
# ---------
with open(nombrDelArchivo, "r") as f:
    csv_cheques = csv.DictReader(f, delimiter=";")
    todosCheques = list(csv_cheques)

f.close()

# recorro todoCheques y voy comparando dni con dni parametro, si son iguales, agrego a una lista ese diccionario (posicionDNI)


def filtroDNIyCodigoBanco():

    for dni in todosCheques:

        if dniParametro == dni["DNI"]:
            # print(dni["DNI"])
            posicionDni.append(dni)

    for ndr in posicionDni:
        # print(ndr["NroCheque"])
        ndc.append(int(ndr["NroCheque"]))


def emitidoYdepositados():
    for emi in posicionDni:
        if emi["tipo"] == tipoDeCheque:  # EMITIDO o DEPOSITADO .
            emiOdepo.append(emi)

    # print(emiOdepo)


def estadosCheques():
    for x in emiOdepo:
        if estadoDelCheque:
            chequeEstado.append(x)
        elif x["Estado"] == estadoDelCheque:  # PENDIENTE, APROBADO, RECHAZADO.
            chequeEstado.append(x)

    """ if x["Estado"] == estadoDelCheque: #PENDIENTE, APROBADO, RECHAZADO.
            chequeEstado.append(x)
        elif estadoDelCheque == "NONE":
            chequeEstado.append(x) """

    # print(chequeEstado)

# en la lista ndc guarde todos los numeros de cheques correspondiente a ese dni, para ver que no se repitan, compare el len de la lista vs el len de la lista con un set, el exit para la ejecucion del programa


def numeroDeCheque():
    # print(ndc)
    # print(set(ndc))
    """ if len(ndc) != len(set(ndc)):
        print("ERROR: Numero de chueque duplicado")
        exit() """
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
        for x in chequeEstado:
            if Fecha_Inicio <= float(x["FechaOrigen"]) and Fecha_Fin >= float(x["FechaOrigen"]):
                ListaFecha.append(x)
    else:
        for x in chequeEstado:
            ListaFecha.append(x)

        # f = rangoFecha.split(":")
        # fechaInf = f[0]
        # fechaSup = f[1]
        # print(fechaInf)
        # print(fechaSup)
        # for y in chequeEstado:
        #     una_fecha = y["FechaOrigen"]
        #     fecha_dt = datetime.strptime(una_fecha, '%Y-%m-%d')
        #     fecha_dt = datetime.strptime(una_fecha, '%Y-%m-%d')

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
emitidoYdepositados()
estadosCheques()
fecha()
numeroDeCheque()
pantalla_CSV()
