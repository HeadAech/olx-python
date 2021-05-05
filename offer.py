import requests
from bs4 import BeautifulSoup

class Offer:
    def __init__(self, title, price, sortingPrice, date, city, image):
        self.title = title
        self.price = price
        self.sortingPrice = sortingPrice
        self.date = date
        self.city = city
        self.image = image


def search(category_link, search_query):
    offers = []
    search_query = search_query.replace(" ", "-")
    url = category_link + "q-" + search_query + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    results = soup.find(id="listContainer")
    tr = results.find_all('tr', class_='wrap')
    
    for el in tr:
        title = el.find('h3', class_='lheight22').find('strong').text
        price = el.find('p', class_='price').text.replace('\n', '')
        sortingPrice = float(price.split('zł')[0][:-1].replace(' ', '').replace(',', '.'))
        city = el.find('td', class_='bottom-cell').find_all('small')[0].text.replace('\n', '')
        date = el.find('td', class_='bottom-cell').find_all('small')[1].text.replace('\n', '')
        image = el.find('img', class_='fleft')['src']
        offers.append(Offer(title, price, sortingPrice, city, date, image))
    return offers

offers = search('https://olx.pl/oferty/', 'guma')

for offer in offers:
    print(offer.title)
    print(offer.price)
    print(offer.sortingPrice)
    print(offer.city)
    print(offer.date)
    print(offer.image)
    print("\n/////")