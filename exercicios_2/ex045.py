# Crie um jogo de Pedra, Papel e Tesoura (Jokenpô) onde o usuário joga contra o computador.
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('Escolha uma opção: ')
pc = randint(0,2)
chute = int(input('''
[0] - PEDRA 
[1] - PAPEL 
[2] - TESOURA
'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 10)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[chute]))
if(pc == 0 and chute == 2) or (pc ==1 and chute == 0) or (pc ==2 and chute ==1):
    print('Computador VENCEU!')
elif (chute == 0 and pc ==2) or (chute ==1 and pc ==0) or (chute ==2 and pc ==1):
    print('Jogador VENCEU!')
elif (chute == 0 and pc ==0) or (chute ==1 and pc ==1) or (chute ==2 and pc ==2):
    print('EMPATE!')
else:
    print('Jogada inválida!')