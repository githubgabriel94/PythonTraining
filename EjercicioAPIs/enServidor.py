# Implementar un programa Python para probar si una página determinada 
# se encuentra o no en el servidor.

import requests

url = input("Introduce la url del servidor que desea comprobar: ")

respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("La página se encuentra en el servidor.")
else: print("La página no se encuentra en el servidor.")