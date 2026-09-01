# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora de se alistar
#  ou se já passou do tempo do alistamento.

#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade < 18:
    print('Você ainda vai se alistar ao serviço militar. Faltam {} anos para o alistamento.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar ao serviço militar!')
else:
    print('Você já passou do tempo de alistamento. Já se passaram {} anos'.format(idade - 18))