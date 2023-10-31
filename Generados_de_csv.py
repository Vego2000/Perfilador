import pandas as pd
import random

# Parámetros de configuración
num_usuarios = 1000000  # Cambia este número según la cantidad de usuarios que desees
num_preguntas = 10  # Número de preguntas en el cuestionario
rango_respuestas = (1, 5)  # Rango de respuestas permitidas

# Generar datos aleatorios para el archivo CSV
datos = []
for i in range(1, num_usuarios + 1):
    respuestas = [random.randint(rango_respuestas[0], rango_respuestas[1]) for _ in range(num_preguntas)]
    datos.append([f'Usuario{i}'] + respuestas)

# Crear un DataFrame de pandas
columnas = ['Usuario'] + [f'Pregunta{i}' for i in range(1, num_preguntas + 1)]
df = pd.DataFrame(datos, columns=columnas)

# Guardar el DataFrame en un archivo CSV
nombre_archivo = 'respuestas5.csv'
df.to_csv(nombre_archivo, index=False)

print(f"Se ha creado el archivo CSV '{nombre_archivo}' con {num_usuarios} usuarios y {num_preguntas} preguntas.")
