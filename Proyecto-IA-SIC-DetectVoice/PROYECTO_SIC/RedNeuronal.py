# Importamos las librerías
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import gc
from pydub import AudioSegment
from pydub.utils import mediainfo
import subprocess
#Librerias CNN
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

# Rutas locales en el PC
ruta_carpeta_IA = 'PROYECTO_SIC/Voces IA'
ruta_carpeta_reales = 'PROYECTO_SIC/Voces reales'
ruta_carpeta_combinadas = 'PROYECTO_SIC/Voces combinadas/clips'

# Función para convertir un archivo de audio en un espectrograma y guardarlo como imagen
def convertir_y_guardar_espectrograma(archivo_audio, nombre_salida, carpeta_espectro):
    # Cargar el audio en segmentos (máximo de 60 segundos)
    y, sr = librosa.load(archivo_audio, sr=None, duration=60)

    # Generar el espectrograma Mel con menor resolución
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)

    # Convertir el espectrograma a escala logarítmica
    S_db = librosa.power_to_db(S, ref=np.max)

    # Crear una imagen del espectrograma usando matplotlib
    plt.figure(figsize=(5, 2))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='mel')

    # Eliminar los ejes y el marco
    plt.axis('off')

    # Guardar la imagen del espectrograma en la carpeta de salida sin ejes
    ruta_imagen = os.path.join(carpeta_espectro, nombre_salida)
    plt.tight_layout()
    plt.savefig(ruta_imagen, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()

    # Liberar memoria
    gc.collect()

    return ruta_imagen

def obtener_data_audio(ruta_archivo_1, ruta_salida, bandera):
    nombres_archivos = []
    duraciones = []
    frecuencias_muestreo = []
    rutas_imagenes_espectrograma = []
    etiquetas = []

    archivos_audio = [f for f in os.listdir(ruta_archivo_1) if f.endswith('.mp3') or f.endswith('.wav') or f.endswith('.flac')]
    print(f"Archivos de audio encontrados en {ruta_archivo_1}: {archivos_audio}")  # Verifica los archivos encontrados

    for archivo in archivos_audio:
        ruta_archivo = os.path.join(ruta_archivo_1, archivo)
        print(f"Procesando archivo: {ruta_archivo}")  # Muestra el archivo en proceso

        # Conversión de FLAC a WAV si es necesario
        if archivo.endswith('.flac'):
            ruta_archivo2 = convertir_flac_a_wav(ruta_archivo)
            if ruta_archivo2 is None:
                print(f"Error al convertir el archivo {archivo}.")
                continue  # Salta al siguiente archivo si la conversión falla

        # Actualiza la ruta del archivo si fue convertido
        ruta_archivo = ruta_archivo2 if archivo.endswith('.flac') else ruta_archivo

        # Cargar el archivo de audio y obtener la duración
        y, sr = librosa.load(ruta_archivo, sr=None, duration=60)
        duracion = librosa.get_duration(y=y, sr=sr)
        print(f"Duración del archivo {archivo}: {duracion} segundos")

        # Guardar la información en listas
        nombres_archivos.append(archivo)
        duraciones.append(duracion)
        frecuencias_muestreo.append(sr)

        # Generar y guardar el espectrograma
        nombre_salida_espectrograma = archivo.replace('.mp3', '.png').replace('.wav', '.png')
        ruta_imagen = convertir_y_guardar_espectrograma(ruta_archivo, nombre_salida_espectrograma, ruta_salida)
        rutas_imagenes_espectrograma.append(ruta_imagen)
        etiquetas.append(1 if bandera == 1 else 0)

    # Crear DataFrame
    df = pd.DataFrame({
        'Nombre del archivo': nombres_archivos,
        'Duración (segundos)': duraciones,
        'Frecuencia de muestreo': frecuencias_muestreo,
        'Ruta espectrograma': rutas_imagenes_espectrograma,
        'Etiqueta': etiquetas
    })

    print("DataFrame creado:\n", df.head())  # Muestra el DataFrame resultante
    return df

# Crear todas las carpetas locales donde se guardarán los espectrogramas
carpeta_salida_espectrogramas_IA = "PROYECTO_SIC/espectrogramas_IA"

# Crear la carpeta para guardar los espectrogramas si no existe
if not os.path.exists(carpeta_salida_espectrogramas_IA):
    os.makedirs(carpeta_salida_espectrogramas_IA)
    
carpeta_salida_espectrogramas_reales = "PROYECTO_SIC/espectrogramas_Reales/"

# Crear la carpeta para guardar los espectrogramas si no existe
if not os.path.exists(carpeta_salida_espectrogramas_reales):
    os.makedirs(carpeta_salida_espectrogramas_reales)
    
carpeta_salida_espectrogramas_combinados = 'PROYECTO_SIC/espectrogramas_combinados/'

# Crear la carpeta para guardar los espectrogramas si no existe
if not os.path.exists(carpeta_salida_espectrogramas_combinados):
    os.makedirs(carpeta_salida_espectrogramas_combinados)

def convertir_flac_a_wav(archivo_flac):
    # Comprobar si el archivo existe y es un archivo FLAC
    if not archivo_flac.endswith('.flac'):
        print(f"El archivo {archivo_flac} no es un archivo FLAC.")
        return None

    # Crear la ruta del archivo WAV
    archivo_wav = archivo_flac.replace('.flac', '.wav')

    # Intentar convertir el archivo FLAC a WAV usando ffmpeg, con sobrescritura automática
    try:
        subprocess.run(['ffmpeg', '-y', '-i', archivo_flac, archivo_wav], check=True)  # Se agregó el parámetro -y
        print(f"Conversión exitosa: {archivo_flac} -> {archivo_wav}")
        return archivo_wav

    except subprocess.CalledProcessError as e:
        print(f"Error al convertir {archivo_flac} con ffmpeg: {e}")
        return None  # Devuelve None si la conversión falla

df_IA = obtener_data_audio(ruta_carpeta_IA , carpeta_salida_espectrogramas_IA, 0 )

#mostramos el df_IA
df_IA.head()

#vamos a ver todo el df_IA
df_IA.info()
df_IA['Ruta espectrograma'].tail()

#ahora vamos con las voces reales
df_reales = obtener_data_audio(ruta_carpeta_reales, carpeta_salida_espectrogramas_reales, 1)

#mostramos el df_reales
df_reales.head()

def cargar_espectrogramas(df):
    # Tamaño de las imágenes de espectrograma
    img_width, img_height = 128, 128

    # Inicializar listas para las imágenes y las etiquetas
    X = []
    y = []

    for index, row in df.iterrows():
        img_path = row['Ruta espectrograma']
        etiqueta = row['Etiqueta']

        # Cargar la imagen y redimensionarla
        img = load_img(img_path, target_size=(img_width, img_height), color_mode="grayscale")
        img_array = img_to_array(img)

        #vamos a ver la etiqueta
        #print("Etiqueta de la imagen: " , etiqueta)
        #vamos a ver la imagen
        #antes de normalizar
        #plt.imshow(img_array.squeeze(), cmap='gray')
        #plt.title(f'Espectrograma - Etiqueta: {etiqueta}')
        #plt.axis('off')
        #plt.show()

        # Normalizar los valores de la imagen entre 0 y 1
        img_array /= 255.0

        #despues de normalizar
        #plt.imshow(img_array.squeeze(), cmap='gray')
        #plt.axis('off')
        #plt.show()
        #print("---------------------------------------")

        X.append(img_array)
        y.append(etiqueta)

    return np.array(X), np.array(y)

# las rutas de los archivos
rutas_espectrogramas_IA = df_IA["Ruta espectrograma"].values
rutas_espectrogramas_reales = df_reales["Ruta espectrograma"].values

# Unir las rutas de espectrogramas IA y reales
rutas_espectrogramas = np.concatenate((rutas_espectrogramas_IA, rutas_espectrogramas_reales), axis=0)

# Cargar los espectrogramas como antes
X_IA, y_IA = cargar_espectrogramas(df_IA)
X_reales, y_reales = cargar_espectrogramas(df_reales)

# Unir los datasets IA y reales
X = np.concatenate((X_IA, X_reales), axis=0)
y = np.concatenate((y_IA, y_reales), axis=0)

# Convertir etiquetas a formato categórico (one-hot encoding)
y = to_categorical(y, num_classes=2)

# Dividir en conjuntos de entrenamiento y prueba, manteniendo las rutas de los archivos en X_test
X_train, X_test, y_train, y_test, rutas_train, rutas_test = train_test_split(
    X, y, rutas_espectrogramas, test_size=0.2, random_state=42
)

# Crear la arquitectura del modelo CNN
model = Sequential()

# Primera capa convolucional
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Segunda capa convolucional
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Tercera capa convolucional
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aplanamiento
model.add(Flatten())

# Capa densa completamente conectada
model.add(Dense(128, activation='relu'))

# Capa de salida (2 clases: IA o Real)
model.add(Dense(2, activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=15, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {test_acc * 100:.2f}%")

# Gráfica de la precisión
plt.plot(history.history['accuracy'], label='Entrenamiento')
plt.plot(history.history['val_accuracy'], label='Validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend(loc='lower right')
plt.show()

# Gráfica de la pérdida
plt.plot(history.history['loss'], label='Entrenamiento')
plt.plot(history.history['val_loss'], label='Validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend(loc='upper right')
plt.show()

# Realizar predicciones con el conjunto de prueba
predicciones = model.predict(X_test)

# Convertir las predicciones de probabilidades a etiquetas (0 o 1)
predicciones_clases = np.argmax(predicciones, axis=1)

# Mostrar las primeras 50 predicciones con rutas y niveles de confianza
for i in range(50):
    ruta_archivo = rutas_test[i]
    prediccion = predicciones_clases[i]
    confianza = predicciones[i][prediccion] * 100

    # Mostrar ubicación, predicción en términos de clase y confianza
    print(f"Ubicación en Drive: {ruta_archivo}")
    print(f"Predicción del modelo: Clase {prediccion} ({confianza:.2f}% de confianza)\n")

# Evaluar el modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Precisión en el conjunto de prueba: {test_acc * 100:.2f}%")

