import pandas as pd
import os

# Definir las preguntas, perfiles y puntuaciones (ajusta según tus necesidades)
preguntas = ["Pregunta1", "Pregunta2", "Pregunta3", "Pregunta4", "Pregunta5", "Pregunta6", "Pregunta7", "Pregunta8", "Pregunta9", "Pregunta10"]
perfiles = ["Turista de Playa", "Turista de Ciudades", "Aventurero", "Cultura y Arte", "Gastronómico"]
puntos_perfil = {
    "Turista de Playa": [5, 1, 2, 1, 1, 4, 1, 3, 2, 2],
    "Turista de Ciudades": [1, 5, 1, 3, 2, 2, 2, 3, 3, 3],
    "Aventurero": [2, 2, 5, 1, 1, 3, 2, 5, 1, 2],
    "Cultura y Arte": [2, 2, 1, 5, 1, 1, 5, 3, 2, 2],
    "Gastronómico": [1, 2, 2, 2, 5, 1, 2, 2, 1, 1]
}

# Obtener una lista de archivos CSV en el directorio actual
archivos_csv = [archivo for archivo in os.listdir() if archivo.endswith('.csv')]

# Procesar cada archivo CSV
for archivo_csv in archivos_csv:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)

    # Crear una columna "Perfil" con valores iniciales vacíos
    data['Perfil'] = ""

    # Asignar perfiles en función de las respuestas
    for index, row in data.iterrows():
        respuestas = [row[pregunta] for pregunta in preguntas]
        puntuaciones = {perfil: sum(a * b for a, b in zip(respuestas, puntos_perfil[perfil])) for perfil in perfiles}
        perfil_asignado = max(puntuaciones, key=puntuaciones.get)
        data.at[index, 'Perfil'] = perfil_asignado

    # Guardar el DataFrame con los perfiles asignados en un nuevo archivo CSV
    archivo_salida = f"perfiles_asignados_{archivo_csv}"
    data.to_csv(archivo_salida, index=False)

    print(f"Perfiles asignados y guardados en '{archivo_salida}'.")
