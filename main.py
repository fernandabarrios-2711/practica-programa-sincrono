
from clima import consultar_clima
from noticias import consultar_noticias

def main():

    clima = consultar_clima()

    print("CLIMA EN VERACRUZ, VERACRUZ")
    print(f"Temperatura: {clima['temperature_2m']} °C")
    print(f"Humedad: {clima['relative_humidity_2m']} %")
    print(f"Sensación térmica: {clima['apparent_temperature']} °C")
    print(f"Viento: {clima['wind_speed_10m']} km/h")
    print(f"Precipitación: {clima['precipitation']} mm")

    lista_noticias = consultar_noticias()

    print("\nNOTICIAS DE TECNOLOGÍA EN MÉXICO Y CHINA")
    print("Tipo de dato:", type(lista_noticias))
    print("Cantidad de noticias:", len(lista_noticias))

    if not lista_noticias:
        print("No se encontraron noticias.")

    else:
        for numero, noticia in enumerate(lista_noticias, start=1):
            print(f"\nNOTICIA {numero}")
            print("-" * 50)
            print(f"Título: {noticia.get('title', 'Sin título')}")
            print(f"Descripción: {noticia.get('description', 'Sin descripción')}")


if __name__ == "__main__":
    main()
