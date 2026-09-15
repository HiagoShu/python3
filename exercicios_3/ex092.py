# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com IDADE) em um dicionário. Se por  acaso a CTPS for diferente de ZERO, o dicionário também receberá o ano da contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

ficha = dict()
ano_atual = date.today().year
ficha['nome'] = str(input('Digite seu nome: '))
ficha['idade'] = ano_atual - int(input('Digite o ano do seu nascimento: '))
ficha['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if ficha['CTPS'] !=0:
    ficha['Ano da Contratação'] = int(input('Ano da contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = ficha['idade'] +(ficha['Ano da Contratação'] +35) - ano_atual

print('-='*30)
print(ficha)
for k,v in ficha.items():
    print(f'{k} tem o valor: {v}')