from email.header import Header
import requests
import json
import urllib.parse
# Se crea una session de HTTP para obtener los datos
s = requests.session()
s.get("https://sia.unal.edu.co/ServiciosApp")

# -------------- Realizando el inicio de sesion --------------

# Obteniendo credenciales de inicio de session
try:
    credsFile = open("keys\sessioninit.json","r")
    creds = json.load(credsFile)
except:
    credsFile.close()
finally:
    credsFile.close()

creds['submit'] = "Iniciar Sesión"

# String necesario para accesar los datos de inicio de session
sessionCreds = urllib.parse.urlencode(creds)
headers = {'Content-type': "application/x-www-form-urlencoded"}

# Se realiza la peticion
r = s.post("https://autenticasia.unal.edu.co/oam/server/auth_cred_submit", sessionCreds, headers=headers)

# Placeholder para verificar inicio de sesion
if r.text.find("Usuario y clave incorrecta.") == -1:
    # Ni modo, no encontre otra forma de verificar si se inicio con exito session o no :(
    print("Ingreso con exito.")
else:
    print("Usuario y/o clave incorrecta")