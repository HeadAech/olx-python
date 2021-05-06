import requests
from bs4 import BeautifulSoup
import os
class Offer:
    def __init__(self, id, title, price, sortingPrice, date, city, image, link):
        self.id = id
        self.title = title
        self.price = price
        self.sortingPrice = sortingPrice
        self.date = date
        self.city = city
        self.image = image
        self.link = link


def search(category_link, search_query, sorting):
    offers = []
    search_query = search_query.replace(" ", "-")
    url = category_link + "q-" + search_query + "/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    results = soup.find(id="listContainer")
    tr = results.find_all('tr', class_='wrap')
    print(url)
    
    i = 0
    for el in tr:
        title = el.find('h3', class_='lheight22').find('strong').text
        try:
            price = el.find('p', class_='price').find('strong').text.replace('\n', '')
        except:
            continue
        if "Zamie" in price or "darmo" in price:
            sortingPrice = 0.0
        else:
            sortingPrice = float(price.split('zł')[0][:-1].replace(' ', '').replace(',', '.'))
        city = el.find('td', class_='bottom-cell').find_all('small')[0].text.replace('\n', '')
        date = el.find('td', class_='bottom-cell').find_all('small')[1].text.replace('\n', '')
        image = el.find('img', class_='fleft')
        link = el.find('a', class_='link')['href']
        if image is not None:
            image = el.find('img', class_='fleft')['src']
            # rsps = requests.get(image, stream=True)
            # if not os.path.exists('images/'):
            #     os.makedirs('images/')
            # file = open("images/" + str(i) + ".png", "wb")
            # file.write(rsps.content)
            # file.close()
        else:
            image = ""
            # rsps = requests.get("https://lh3.googleusercontent.com/proxy/RxZazwtrTvFOLHQB4pOoXldzdfQi87NGurL0FSDR4FP846aCSMbW6OMDWIFSD4jN9ay9Ls14IbIJbwUHzX-MyQSgVnRiaCwjKRinkpyZHf8ASNKl65JejlyHtdsVmieLQGYseRpql58-L-A", stream = True)
            # if not os.path.exists('images/'):
            #     os.makedirs('images/')
            # file = open("images/" + str(i) + ".png", "wb")
            # file.write(rsps.content)
            # file.close()
        print(link)
        print(title)
        
        offers.append(Offer(i, title, price, sortingPrice, date, city, image, link))
        i += 1
    
    if sorting == 'Od najmniejszej':
        offers.sort(key=lambda x: x.sortingPrice)
    elif sorting == 'Od największej':
        offers.sort(key=lambda x: x.sortingPrice, reverse=True)
    return offers