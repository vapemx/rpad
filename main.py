from io import open
from sqlite3 import DatabaseError
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


def main():
    soups = []
    linkDB = {}

    links = getLinks()
    for link in links:
        soups.append(getWeb.get(link))

    for i in range(len(links)):
        linkDB[links[i]] = soups[i]
    print(linkDB)



if __name__ == "__main__":
    main()