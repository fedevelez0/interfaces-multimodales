import streamlit as st
from PIL import Image 

st.title("Mi Primera App!!")
st.header("en esta app desarrollare mis aplicaciomes para interfaces mutimodales")
st.write("realizo tanto backend como frontend")
image = Image.open('marco carola.png')

st.image(image, caption='marco carola')
