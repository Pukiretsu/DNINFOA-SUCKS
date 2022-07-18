import json
import urllib.parse

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
print(type(sessionCreds))
