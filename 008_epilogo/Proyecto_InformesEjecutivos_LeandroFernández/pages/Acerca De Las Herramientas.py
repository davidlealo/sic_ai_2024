import json
import base64
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

@st.cache_data
@st.cache_resource

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
 
img = get_img_as_base64("image.jpg")

def load_gif (url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



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

st.markdown(
    """
    <style>
    .text-container {
        position: relative; /* Posición relativa para el contenedor */
        height: 400px; /* Altura del contenedor */
    }
    .text-area {
        position: absolute; /* Posición absoluta para el cuadro de texto */
        top: -420px; /* Ajusta la distancia desde la parte superior */
        left: -700px; /* Ajusta la distancia desde la izquierda */
        width: 1000px; /* Ancho del cuadro de texto */
        height: 300px; /* Altura del cuadro de texto */
        padding: 10px; /* Espaciado interno */
        border: 5px solid grey; /* Borde verde */
        border-radius: 8px; /* Bordes redondeados */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor para el cuadro de texto
st.markdown('<div class="text-container">', unsafe_allow_html=True)
st.markdown('<textarea class="text-area" placeholder="La herramienta de resumen de texto permite de manera sencilla extraer los aspectos mas relevantes de un escrito, para ello puedes cargar en PDF o inserter un texto a mano."></textarea>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contenedor para el cuadro de texto
st.markdown('<div class="text-container">', unsafe_allow_html=True)
st.markdown('<textarea class="text-area" placeholder="La herramienta de resumen de texto permite de manera sencilla extraer los aspectos mas relevantes de un escrito, para ello puedes cargar en PDF o inserter un texto a mano."></textarea>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contenedor para el cuadro de texto
st.markdown('<div class="text-container">', unsafe_allow_html=True)
st.markdown('<textarea class="text-area" placeholder="La herramienta de resumen de texto permite de manera sencilla extraer los aspectos mas relevantes de un escrito, para ello puedes cargar en PDF o inserter un texto a mano."></textarea>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
