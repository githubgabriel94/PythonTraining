# Implementar un programa de Python para extraer y mostrar
# todas las etiquetas de encabezado de en.wikipedia.org/wiki/Main_Page.

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

def etiquetasEncabezado():
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        contenido = respuesta.content

        soup = BeautifulSoup(contenido, "html.parser")
        encabezados = soup.find_all(["img"])
        
        for encabezado in encabezados:
            print(encabezado.get_text(strip=True))


    except requests.exceptions.RequestException as e:
        print("Error al descargar {url}: {e}")

etiquetasEncabezado()