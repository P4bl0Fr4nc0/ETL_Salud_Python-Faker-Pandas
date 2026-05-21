import pandas as pd

#Libreria para generar datos aleatorios
from faker import Faker
import random 
from datetime import timedelta 

fake = Faker('es_MX')
Faker.seed(42)

data=[]

for i in range(1500):
 
 #Fecha de solicitud que sea entre hoy y hace 2 años 
 fecha_solicitud = fake.date_between(start_date ='-2y', end_date = 'today')
 dias_espera = random.randint(1,45)

 #generando fechas aleatorias para fecha referencia 
 fecha_referencia = fecha_solicitud + timedelta(days = dias_espera)

    #Datos hipoteticos
 data.append({
            'Folio': f'EXP-{260000+i}',
            'Institucion': random.choice(['IMSS','ISSSTE',"INER", "Centro de Salud","INNN", "INP", "Hospital de la mujer", "Hospitales Generalees"]),        
            'Fecha_Solicitud': fecha_solicitud,
            'Fecha_Referencia': fecha_referencia,
            'Diagnostico': random.choice(['Estomago','Colon','Recto','Pulmon', 'Tiroides', 'Riñon']),
            'Estatus': random.choice(['Completado','En proceso','Cancelado']),
            'Costo_Estimado': round(random.uniform(5000, 155000), 2)
          })

df = pd.DataFrame(data)
#Nombre del archivo que se creara 
df.to_csv('expedientes_sinteticos_salud.csv', index=False)
print("Se han generado 1500 expedientes sintéticos para pruebas")