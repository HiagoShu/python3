# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam MAIS de 1000 reais.
# C) Qual é o nome do produto mais barato.
total =0
totmil = 0
menor = 0 # C
cont = 0  # C

print('-='*20)
print('MERCADÃO DO JORJÃO')
print('-='*20)
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: '))
    total =+ preco 
    cont +=1 # C
    if preco >1000:
        totmil +=1
    if cont == 1:
        menor = preco
    else:
        if preco <menor:
            menor = preco
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer passar mais um produto?[S/N] ')).strip().upper()[0]
    if opcao =='N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra deu R${total:.2f}')
print(f'A quantidade de produtos com valor maior de R$1000.00 foi de {totmil}')
print(f'O produto mais barato custa R${menor:.2f}')
