import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text("Hello world")],
    [sg.InputText()],
    [sg.InputText()],
    [sg.Button("Ok"), sg.Cancel("Cancel")]   
]

window = sg.Window('First app', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered', values[0])
    print('You also entered', values[1])