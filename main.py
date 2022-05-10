from io import open
import re
import getWeb


def getLinks():
    links = []

    with open("links.txt") as fileLinks:
        lines = fileLinks.readlines()
        for line in lines:
            if line == "\n":
                continue
            else:
                links.append(line)
    print(links)

    return links


def addLinks():
    pattern = "([a-z]+.[a-zA-Z0-9]+.[a-z]{2,}/*)"
    newLink = input("Escriba el link a agregar: ")
    check = re.findall(pattern, newLink)
    if not check:
        print("Formato de link erróneo. ")
        addLinks()
    else:
        with open("links.txt", "w") as fileLinks:
            fileLinks.write("\n".join(newLink))

    return getLinks()


def main():
    links = getLinks()
    print("Esto son los link a utilizar: ")
    print(links)
    x = input("¿Desea agregar[s/N]?: ")
    if x == "S" or x == "s":
        links = addLinks()

    soups = []
    linkDB = {}

    
    for link in links:
        soups.append(getWeb.get(link))

    for i in range(len(links)):
        linkDB[links[i]] = soups[i]
    print(linkDB)



if __name__ == "__main__":
    main()