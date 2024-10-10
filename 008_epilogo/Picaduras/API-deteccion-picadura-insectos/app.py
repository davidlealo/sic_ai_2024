import cv2
import base64
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Inicializar cliente de inferencia de Roboflow
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.getenv('ROBOFLOW_API_KEY')  # Tu clave API de Roboflow
)

# Iniciar la captura de la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede acceder a la cámara")
    exit()

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    if not ret:
        print("No se puede recibir frame. Finalizando...")
        break

    # Mostrar el frame capturado en una ventana
    cv2.imshow('Webcam - Presiona "q" para salir', frame)

    # Guardar la imagen capturada temporalmente
    image_path = "temp_image.jpg"
    cv2.imwrite(image_path, frame)

    # Convertir la imagen a base64 para enviarla a Roboflow
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

    # Enviar la imagen a Roboflow
    try:
        result = CLIENT.infer(image_path, model_id="insect-bites/1")
        print(result)  # Mostrar el resultado de la detección
    except Exception as e:
        print(f"Error en la inferencia: {str(e)}")

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo esté hecho, libera la captura
cap.release()
cv2.destroyAllWindows()
