import base64
import streamlit as st

@st.cache_data
@st.cache_resource

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
 
img = get_img_as_base64("image.jpg")
st.title('My IA App') 

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