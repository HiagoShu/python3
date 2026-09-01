#Escreva um programa que pergunte a quantidade Km percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

dia = int(input('Quantos dias você utilizou o carro?: '))
km = float(input('Quantos km você rodou com o carro?: '))

preco = (60*dia) + (km * 0.15)

print('Você usou o carro por {} dias, e rodou {:.1f}Km, e o preço a pagar é R${:.2f}'.format(dia,km,preco))