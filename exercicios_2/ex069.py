# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A ) Quantas pessoas tem mais de 18 anos.
# B ) Quantos HOMENS foram cadastrados. 
# C ) Quantas mulheres tem menos de 20 anos.
mais_dezoito = 0
homem = 0
mulher_menos_vinte = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-='*20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >=18:
        mais_dezoito +=1
    if sexo in 'Mm':
        homem +=1
    if sexo in 'Ff' and idade <20:
        mulher_menos_vinte +=1
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer cadastrar mais uma pessoa? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'A quantidade de pessoas com mais de 18 anos de idade é de {mais_dezoito}')
print(f'A quantidade de homens cadastrados foi de {homem}')
print(f'A quantidade de mulheres cadastradas com menos de 20 anos é de {mulher_menos_vinte}')