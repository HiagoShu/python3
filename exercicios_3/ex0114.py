#Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import webbrowser
url = "http://pudim.com.br"

try:
    webbrowser.open(url)
    print("O site Pudim está acessível!")
except Exception as e:
    print("O site Pudim não está acessível. Erro:", e)