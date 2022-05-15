import requests
from bs4 import BeautifulSoup
import re
from datetime import date


def titulares(url):
    patron_web = "(?<=\")(https.*?)(?=\")" 
    patron_titulares = "(?<=\>)(.*?)(?=\<)" 
    webpage_response = requests.get(url)

    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")

    links = []
    titulares_links = soup.find_all("h2")

    for a in titulares_links:
        a = str(a)
        link = re.findall(patron_web, a)
        links.append(link[0])

    titulares = []    
    for link in links:
        webpage = requests.get(link)
        titular = BeautifulSoup(webpage.content, "html.parser")
        nombre_titular_raw = titular.find("title")
        titulares.append(nombre_titular_raw)

    nombre_titulares = []
    for titular in titulares:
        titular = str(titular)
        nombre_titular = re.findall(patron_titulares, titular)
        nombre_titulares.append(nombre_titular[0])

    headers = nombre_titulares[:3]
    
    return headers


def personal_info(url):
    webpage_response = requests.get(url)

    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    today = date.today()

    infobox = soup.find(class_="infobox")
    infobox = str(infobox)
    infobox = infobox.split("<tr>")[4:]

    for element in infobox:
        matchName = re.findall(">Nombre<", element)
        if matchName:
            name = element.split("\n")[1].split("<")[0]

        matchBorn = re.findall(">Nacimiento<", element)
        if matchBorn:
            bornPlace = element.split("\n")[1].split("<")[2]
            bornPlace = re.findall('title="(\w+)', bornPlace)[0]
            bornDate = element.split("\n")[1].split("<")[0]

        matchActive = re.findall(">Años<", element)
        if matchActive:
            active = element.split(">")
            for x in active:
                match = re.findall("(\d{4})", x)
                if match:
                    active = int(match[0])
                    years = today.year - active
                    years = str(years)
                    
        matchPodiums = re.findall(">Podios<", element)
        if matchPodiums:
            podiums = element.split("\n")[1].split("<")[0]

        matchWins = re.findall(">Victorias<", element)
        if matchWins:
            victorias = element.split("\n")[1].split("<")[0]            

    return name, bornDate, bornPlace, podiums, victorias, years