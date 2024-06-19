import pandas as pd

from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido():
    datosRuido=generarDatosRuido()
    ruidoDataFrame=pd.DataFrame(datosRuido,columns=["id","Nivel Ruido","Comuna"])
    ruidoDataFrame.to_csv("ruido.csv",index=False)
    
construirDataRuido()