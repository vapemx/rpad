from io import open
import re
import getWeb


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
    pattern = "(http[s]*://[a-z]+.[a-zA-Z0-9]+.[a-z]{2,}/*)"
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
    x = input("¿Desea agregar[s/N]?: ")
    if x == "S" or x == "s":
        links = addLinks(links)
        print("Esto son los link a utilizar: ")
        print("\n")
        print(links)


    soups = []
    linkDB = {}

    
    for link in links:
        soups.append(getWeb.get(link))

    for i in range(len(links)):
        linkDB[links[i]] = soups[i]



if __name__ == "__main__":
    main()