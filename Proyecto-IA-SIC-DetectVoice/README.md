# Clasificación de Espectrogramas de Voces IA y Reales

Este proyecto permite la clasificación de voces generadas por IA y voces reales mediante la conversión de clips de audio en espectrogramas. Los espectrogramas generados se utilizan para entrenar y evaluar un modelo de red neuronal convolucional (CNN) que predice si un clip de audio es de una voz generada por IA o una voz real.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- `PROYECTO_SIC/Voces IA`: Contiene los clips de audio de voces generadas por IA.
- `PROYECTO_SIC/Voces reales`: Contiene los clips de audio de voces reales.
- `PROYECTO_SIC/espectrogramas_IA`: Carpeta para almacenar espectrogramas generados de las voces IA.
- `PROYECTO_SIC/espectrogramas_Reales`: Carpeta para almacenar espectrogramas generados de las voces reales.
- `PROYECTO_SIC/espectrogramas_combinados`: Carpeta para combinar espectrogramas de ambos tipos de voces (opcional).
- `PROYECTO_SIC/RedNeuronal.py`: Script principal para el entrenamiento y evaluación del modelo.
- `PROYECTO_SIC/CrearAudios.py`: Script para la generación y procesamiento de clips de audio.

## Requisitos Previos

1. **Python**: Asegúrate de tener Python 3.12 instalado en tu sistema.
2. **Visual Studio Code**: Descarga e instala [Visual Studio Code](https://code.visualstudio.com/).
3. **Extensión de Python en VS Code**: Instala la extensión de Python para Visual Studio Code desde el [Marketplace de VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Instalación de Dependencias

### Paso 1: Ejecutar el Script de Configuración

- Abrir una terminal en la carpeta raíz del proyecto.
- Ejecutar el .bash "dependencias.bat":

### Paso 2: Preparar los Archivos de Audio

- Colocar los archivos de audio en formato .mp3, .wav o .flac en las carpetas correspondientes:
 - Colocar voces generadas por IA en PROYECTO_SIC/Voces IA.
 - Colocar voces reales en PROYECTO_SIC/Voces reales.

### Paso 3: Generar Espectrogramas desde los Clips de Audio

- Abrir Visual Studio Code y cargar el directorio raíz del proyecto.
- Navegar a PROYECTO_SIC/CrearAudios.py.
- Ejecutar el script CrearAudios.py presionando F5 o haciendo clic en Run > Start Debugging para procesar los clips de audio y generar espectrogramas.

### Paso 4: Entrenar el Modelo en Visual Studio Code
- Navegar a PROYECTO_SIC/RedNeuronal.py en el explorador de archivos de VS Code.
- Ejecutar el script RedNeuronal.py presionando F5 o haciendo clic en Run > Start Debugging para entrenar y evaluar el modelo usando los espectrogramas generados.

### Paso 5: Ejecutar los Scripts desde la Terminal (Opcional)

- Para ejecutar CrearAudios.py desde la terminal:

- python PROYECTO_SIC/CrearAudios.py

- Para ejecutar RedNeuronal.py desde la terminal:

- python PROYECTO_SIC/RedNeuronal.py

# Estructura del Código

## Funciones Principales

- convertir_flac_a_wav (en CrearAudios.py): Convierte archivos .flac a .wav automáticamente si es necesario.
- convertir_y_guardar_espectrograma (en CrearAudios.py): Convierte un archivo de audio en un espectrograma y lo guarda como imagen.
- obtener_data_audio (en CrearAudios.py): Lee los archivos de audio, genera espectrogramas y almacena la información en un DataFrame.
- cargar_espectrogramas (en RedNeuronal.py): Carga las imágenes de espectrogramas y etiquetas para el entrenamiento del modelo.
- Definición del modelo CNN (en RedNeuronal.py): Construye, entrena y evalúa el modelo.

# Notas Importantes

- ffmpeg en el PATH: Asegúrate de que ffmpeg esté en el PATH del sistema. Si el archivo .wav de salida ya existe, se sobrescribirá automáticamente sin solicitar confirmació

- se recomienda revisar las sugerencias para la instalacion de la libreria ffmpeg

---

© Todos los derechos reservados para Samsung Innovation Campus. Proyecto desarrollado por Ethan Astorga y Alejandro Pimiento.

