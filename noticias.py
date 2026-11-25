
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def consultar_noticias():

    API_KEY = os.getenv("NEWSDATA_API_KEY")

    if not API_KEY:
        raise ValueError("No se encontro la API KEY")

    url = "https://newsdata.io/api/1/latest"

    parametros = {
        "apikey": API_KEY,
        "language": "es"
    }

    respuesta = requests.get(url, params=parametros)

    respuesta.raise_for_status()

    datos = respuesta.json()

    # Revisar qué respondió la API
    print("\nRESPUESTA DE NEWSDATA")
    print("Estado:", datos.get("status"))
    print("Total de resultados:", datos.get("totalResults"))

    # Comprobar si existe la lista de noticias
    noticias = datos.get("results", [])

    return noticias
