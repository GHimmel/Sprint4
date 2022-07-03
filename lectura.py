""" import sys
import datetime
dia=str(datetime.datetime.now())
nombres= open("cuentas.csv","a")
nombres.write(sys.argv[1]+"; fecha: "+dia+"\n")
nombres.close """

from datetime import datetime
# Convertimos un string con formato <día>/<mes>/<año> en datetime
una_fecha = '30-05-2022'
fecha_dt = datetime.strptime(una_fecha,'%d/%m/%Y')
print(fecha_dt)

