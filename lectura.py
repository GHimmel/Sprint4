import sys
import datetime
dia=str(datetime.datetime.now())
nombres= open("cuentas.csv","a")
nombres.write(sys.argv[1]+"; fecha: "+dia+"\n")
nombres.close