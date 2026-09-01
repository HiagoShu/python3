# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

#MODO COM MÓDULO CALENDAR
#import calendar 
#num = int(input('Digite aqui um ano para que eu verifique se é bissexto ou não: '))
#ano = calendar.isleap(num)

#if (ano == True):
#    print('Sim! Seu ano é bissexto')
#else:
#    print('Não, seu ano não é bissexto.')

#MODO NA MARRA
#Regra, ocorre de 4 em 4 anos (divisível por 4), e se terminar em 00 NÃO PODE ser divísível por 100 E DEVE ser divisível por 400.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analizar o ano atual: '))
if ano ==0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100!= 0 or ano % 400 ==0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))
