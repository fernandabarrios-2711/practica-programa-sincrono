
import requests #importar biblioteca que permite hacer peticiones HTTP

url = "https://api.open-meteo.com/v1/forecast" #variable URL que contiene la URL de la API de Open-Meteo

parametros = { # diccionario de parametros que son enviados a la API de Open-Meteo
    "latitude": 19.1738,
    "longitude": -96.1342,
    "current": "temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m",
    "timezone": "America/Mexico_City"
}

respuesta = requests.get(url, params=parametros)
#.get() es un método de la biblioteca requests que permite hacer una petición HTTP GET a la URL especificada, 
# con los parámetros especificados. La respuesta de la API se almacena en la variable respuesta.

print(respuesta.status_code)
print(respuesta.json())
