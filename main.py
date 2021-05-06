import PySimpleGUI as sg
import category
import offer_view
import threading
sg.theme('DarkAmber')

categories = category.fetchCategories()
category_names = ["-"]
for x in categories:
    category_names.append(x.name)
sorting_list = ["Od najmniejszej", "Od największej", "Trafność"]    

layout = [
    [sg.Text("OLX searcher", font='Any 15')],
    [sg.Text("Szukaj: ", font='Any 15'),sg.InputText(key='search', font='Any 15')],
    [sg.Text("Kategoria:", font='Any 15'), sg.Combo(category_names, default_value='-', key='category', font='Any 15')],
    [sg.Text("Sortuj: ", font='Any 15'), sg.Combo(sorting_list, default_value='Trafność', key='sorting', font='Any 15')],
    [sg.Button("Szukaj", font='Any 15')]
]
window = sg.Window('OLX searcher', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Szukaj":
        offer_view.app(values['search'], values['category'], categories, values['sorting'])
window.close()
