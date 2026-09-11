#Crie um programa onde o usuário possa digitar VÁRIOS valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


#TO DO - Acrescentar a exibição de todos os valores únicos digitados em ordem crescente.
lista = []
while True:
    num=(int(input('Digite um número: ')))
    if num not in lista:
        lista.append(num)
    else:
        print('Esse valor já está na lista. Escreva outro.')
    #Opção de parar ou não.
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if opcao =='N':
        break
lista.sort()
print(f'A ordem crescente dos números que você digitou é: {lista}')