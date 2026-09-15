# Faça um programa que leia nome e média de um aluno. Guardando também a situação em um dicionário. (média mínima 7)
#No final, mostre o conteúdo da estrutura na tela.

situação = {}
situação['Nome'] = str(input('Nome: '))
situação['media'] = float(input(f'Média de {situação["Nome"]}: '))
if situação['media'] <=7:
    situação['Situação'] = 'Reprovado'
else:
    situação['Situação'] = 'Aprovado'

print(f'Nome é igual a {situação["Nome"]}')
print(f'Média é igual a {situação["media"]}')
print(f'Situação é igual a {situação["Situação"]}')