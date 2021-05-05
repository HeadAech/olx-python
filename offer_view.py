import PySimpleGUI as sg
import offer
import requests
import os
from PIL import Image
def app(search, chosen_category, categories):
    sg.theme("DarkAmber")
    for category in categories:
        if category.name == chosen_category:
            chosen_category = category.link
    
    if chosen_category == "-":
        chosen_category = 'https://olx.pl/oferty/'
        
    offers = offer.search(chosen_category, search)
    layout = [
        [sg.Text("Oferty")]
    ]
    
    for off in offers:
        
        # im = Image.open(requests.get('https://process.filestackapi.com/AhTgLagciQByzXpFGRI0Az/output=format:png/' + off.image, stream=True).raw)
        group =[
            [sg.Image('images/' + off.title.replace('/', '-') + '.gif'), sg.Text(off.title)],
            [sg.Text("Cena: " + off.price)],
            [sg.Text("Data: " + off.date), sg.Text(", " + off.city)]
            ]
        layout.append(group)
        
    window = sg.Window("Offers", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            # if os.path.exists('images/'):
            #     os.remove('images/')
            break
    window.close()
    
