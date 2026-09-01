#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = valor / (anos * 12)

if prestacao > (salario *0.3):
    print('Empréstimo negado! A prestação de R${:.2f} excede 30 por cento do seu salário! Sinto muito'.format(prestacao))
else:
    print('Empréstimo aprovado! A prestação de R${:.2f} cabe no seu orçamento!'.format(prestacao))
