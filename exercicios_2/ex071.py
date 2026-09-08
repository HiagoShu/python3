# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. 
print('='*30)
print('{:^30}'.format('BANCO DA PICANHA'))
print('='*30)
valor = int(input('Digite o valor a ser sacado: R$'))
total = valor 
céd_atual = 50
tot_céd= 0

while True:
    if total >= céd_atual:
        total -= céd_atual
        tot_céd += 1
    else:
        if tot_céd > 0:
            print(f'Total de {tot_céd} cédulas de R${céd_atual}')
        if céd_atual == 50:
            céd_atual = 20
        elif céd_atual == 20:
            céd_atual = 10
        elif céd_atual == 10:
            céd_atual =1
        tot_céd = 0
        if total == 0:
            break 

print('Obrigado por utilizar o Banco da Picanha! Volte sempre, tenha um bom dia.')