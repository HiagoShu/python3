#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Dica do Hiago: Use random
import random
print('Estou pensando em um número entre 1 e 5, consegue adivinhar?')
num = random.randint(1,5)
chute = int(input('Digite aqui o número que você acha que eu pensei: '))

if chute == num:
    print('Você acertou!')
else:
    print('Você errou! O número é {}'.format(num))