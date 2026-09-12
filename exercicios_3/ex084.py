# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final , mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves 
pessoas = list()
dado = list()
maior = menor = 0
while True:
    nome = (str(input('Cadastre uma pessoa: ')))
    dado.append(nome)
    peso = (float(input('Diga o peso da pessoa em kg: ')))
    dado.append(peso)
    #Lógica de verificação de peso
    if len(pessoas) ==0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] <menor:
            menor = dado[1]
    #Adicionando a lista principal
    pessoas.append(dado[:])
    dado.clear()

    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Você quer Cadastrar mais uma pessoa? [S/N]').strip().upper()[0]
    if opcao == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')
print()