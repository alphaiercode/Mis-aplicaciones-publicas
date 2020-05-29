import requests
import json

print("########################################################################")
print("#                                                                      #")
print("#                   G E O L O C A L I Z A D O R                        #")
print("#                                                                      #")
print("########################################################################")

# URL de laAPI
api_url = "http://ip-api.com/json/"

# Definimos los parametros de respuesta.
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
    # Nos conectamos con la API.
    res = requests.get(api_url+ip, data=data)
    # Obtenemos y procesamos la respuesta JSON.
    api_json_res = json.loads(res.content)
    return api_json_res

if __name__ == '__main__':
    # Solicitamos la entrada.
    ip = input("Ingrese la direccion IP: ")

    # Llamamamos a la funcion ip_scraping y mostramos los resultados.
    par = parametros.split(",")
    for x in par:
        print(x.upper(), ":")
        print(ip_scraping(ip)[x])
        print("\n")
