// Acceder a la cámara
const video = document.getElementById('webcam');

// Solicitar acceso a la cámara
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream; // Mostrar el stream de video en el elemento <video>
    })
    .catch(error => {
        console.error("Error al acceder a la cámara:", error);
    });

// Capturar imagen de la webcam
document.getElementById('capture').addEventListener('click', () => {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/png'); // Obtener datos de imagen en formato base64

    // Enviar imagen a la API para predicción
    fetch('/predict_webcam', {
        method: 'POST',
        body: JSON.stringify({ image: imageData }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Mostrar los resultados de la predicción
                console.log(data.prediction); // Ver la predicción en la consola
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = `<pre>${JSON.stringify(data.prediction, null, 2)}</pre>`;
            } else {
                // Mostrar un mensaje de error
                alert(data.message || "Error en la predicción.");
            }
        })
        .catch(error => {
            console.error("Error al enviar la imagen:", error);
        });
});

// Manejar la predicción de la imagen local
document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evita el envío tradicional del formulario

    const formData = new FormData(this);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log("Respuesta de la predicción:", data);  // Aquí puedes ver el JSON completo en la consola
            const localResultDiv = document.getElementById('localResult');
            if (data.success) {
                localResultDiv.innerHTML = `<pre>${JSON.stringify(data.prediction, null, 2)}</pre>`;
            } else {
                localResultDiv.innerHTML = `<p>Error en la predicción: ${data.message}</p>`;
            }
        })
        .catch(error => {
            console.error("Error al enviar la imagen local:", error);
        });
});



