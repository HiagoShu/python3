# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#Considere a maioridade 21 
from datetime import date
atual = date.today().year
for pessoa in range(1,8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade < 21:
        print('Essa pessoa ainda não atingiu a maioridade.')
    else:
        print('Essa pessoa já atingiu a maioridade.')
