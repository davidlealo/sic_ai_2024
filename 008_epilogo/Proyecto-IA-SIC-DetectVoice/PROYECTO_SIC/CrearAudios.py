# Importamos las librerías necesarias
from pydub import AudioSegment
import os
import random
import uuid
import subprocess

#EN CASO QUE USES DRIVE
# Función para montar Google Drive
#   def montar_drive():
#     drive.mount('/content/drive')
#     print("Google Drive montado correctamente.")
    
# Función para "montar" carpetas locales, imitando el propósito de montar Google Drive
def montar_directorios(folder_descargas, folder_clips):
    # Verifica si las carpetas existen, si no, las crea
    if not os.path.exists(folder_descargas):
        os.makedirs(folder_descargas)
        print(f"Carpeta de descargas '{folder_descargas}' creada correctamente.")
    else:
        print(f"Carpeta de descargas '{folder_descargas}' ya existe.")
        
    if not os.path.exists(folder_clips):
        os.makedirs(folder_clips)
        print(f"Carpeta de clips '{folder_clips}' creada correctamente.")
    else:
        print(f"Carpeta de clips '{folder_clips}' ya existe.")
        
# Función para descargar el video de YouTube como FLAC
def descargar_audio_youtube(url, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # Crear carpeta si no existe
    print(f"Descargando audio desde {url}...")
    # Descargar el audio en formato FLAC en la carpeta especificada usando subprocess
    subprocess.run(["yt-dlp", "-x", "--audio-format", "flac", "-o", f"{output_folder}/%(title)s.%(ext)s", url])
    print("Descarga completa.")
    

# Función para dividir el archivo de audio en clips con duración y nombre aleatorios
def dividir_audio_en_clips(audio_file, min_duration_sec, max_duration_sec, output_folder_clips):
    # Carga el archivo de audio en formato FLAC
    audio = AudioSegment.from_file(audio_file, format="flac")

    # Crea la carpeta de clips si no existe
    os.makedirs(output_folder_clips, exist_ok=True)

    # Inicializamos la posición inicial
    start_time = 0

    # Divide el archivo en clips de duración aleatoria entre min_duration_sec y max_duration_sec
    while start_time < len(audio):
        # Genera una duración aleatoria para el clip dentro del rango especificado
        clip_duration_ms = random.randint(min_duration_sec * 1000, max_duration_sec * 1000)
        end_time = min(start_time + clip_duration_ms, len(audio))  # Evita pasar la duración del audio

        # Extrae el clip y le asigna un nombre único aleatorio
        clip = audio[start_time:end_time]
        clip_name = f"clip_{uuid.uuid4()}.flac"  # Nombre aleatorio único
        clip.export(os.path.join(output_folder_clips, clip_name), format="flac")
        print(f"Guardado: {clip_name} (Duración: {clip_duration_ms / 1000} segundos)")

        # Avanzamos al siguiente segmento
        start_time = end_time

    print(f"Proceso completo. Los clips se guardaron en {output_folder_clips}")
    
# Función principal que combina todos los pasos
def procesar_video_youtube(url, min_duration_sec, max_duration_sec, folder_descargas, folder_clips):
    # Montamos los directorios locales, asegurándonos de pasar los argumentos
    montar_directorios(folder_descargas, folder_clips)
    
    # En el caso de que use drive es 
    # montar_drive()
    
    # Descargamos el video desde YouTube y lo convertimos a FLAC
    descargar_audio_youtube(url, folder_descargas)

    # Obtener el archivo de audio descargado (último archivo en la carpeta)
    audio_files = [f for f in os.listdir(folder_descargas) if f.endswith('.flac')]

    if not audio_files:
        print("No se encontró ningún archivo de audio en la carpeta de descargas.")
        return

    audio_file = max([os.path.join(folder_descargas, f) for f in audio_files], key=os.path.getctime)

    # Dividimos el audio en clips con duración aleatoria y nombre único
    dividir_audio_en_clips(audio_file, min_duration_sec, max_duration_sec, folder_clips)

# Configuración de los parámetros y ejecución del flujo completo
url_video = "https://youtu.be/6rq_wS3EFD0?si=xSNXpkTthJHi4bNl"  # URL del video de YouTube


# Rutas locales en el PC
carpeta_descargas = r"C:/Users/Alejandro Pimiento/Documents/GitHub/ProyectoIA/PROYECTO_SIC/videos_Audio_Pruebas"
carpeta_clips_IA = r"C:/Users/Alejandro Pimiento/Documents/GitHub/ProyectoIA/PROYECTO_SIC/Voces IA"
carpeta_clips_Real = r"C:/Users/Alejandro Pimiento/Documents/GitHub/ProyectoIA/PROYECTO_SIC/Voces reales"

# Definimos el rango de duración aleatoria para los clips
duracion_clip_min = 10  # Duración mínima en segundos
duracion_clip_max = 50  # Duración máxima en segundos

# Ejecutamos el flujo completo en las carpetas de voces IA
procesar_video_youtube(url_video, duracion_clip_min, duracion_clip_max, carpeta_descargas, carpeta_clips_IA)

# Ejecutamos el flujo completo en las carpetas de voces reales
procesar_video_youtube(url_video, duracion_clip_min, duracion_clip_max, carpeta_descargas, carpeta_clips_Real)