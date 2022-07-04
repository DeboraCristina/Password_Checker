import PySimpleGUI as pg

pg.theme('Reddit')

row01 = [ pg.Column([[pg.Input(key='password', size=(20, 1))]]), pg.Column([[pg.Button(key='check')]]) ]
row02 = [ pg.Column([[ pg.Text(key='erro', text='', justification='center', ) ]], element_justification='c', justification='center', expand_x=True, ) ]
layout=[
    row01,
    row02
]

win = pg.Window('Password Checker', layout)

while True:
    event, value = win.read()

    if event == pg.WINDOW_CLOSED:
        break

win.close()
