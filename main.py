import PySimpleGUI as sg
import category
import offer_view
sg.theme('DarkAmber')

categories = category.fetchCategories()
category_names = ["-"]
for x in categories:
    category_names.append(x.name)
    

layout = [
    [sg.Text("OLX searcher")],
    [sg.Text("Szukaj: "),sg.InputText(key='search')],
    [sg.Text("Kategoria:"), sg.Combo(category_names, default_value='-', key='category')],
    [sg.Button("Szukaj")]
]
window = sg.Window('OLX searcher', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Szukaj":
        offer_view.app(values['search'], values['category'], categories)
window.close()