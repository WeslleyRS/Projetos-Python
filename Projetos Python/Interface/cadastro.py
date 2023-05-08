from PySimpleGUI import PySimpleGUI as sg

# layout

sg.theme('Dark')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Confirmar')],
    [sg.Button('Cancelar')],
]

# janela

janela = sg.Window('Tela de Login', layout)

# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos =='cancelar':
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'weslley' and valores['senha'] == '32902787':
            print('Seja Bem-vindo!')