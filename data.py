from bs4 import BeautifulSoup
import requests


class Category:
    def __init__(self, name, link):
        self.name = name
        self.link = link


def fetchCategories():
    url = "https://www.olx.pl"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id="searchmain-container")
    maincat = results.find_all('div', class_='item')
    categories = []
    for div in maincat:
        name = div.find('a', class_="link").text.rstrip("\n")
        link = div.find('a', class_="link")['href']
        categories.append(Category(name, link))
        
    return categories