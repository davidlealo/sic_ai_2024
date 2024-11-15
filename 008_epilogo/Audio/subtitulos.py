import speech_recognition as sr


def real_time_subtitles():
    # Inicializamos el reconocedor
    recognizer = sr.Recognizer()

    # Usamos el micrófono como fuente
    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental... Un momento.")
        recognizer.adjust_for_ambient_noise(source)
        print("¡Comienza a hablar!")

        # Abre un archivo para escribir los subtítulos en tiempo real
        with open("subtitulos.txt", "w") as f:
            try:
                while True:
                    # Escucha el audio con un tiempo de espera y límite de frase más largos
                    print("Escuchando...")
                    audio = recognizer.listen(
                        source, timeout=10, phrase_time_limit=30)

                    # Intenta reconocer el audio
                    try:
                        text = recognizer.recognize_google(
                            audio, language="es-ES")
                        print(f"Subtítulo: {text}")

                        # Escribe los subtítulos en el archivo de texto
                        f.write(f"{text}\n")
                        f.flush()  # Asegura que los datos se escriban inmediatamente en el archivo
                    except sr.UnknownValueError:
                        print("No se pudo entender el audio.")
                    except sr.RequestError as e:
                        print(
                            f"Error con el servicio de reconocimiento de voz; {e}")

            except KeyboardInterrupt:
                print("Deteniendo subtítulos en tiempo real.")


if __name__ == "__main__":
    real_time_subtitles()
