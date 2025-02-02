# Implementar una función que reciba una cadena y compruebe,
# mediante una expresión regular, si la cadena es una cuenta de correo válida.

import re

correo = input("Introduce una dirección de correo (email): ")

def esCorreo(correo):
    if re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$', correo):
        print("Su correo es válido.")
    else: 
        correo = input("La dirección introducida no es válida, intentelo de nuevo: ")
        esCorreo(correo)
    
esCorreo(correo)

# Implementar una función que reciba una cadena y compruebe, mediante una
# expresión regular, si la cadena es una url válida.

print("---------------------------------------------------------")

website = input("Introduce la url de una página web: ")

def esWeb(web):
    if re.match('^(https?://)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(/.*)?$', web):    
        print("La website introducida es válida.")
    else: 
        web = input("La website introducida introducida no es válida, intentelo de nuevo: ")
        esWeb(web)

esWeb(website)