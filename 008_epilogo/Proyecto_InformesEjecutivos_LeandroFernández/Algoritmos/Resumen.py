import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from heapq import nlargest
from urllib.parse import urlparse, urlunparse
import re
import fitz

def limpiar_texto(texto):
    # Eliminar patrones como "[20]" y otros símbolos no deseados
    texto = re.sub(r'\[\d+\]', '', texto)
    texto = re.sub(r'[^\w\s.,;!?]', '', texto)
    return texto.strip()

def resumir_articulo(url, Extension, num_sentences=8):
    try:
        # Limpiar el URL
        parsed_url = urlparse(url)
        clean_url = urlunparse(parsed_url._replace(query="", fragment=""))
        
        # Obtener el contenido del artículo
        response = requests.get(clean_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraer el texto principal
        article_text = ' '.join([limpiar_texto(p.text) for p in soup.find_all('p')])
        
        # Tokenizar el texto en oraciones y palabras
        sentences = sent_tokenize(article_text)
        words = word_tokenize(article_text.lower())
        
        # Eliminar stopwords
        stop_words = set(stopwords.words('spanish'))  # Cambia a 'english' si el texto está en inglés
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        
        # Calcular la frecuencia de las palabras
        word_freq = FreqDist(filtered_words)
        
        # Calcular el puntaje de cada oración
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_freq:
                    if len(sentence.split()) < Extension:  # Aumentamos el límite de palabras por oración
                        if sentence not in sentence_scores:
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]
        
        # Obtener las oraciones con mayor puntaje
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        
        # Ordenar las oraciones según su aparición en el texto original
        summary_sentences.sort(key=lambda x: sentences.index(x))
        
        # Unir las oraciones para formar el resumen
        summary = ' '.join(summary_sentences)
        
        # Asegurar que el resumen comience con una oración introductoria
        if sentences[0] not in summary_sentences:
            summary = sentences[0] + ' ' + summary
        
        return summary
    
    except Exception as e:
        return f"Se produjo un error al procesar el artículo: {str(e)}"
    



    
def resumir_articulo_texto(texto : str, Extension ,num_sentences = 8):
    try:
        # Extraer el texto principal
        article_text = texto
        
        # Tokenizar el texto en oraciones y palabras
        sentences = sent_tokenize(article_text)
        words = word_tokenize(article_text.lower())
        
        # Eliminar stopwords
        stop_words = set(stopwords.words('spanish'))  # Cambia a 'english' si el texto está en inglés
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        
        # Calcular la frecuencia de las palabras
        word_freq = FreqDist(filtered_words)
        
        # Calcular el puntaje de cada oración
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_freq:
                    if len(sentence.split()) < Extension:  # Aumentamos el límite de palabras por oración
                        if sentence not in sentence_scores:
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]
        
        # Obtener las oraciones con mayor puntaje
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        
        # Ordenar las oraciones según su aparición en el texto original
        summary_sentences.sort(key=lambda x: sentences.index(x))
        
        # Unir las oraciones para formar el resumen
        summary = ' '.join(summary_sentences)
        
        # Asegurar que el resumen comience con una oración introductoria
        if sentences[0] not in summary_sentences:
            summary = sentences[0] + ' ' + summary
        
        return summary
    
    except Exception as e:
        return f"Se produjo un error al procesar el artículo: {str(e)}"
    



def resumir_articulo_pdf(uploaded_file, Extension,num_sentences=8):
    # Función para leer el archivo PDF desde un objeto UploadedFile
    def leer_pdf(uploaded_file):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        texto = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            texto += page.get_text("text")
        return texto

    def limpiar_texto(texto):
        # Eliminar patrones de líneas de puntos
        texto = re.sub(r'\.+', '', texto)  # Elimina las líneas de puntos
        
        # Eliminar el índice (esto puede ajustarse según la estructura del índice)
        texto = re.sub(r'Índice.*?\n', '', texto, flags=re.DOTALL)  # Elimina todo lo que sigue a "Índice"
        
        # Limpiar el texto de patrones, caracteres no deseados y espacios
        texto = re.sub(r'\[\d+\]|[^\w\s.,;!?]|^\s+|\s+$|^\d+\s*$|\n\s*\n|[\n\s]+', ' ', texto)
        texto = re.sub(r'\s{2,}', ' ', texto)  # Reemplazar múltiples espacios por uno solo
        return texto.strip()

    # Función para resumir el texto
    def resumir_articulo(texto, num_sentences=8):
        article_text = limpiar_texto(texto)
        sentences = sent_tokenize(article_text)
        words = word_tokenize(article_text.lower())
        stop_words = set(stopwords.words('spanish'))  # Cambia a 'english' si el texto está en inglés
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        word_freq = FreqDist(filtered_words)
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_freq:
                    if len(sentence.split()) < Extension:
                        if sentence not in sentence_scores:
                            sentence_scores[sentence] = word_freq[word]
                        else:
                            sentence_scores[sentence] += word_freq[word]
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary_sentences.sort(key=lambda x: sentences.index(x))
        summary = ' '.join(summary_sentences)
        if sentences[0] not in summary_sentences:
            summary = sentences[0] + ' ' + summary
        return summary

    # Función para estructurar el resumen
    def estructurar_resumen(resumen):
        lineas = resumen.split('. ')  # Dividir por oraciones
        resumen_estructurado = []
        
        for linea in lineas:
            if re.match(r'^\d+', linea.strip()):  # Si la línea comienza con un número
                resumen_estructurado.append(f"- **{linea.strip()}**")  # Usar asteriscos para resaltar
            else:
                resumen_estructurado.append(linea.strip())
        
        return '\n'.join(resumen_estructurado)

    # Leer el archivo PDF
    libro = leer_pdf(uploaded_file)

    # Generar resumen
    resumen = resumir_articulo(libro, num_sentences)

    # Estructurar el resumen
    resumen_estructurado = estructurar_resumen(resumen)

    return resumen_estructurado
