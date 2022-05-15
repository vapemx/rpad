from io import open
import re
import scrapping
from os import link, remove, listdir


def getLinks(links):
    with open("links.txt") as fileLinks:
        lines = fileLinks.readlines()
        for line in lines:
            if line in links:
                continue
            line = line.split("\n")
            links.append(line[0])

    return links


def addLinks(links):
    pattern = "(http[s]?://\w+.\w+.\w{2,}/*)"
    newLink = input("Escriba el link a agregar con prefijo http al inicio: ")
    check = re.findall(pattern, newLink)
    if not check:
        print("Formato de link erróneo. ")
        addLinks()
    else:
        with open("links.txt", "a") as fileLinks:
            fileLinks.write("\n"+newLink)

    return getLinks(links)


def main():
    links = []
    links = getLinks(links)
    print("Esto son los link a utilizar: ")
    print("\n")
    print(links)
    print("\n")
    x = input("¿Desea agregar[s/N]?: ").lowercase()
    if x == "s":
        links = addLinks(links)
        print("Esto son los link a utilizar: ")
        print("\n")
        print(links)
    else:
        pass
    
    #Buscar links info
    for link in links:
        match = re.findall("(wikipedia)", link)
        if match:
            wikiURL = link
    
    #Buscamos la info
    name, age, bornPlace, podiums, victories, years = scrapping.personal_info(wikiURL)

    #Buscamos sus RRSS
    redes = scrapping.redes(wikiURL)

    #Buscamos link del calendario
    for link in links:
        match = re.findall("(calendar)", link)
        if match:
            calendarURL = link

    #Buscamos los siguientes eventos
    nextevents = scrapping.event(calendarURL)

    #Buscar link para noticias e imágenes
    for link in links:
        match = re.findall("(noticias)", link)
        if match:
            newsUrl = match[0][0]

    #Descargamos las imágenes
    scrapping.images(newsUrl)

    #Buscar las noticas
    news = []
    for link in newsUrl:
        news.append(scrapping.titulares(link))


    #Fin: Se le pregunta al usuario si quiere eliminar excel generado
    ls = listdir()
    for i in ls:
        match = re.findall("(\w+.xlsx)", i)
        if match:
            xlxsName = match[0][0]

    x = input(f"¿Desea eliminar el archivo {xlxsName}? [s/N]: ")
    if x == "S" or x == "s":
        remove(xlxsName)
    else:
        pass


if __name__ == "__main__":
    main()
