# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
while True:
    n = int(input('Digite um número: '))
    pc = randint(0,10)
    resultado = n + pc
    opcao = ' '
    while opcao not in 'PpIi': #validação: se é P ou I
        opcao = str(input('Escolhe PAR ou ÍMPAR? [P/I]')).strip().upper()[0]
    print(f'Você jogou {n} e o computador jogou {pc}. O resultado é de {resultado}')
    if opcao =='P':
        if resultado %2 ==0:
            print('Você ganhou!')
            vitoria+=1
        else:
            print('Você perdeu!')
            break
    if opcao == 'I':
        if resultado %2 ==1:
            print('Você ganhou!')
            vitoria +=1
        else:
            print('Você perdeu!')
            break

print(f'Você conquistou {vitoria} vitórias')