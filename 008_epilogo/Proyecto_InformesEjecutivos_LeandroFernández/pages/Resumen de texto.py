import base64
import streamlit as st
from Algoritmos.Resumen import resumir_articulo, resumir_articulo_texto, resumir_articulo_pdf

@st.cache_data
@st.cache_resource

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
 
img = get_img_as_base64("image.jpg")
st.title('Resumen de texto')

#Editar background principal y del sidebar
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: rgb(89,89,89);
    background: linear-gradient(0deg, rgba(89,89,89,1) 0%, rgba(64,64,64,1) 31%, rgba(38,38,38,1) 69%, rgba(13,13,13,1) 100%);
}}


[data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: fixed;

}}

[data-testid="stBaseButton-headerNoPadding"] {{
background: rgb(89,89,89);
padding: 15px;


}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Instrucciones de uso
st.markdown("### Instrucciones:")
st.write("""
1. Introduce una URL en la primera caja de texto si deseas cargar un texto desde internet.
2. Si no deseas usar una URL, introduce tu propio texto en la segunda caja de texto.
3. Presiona el botón correspondiente para guardar tu URL o texto.\n
4. El texto procesado aparecerá debajo de la segunda caja de texto.
5. Puedes ajustar en la barra la extensión de tu resumen pero ten en cuenta que eso tendra un limite en base a la información entregada.
""")

uploaded_file = st.file_uploader("Selecciona un archivo PDF", type=["pdf"])

if uploaded_file is not None:
        # Mostrar el nombre del archivo
        st.success(f"Archivo cargado: {uploaded_file.name}")

# Centrar el contenido
st.markdown('<div class="centered">', unsafe_allow_html=True)

#Slide para definir extension del resumen
Extension_slide = summary_length = st.slider("Define la extensión del resumen", min_value=20, max_value=1000, value=40)

# Variable para almacenar el URL y el texto
url = ""
text = ""

# Muestra un botón para procesar el archivo
if st.button("Procesar PDF"):
    
    try:
        # Llama a la función para resumir el artículo
        processed_pdf_text = resumir_articulo_pdf(uploaded_file, Extension_slide)  # Asegúrate de que la función acepte un archivo como entrada
        st.success("PDF procesado con éxito:")  # Mensaje de éxito
        st.write(processed_pdf_text)  # Muestra el texto procesado
    except AttributeError as e:
             st.success('Hubo un error al procesar el documento, puede que la casilla este vacia o el pdf no sea legible.')

             
# Cuadro pequeño para URL
url_input = st.text_area("Ingresa el URL:", height=10, key="url_input", label_visibility="visible")
if st.button("Procesar URL"):
    url = url_input  # Guardamos el URL en la variable
    processed_url_text = resumir_articulo(url, Extension_slide)  # Llama a la función
    st.success("URL procesada con éxito:")  # Mensaje de éxito
    st.write(processed_url_text)  # Muestra el texto procesado

# Cuadro de entrada de texto centrado
user_input = st.text_area("Ingresa el texto:", height=200, key="input", label_visibility="visible")
if st.button("Procesar texto"):
    text = user_input  # Guardamos el texto en la variable
    processed_text = resumir_articulo_texto(text, Extension_slide)  # Llama a la función
    st.success("Texto procesada con éxito:")  # Mensaje de éxito
    st.write(processed_text)  # Muestra el texto procesado


# Cerrar el div centrado
st.markdown('</div>', unsafe_allow_html=True)
