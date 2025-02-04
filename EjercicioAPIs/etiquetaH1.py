# Implementar un programa Python para extraer la etiqueta h1 de example.com.

import requests
import re
#from bs4 import BeautifulSoup

url = "http://example.com"

def etiquetaH1():
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        contenido = respuesta.text
        match = re.search(r"<h1>(.*?)</h1>", contenido, re.IGNORECASE)
        #soup = BeautifulSoup(contenido, "html.parser")
        #match = soup.find("h1")
        
        if match: 
            h1 = match.group(1)
            print("La etiqueta <h1> contiene; ", h1)
        else:
            print("No se pudo encontrar ninguna etiqueta <h1> en la página.")


    except requests.exceptions.RequestException as e:
        print("Error al descargar {url}: {e}")

etiquetaH1()