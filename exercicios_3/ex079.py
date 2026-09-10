#Crie um programa onde o usuário possa digitar VÁRIOS valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


#TO DO - Acrescentar a verificação se o número JÁ está na lista, não ser adicionado.
lista = []
while True:
    lista.append(int(input('Digite um número: ')))



    #Opção de parar ou não.
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    if opcao =='N':
        break
