import base64
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from Algoritmos.LimpiezaDatos import analizar_y_limpiar
from Algoritmos.ResumenDatos import analizar_y_limpiar

st.set_page_config(layout='wide')


@st.cache_data
@st.cache_resource

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
 
img = get_img_as_base64("image.jpg")


st.title('Resumen Financiero') 

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


#INICIO


# Crear una casilla de verificación
Procesar = False

if st.checkbox('Procesar datos'):
    Procesar = True
else:
    Procesar = False

def load_data(path: str):
    data = pd.read_csv(path)
    
    if Procesar:

        Datos_procesados = analizar_y_limpiar(data)
        st.write(analizar_y_limpiar(data))
        print('datos limpiados')
        return Datos_procesados
    else:
        
        return data

uploaded_file = st.file_uploader('Subir Archivo')

if uploaded_file is None:
    st.info('Esperando archivo', icon="❕")
    st.stop()


df = load_data(uploaded_file)
st.dataframe(df)