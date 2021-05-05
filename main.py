import PySimpleGUI as sg
import category
import offer

sg.theme('DarkAmber')

layout = [
    [sg.Text("Hello world")],
    [sg.InputText()],
    [sg.InputText(key='-IN-')],
    [sg.Button("Ok"), sg.Cancel("Cancel")]
]

categories = category.fetchCategories()

for category in categories:
    layout.append([sg.Text(category.name)])

window = sg.Window('First app', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered', values[0])
    print('You also entered', values['-IN-'])
window.close()
