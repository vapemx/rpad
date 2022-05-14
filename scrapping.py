from email import header
import requests
from bs4 import BeautifulSoup
import re

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