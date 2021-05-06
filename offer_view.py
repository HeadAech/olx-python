from sys import platform
from time import time
import PySimpleGUI as sg
import offer
import platform
import webbrowser
import threading

def app(search, chosen_category, categories, sorting):
    sg.theme("DarkAmber")
    for category in categories:
        if category.name == chosen_category:
            chosen_category = category.link
    
    if chosen_category == "-":
        chosen_category = 'https://olx.pl/oferty/'
        
    offers = offer.search(chosen_category, search, sorting)
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
        group.append([sg.Text("\n"+off.title, font='Any 21')])
        group.append([sg.Text("Cena: " + off.price, font='Any 15')])
        group.append([sg.Text("Data: " + off.date, font='Any 15')])
        group.append([sg.Text(off.city, font='Any 15')])
        button = sg.InputText(off.link + "\n\n\n", readonly=True, text_color='black', font='Any 14', enable_events=True)
        button.metadata = off.link
        group.append([button])
        
    layout.append([sg.Column(group, size=(1100,600), scrollable=True, vertical_scroll_only=True)])
    
        
    window = sg.Window("Offers", layout)
    timer = 0
    while True:
        # threading.Timer(5.0, app(search, chosen_category, categories, sorting)).start()
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
                
    window.close()
    # if os.path.exists('images/'):
    #     os.remove('images/')

