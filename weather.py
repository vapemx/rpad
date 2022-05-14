'''
Se va a obtener los 3 eventos siguientes y su clima.
El problema está en que a veces entre el primer evento y el tercero es un més de diferencia.
Hay que buscar solución a eso.
'''

import requests
import json
from datetime import datetime

listakey = []
listavalue = []
listadia = []

Latitud = "25.767"
Longitud = "-100.200"
appid = "a3a7114576a3b54a0a02aee0bb777dea"
page=requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + Latitud + "&lon=" + Longitud + "&exclude=minutely,hourly&units=metric&appid=" + appid)
print()
print(f"The code of the request is: {page.status_code}")

weatherData = json.loads(page.content)

for x, y in weatherData.items():
    if x == "daily":
        for i in y[0:1]:
            fecha = int(i['dt'])
            dia = datetime.utcfromtimestamp(fecha).strftime("%d-%m-%Y")
            listadia.append(dia)
            for key in i['temp']:
                listakey.append(key)
                listavalue.append(i['temp']['day'])
                listavalue.append(i['temp']['eve'])
                listavalue.append(i['temp']['night'])
                listavalue.append(i['temp']['min'])
                listavalue.append(i['temp']['max'])

Datos= listavalue
Resultado = []
for repetido in Datos:
    if repetido not in Resultado:
        Resultado.append(repetido)

print("                                         Dia   Tarde   Noche  MINIMA  MAXIMA")
print(f"Las temperaturas para el 13 de Mayo son:{Resultado}")
print()


'''
ESTO LO REVISARE DESPUES PORQUE IMPRIME LAS LISTAS MUCHISIMAS VECES (ATTE YAHIR)

print(listakey)
print(listavalue)
print(listadia)
input()
'''

                
