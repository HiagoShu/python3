# Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, mostre: 

#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    # valores.append(int(input('Digite um número: '))) #-> Maneira do professor
    opcao = ' '
    while opcao not in 'SsNn':
        opcao =str(input('Você quer continuar? [S/N]').strip().upper()[0])
    if opcao == 'N':
        break

    #Controle de continuação do professor.
    # resp = str(input('Quer continuar? [S/N] '))
    # if resp in 'Nn':
    #       break
print('-='*30)
print(f'A quantidade de números digitados é de {len(lista)}')
lista.sort(reverse=True)
print(f'A lista de valores em forma decrescente é esta: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 NÃO está na lista')