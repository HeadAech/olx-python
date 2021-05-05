import PySimpleGUI as sg
import offer
import requests
import os
from PIL import ImageTk, Image
def app(search, chosen_category, categories):
    sg.theme("DarkAmber")
    for category in categories:
        if category.name == chosen_category:
            chosen_category = category.link
    
    if chosen_category == "-":
        chosen_category = 'https://olx.pl/oferty/'
        
    offers = offer.search(chosen_category, search)
    layout = [
        [sg.Text("Oferty", font='Any 20')]
    ]
    group = []
    for off in offers:
        # image = Image.open('images/' + off.title.replace('/', '-') + '.gif')
        # cwd = os.getcwd()
        # fname = 'images/' + str(off.id) + '.png'

        # with open(fname, 'rb') as fh:
        #     image1 = fh.read()
        # im = Image.open(requests.get('https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/' + off.image, stream=True).raw)
        # lay =[
        #     [sg.Text(off.title)],
        #     [sg.Text("Cena: " + off.price)],
        #     [sg.Text("Data: " + off.date), sg.Text(", " + off.city)]
        #     ]
        group.append([sg.Text(off.title, font='Any 15')])
        group.append([sg.Text("Cena: " + off.price, font='Any 15')])
        group.append([sg.Text("Data: " + off.date, font='Any 15')])
        group.append([sg.Text(off.city + "\n\n\n", font='Any 15')])
        
    layout.append([sg.Column(group, size=(1100,800), scrollable=True)])
    
        
    window = sg.Window("Offers", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            
            break
    window.close()
    # if os.path.exists('images/'):
    #     os.remove('images/')
