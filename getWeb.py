import requests
from bs4 import BeautifulSoup as bs

def get(url):
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

    return soup.prettify