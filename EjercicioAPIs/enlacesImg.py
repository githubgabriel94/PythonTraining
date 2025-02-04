# Implementar un programa de Python para extraer y mostrar todos 
# los enlaces de imágenes de en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer).

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)"

def enlacesImg():
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        contenido = respuesta.content

        soup = BeautifulSoup(contenido, "html.parser")
        imagenes = soup.find_all("img")

        for imagen in imagenes:
            fuente = imagen.get("src")
            if fuente:
                print(fuente)

    except requests.exceptions.RequestException as e:
        print("Error al descargar {url}: {e}")

enlacesImg()