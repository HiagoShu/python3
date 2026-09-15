# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um DICIONÁRIO e todos os dicionários em uma LISTA. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.
galera = list()
pessoa = {}
soma = media =0
mulher = list()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Qual a idade? '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opcao in 'SN':
            break 
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break



print('-='*30)
print(galera)
print(f' A) Pessoas cadastradas: {len(galera)} pessoas')

media = soma //len(galera)
print('-='*30)
print(f'B) A média das idades é de: {media}')
print('-='*30)
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]} , ',end='')
print()
print('-='*30)
print('D) Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ')
        for k,v in p.items():
            print(f' {k}  =  {v}; ',end='')
        print() 
print('<< ENCERRADO >>')