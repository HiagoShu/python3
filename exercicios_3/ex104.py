# Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante á função input do Python, só que fazendo a validação para aceitar apenas um valor numérico. 

#Ex: n = leiaInt('Digite um n')
def linha():
    print('-='*30)

def leiaInt(msg):
    ok = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
        if ok:
            break 
    return num



#Programa principal
linha()
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')