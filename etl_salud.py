import pandas as pd
from sqlalchemy import create_engine
import time 

inicio = time.time()
print ("Iniciando ETL con datos sinteticos Sector Salud con MySQL")

#Lectura del archivo CSV creado con Faker y extraccion de registros
df = pd.read_csv("expedientes_sinteticos_salud.csv")
print (f"Extraidos:{len(df)} registros")


#Transformación de datos 
df["Fecha_Solicitud"]= pd.to_datetime(df["Fecha_Solicitud"])
df["Fecha_Referencia"] = pd.to_datetime(df["Fecha_Referencia"])

#Calculo de dias de espera
df["Dias_Espera"] =(df["Fecha_Referencia"]-df["Fecha_Solicitud"]).dt.days
df = df[df["Dias_Espera"]>=0]
# Se asignan niveles de prioridad si es de -1 a 7 la prioridad es Baja, si es de 7 a 21 es media y si es de 21 en adelante la prioridad sera Alta
#Es decir entre mas dias este el paciente en espera la prioridad aumentara 
df["Nivel_Prioridad"]= pd.cut(df["Dias_Espera"], bins=[-1, 7, 21, 100], labels= ["Baja","Media", "Alta"])

print(f"Transformados: {len(df)} registros válidos")

print(df.head())