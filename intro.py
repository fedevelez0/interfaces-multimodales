import streamlit as st
from PIL import Image 

st.title("Mi Primera App!!")
st.header("en esta app desarrollare mis aplicaciomes para interfaces mutimodales")
st.write("realizo tanto backend como frontend")
image = Image.open('marco carola.png')

st.image(image, caption='marco carola')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usamos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("las Interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('estoy de acuerdo')
  if resp:
    st.write('correcto')

with col2:
  st.subheader("esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('visual', 'auditiva', 'tactil'))
  if modo == 'visual':
    st.write('la vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('la audicion es fundamental para tu interfaz')
  if modo == 'tactil':
    st.write('El tacto es fundamental para tu interfaz')
