from clima import consultar_clima #importar nuestra funcion

def main():
    clima=consultar_clima() #llamar a la funcion
    
    print("CLIMA EN VERACRUZ, VERACRUZ")
    print(f"Temperatura: {clima['temperature_2m']} °C")
    print(f"Humedad: {clima['relative_humidity_2m']} %")
    print(f"Sensación térmica: {clima['apparent_temperature']} °C")
    print(f"Viento: {clima['wind_speed_10m']} km/h")
    print(f"Precipitación: {clima['precipitation']} mm")
    
if __name__ == "__main__": 
    #indica al programa que si este archivo es ejecutado directamente, se ejecute la funcion main()
    main()

