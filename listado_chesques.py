import sys

nombrDelArchivo=sys.argv[1]
dniParametro=sys.argv[2]
"""salida=sys.argv[3]
tipoDeCheque=sys.argv[4]
estadoDelCheque=sys.argv[5]
rangoFecha=sys.argv[6]  """
num=0  
todoLosDatosCheque={}
NroDeChequesDic={}
CodigoBanco={}
CodigoScurusal={}
NumeroCuentaOrigen={}
NumeroCuentaDestino={}
Valor={}
FechaOrigen={}
FechaPago={}
dni={}
Estado={}

cheques= open(nombrDelArchivo,"r")
next(cheques,None)
    
for cheque in cheques:
    num+=1 
    cheque=cheque.rstrip("\n")
    chequeSeparado=cheque.split(";")
    todoLosDatosCheque[str(num)]=chequeSeparado
    NroDeChequesDic[str(num)]=chequeSeparado[0]
    CodigoBanco[str(num)]=chequeSeparado[1]
    CodigoScurusal[str(num)]=chequeSeparado[2]
    NumeroCuentaOrigen[str(num)]=chequeSeparado[3]
    NumeroCuentaDestino[str(num)]=chequeSeparado[4]
    Valor[str(num)]=chequeSeparado[5]
    FechaOrigen[str(num)]=chequeSeparado[6]
    FechaPago[str(num)]=chequeSeparado[7]
    dni[str(num)]=chequeSeparado[8]
    Estado[str(num)]=chequeSeparado[9]
  
cheques.close()

chequesSelecionados={}
nana=0
for NroDni in dni:
    nana+=1
    if dniParametro == dni[NroDni]:
        chequesSelecionados[str(nana)]=str(chequeSeparado)





print(chequesSelecionados)



""" print (NroDeChequesDic)
print(CodigoBanco)
print(CodigoScurusal)
print(NumeroCuentaOrigen)
print(NumeroCuentaDestino)
print(Valor)
print(FechaOrigen)
print(FechaPago)
print(dni)
print(Estado) """



