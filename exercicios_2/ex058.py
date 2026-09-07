# Melhora o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

vezes = 0
palpite = 0
computador = randint(0,10)
while palpite != computador:
    palpite = int(input('Digite um número entre 0 e 10: '))
    vezes += 1
    if palpite < computador:
        print('Mais... Tente novamente.')
    elif palpite > computador:
        print('Menos... tente novamente.')
print('Parabéns! Você acertou o número {} em {} tentaivas.'.format(computador, vezes))