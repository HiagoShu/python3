#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade <18:
        print('NÃO VOTA')
    elif idade >= 18 and idade <65:
        print('VOTO OBRIGATÓRIO')
    else:
        print('VOTO OPCIONAL')

#Programa principal
n = int(input('Digite o ano em que você nasceu: '))
voto(n)