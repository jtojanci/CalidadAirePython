import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA

def construirDataICA():
    #Creando un dataFrame
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna","ica","fecha","id"])
    dataFrameICA.to_csv("datosica.csv",index=False)
    print(dataFrameICA)

    #generando grafica de los datos por columna
    datosOrdenadosPorComuna=dataFrameICA.groupby("comuna")["ica"].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadosPorComuna.plot(kind="bar",color="green")
    plt.show()

construirDataICA()