# import os es una instrucción de Python que importa el módulo os, que proporciona funciones para interactuar con el sistema operativo, para realizar operaciones como:
# """"Trabajar con rutas de archivos y directorios.
#     Consultar variables de entorno.
#     Comandos del sistema operativo.""""
 
import pyshorteners.shorteners
import streamlit as st

def validar_url(url): 
  if not url or len(url.strip()) <= 6: 
        return ValueError("Lo siento la URL es demasiado corta, intenta de nuevo! ")

  if not (url.startswith("http://") or url.startswith("https://")): 
        return ValueError("Lo sentimos, la URL debe comenzar con 'http://' o 'https://'")

        return True

def acortar_url(url): 
    try: 
        # Inicializamos el acortador
        s = pyshorteners.Shortener()

        url_corta = s.tinyurl.short(url)
        return url_corta
          
    except Exception as e: 
       return ValueError("Error al acortar la URL")
 

#3 Creamos la app web con Streamlit
st.set_page_config(page_title="Acortar URL", page_icon="✂️", layout="centered")
st.image("images/background.jpg", use_container_width=True)
st.title("Acortar URL")

url = st.text_input("Ingrese la URL")

if st.button("Generar la URL"):
    try:
        validar_url(url)
        resultado = acortar_url(url)
        st.success("URL corta: ", resultado)

    except ValueError as e: 
       st.error(str(e))