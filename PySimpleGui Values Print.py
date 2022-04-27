import PySimpleGUI as sg
layout = [[sg.InputText('', size=(10,1), key='input_height')],
          [sg.Submit()]]
window = sg.Window('Window Title', layout)
while True:
    event, values = window.Read()
    if event == 'Submit':
        height = int(values['input_height'])
        print (height)
