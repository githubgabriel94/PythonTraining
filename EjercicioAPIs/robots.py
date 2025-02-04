# Implementar un programa de Python para descargar y mostrar el contenido
# de robots.txt para en.wikipedia.org. Nota: Un fichero robots.txt proporciona
# información a los rastreadores de buscadores sobre las páginas o los archivos
# que pueden solicitar o no de tu sitio web y se encuentran en la raiz
# del servidor web.

import requests

url = "https://en.wikipedia.org/robots.txt"

def descargar():
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.text

    except requests.exceptions.RequestException as e:
        print("Error al descargar {url}: {e}")

def mostrar(respuesta):
    if respuesta:
        print(respuesta)
    else:
        print("La respuesta no pudo ser obtenida.")


respuesta = descargar()
mostrar(respuesta)