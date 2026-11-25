
import requests
def consultar_clima(): #crear funcion para consultar el clima
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": 19.1738,
        "longitude": -96.1342,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m",
        "timezone": "America/Mexico_City"
    }
    respuesta = requests.get(url, params=parametros, timeout=10) 
    # solicitud HTTP, timeout significa que tenemos un limite de espera de 10 segundos
    respuesta.raise_for_status() #comprueba que la solicitud HTTP tuvo exito
    datos = respuesta.json() # .json, metodo para convertir la respuesta JSON en un diccionario de python
    clima_actual = datos["current"] #acceder solo al diccionario "current" que contiene la informacion del clima actual
    return clima_actual #devolver el resultado de la funcion, que es un diccionario con la informacion del clima actual
