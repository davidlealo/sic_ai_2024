import cv2
import os
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Obtener la clave API de Roboflow
API_KEY = os.getenv('ROBOFLOW_API_KEY')

# Inicializar cliente de inferencia de Roboflow
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=API_KEY  # Usa la clave API cargada
)

# Ruta de la imagen local
image_path = "6a0f4365-98a5-4c26-9030-3703e59cc68e.jpeg"  # Cambia esto por la ruta de tu imagen

# Leer la imagen usando OpenCV
image = cv2.imread(image_path)

# Verificar si la imagen se ha cargado correctamente
if image is None:
    print(f"Error: No se pudo cargar la imagen en la ruta: {image_path}")
else:
    print("Imagen cargada correctamente.")

    # Enviar la imagen a Roboflow
    try:
        result = CLIENT.infer(image_path, model_id="insect-bites/1")
        print(result)  # Mostrar el resultado de la detección
    except Exception as e:
        print(f"Error en la inferencia: {str(e)}")

