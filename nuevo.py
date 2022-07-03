import csv
import sys
import time
dia=str(time.time())
n=0
posicionDni=[]
ndc=[]
nombrDelArchivo=sys.argv[1]
dniParametro=sys.argv[2] 
salida=sys.argv[3]
"""tipoDeCheque=sys.argv[4]
estadoDelCheque=sys.argv[5]
rangoFecha=sys.argv[6]  """

with open(nombrDelArchivo,"r") as f:
    csv_cheques=csv.DictReader(f,delimiter=";")
    todosCheques=list(csv_cheques)


   
    
        


f.close()
""" print(todosCheques[1]) 
print(posicionDni) """

def filtroDNIyCodigoBanco ():
    
    for dni in todosCheques:
        
        if dniParametro==dni["DNI"]:
            print(dni["DNI"])
            posicionDni.append(dni)
 
    
    for ndr in posicionDni:
        print(ndr["NroCheque"])
        ndc.append(int(ndr["NroCheque"]))


def numeroDeCheque ():
    print(ndc)
    print(set(ndc))
    if len (ndc) != len (set(ndc)):
        print ("ERROR: Numero de chueque duplicado")
        exit()
    
         
            
 

def pantalla_CSV ():
    if salida == "PANTALLA":
        print ("sale por pantalla")
    elif salida == "CSV":
        print ("creando archivo csv")
        with open(dniParametro+"-"+dia+".csv","a") as h:
            h.write("<"+dniParametro+"><"+dia+">\n")
        h.close


filtroDNIyCodigoBanco()
numeroDeCheque()
pantalla_CSV()
