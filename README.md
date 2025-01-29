
#  Acortar URL ✨

Esta es una aplicación web simple para acortar URLs utilizando Python y Streamlit. Con esta herramienta, los usuarios pueden ingresar una URL larga y generar una versión corta mediante la API de TinyURL


## Características

Validación de URL: Asegura que la URL ingresada sea válida y comience con http:// o https://.

Interfaz amigable: La aplicación está diseñada con Streamlit para una experiencia de usuario intuitiva.

Mensajes de error: Se notifican errores si la URL es demasiado corta o no tiene el formato adecuado.
##  Tecnologia utilizada

- Python: Lenguaje de programación principal.
- Streamlit: Framework para crear aplicaciones web interactivas.
- Pyshorteners: Biblioteca para acortar URLs mediante APIs de servicios populares.

## Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1 - Clona este repositorio:

git clone https://github.com/tu_usuario/acortar-url.git

2 - Navega al directorio del proyecto:

cd acortar-url

3 - Crea un entorno virtual (opcional, pero recomendado):

python -m venv venv
source venv/bin/activate  # En Linux/Mac
.\venv\Scripts\activate # En Windows

4 - Instala las dependencias:

pip install -r requirements.txt

5 -  la aplicación:

streamlit run app.py

6 - Abre la aplicación en tu navegador:Ve a http://localhost:8501.
## Usage
Ingresa una URL en el campo de texto.

Haz clic en el botón Generar la URL.

Si la URL es válida, se mostrará una versión corta de la URL. Si no, se mostrará un mensaje de error indicando el problema.


## Authors

[@milagrosCabrera23]https://github.com/MilagrosCabrera23)
