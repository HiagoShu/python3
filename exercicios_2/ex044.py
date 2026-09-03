#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: R$ '))
opcao = int(input(('''Escolha a forma de pagamento:
[1] - Á vista (10 por cento de desconto)
[2] - À vista no cartão (5 por cento de desconto)
[3] - Em até 2x no cartão (preço normal)
[4] - 3x ou mais no cartão (20 por cento de juros): 
''')))

if opcao == 1:
    print('O valor a ser pago é R$ {:.2f}'.format(preco - (preco *0.1)))
elif opcao == 2:
    print('O valor a ser pago é R$ {:.2f}'.format(preco - (preco *0.05)))
elif opcao == 3:
    print('O valor a ser pago é R$ {:.2f}'.format(preco))
else:
    print('O valor a ser pago é R$ {:.2f}'.format(preco + (preco *1.2)))



