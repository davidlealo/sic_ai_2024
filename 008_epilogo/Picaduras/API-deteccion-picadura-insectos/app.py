import os
from flask import app
from dotenv import load_dotenv
import base64
from flask import Flask, request, jsonify, render_template
import pyscreenshot
from PIL import Image
import numpy as np
import os
import io
from inference_sdk import InferenceHTTPClient

app = Flask(__name__)

#cargar variables de entorno
load_dotenv()

# Configuración de Roboflow
API_KEY = os.getenv('api_key')
MODEL_ID = os.getenv("model_id")

if not API_KEY or not MODEL_ID:
    raise ValueError("Las variables de entorno 'api_key' y 'model_id' deben estar configuradas correctamente.")

# Inicializar cliente de inferencia
CLIENT = InferenceHTTPClient(
    api_url="https://outline.roboflow.com",
    api_key=API_KEY
)

@app.route('/')
def home():
    # Renderiza la página principal con la interfaz de la cámara
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"success": False, "message": "No se ha subido ninguna imagen."}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"success": False, "message": "No se ha seleccionado ninguna imagen."}), 400

    try:
        # Convertir la imagen usando PIL
        image = Image.open(file)
        # Convertir a base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        # Hacer la predicción con la imagen en base64
        result = CLIENT.infer(img_str, model_id=MODEL_ID)
        return jsonify({"success": True, "prediction": result['predictions'][0]['class']})
        
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/predict_webcam', methods=['POST'])
def predict_webcam():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'success': False, 'message': 'No se recibió imagen.'}), 400

    try:
        # Usar directamente la imagen en base64
        image_data = data['image'].split(',')[1]
        
        # Realizar inferencia con la imagen en base64
        result = CLIENT.infer(image_data, model_id=MODEL_ID)
        return jsonify({"success": True, "prediction": result['predictions'][0]['class']})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))