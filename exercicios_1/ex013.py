# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite aqui o valor do seu salário: R$'))

aumento = salario * 1.15

print('Seu salário anterior era de R${:.2f}, e com aumento é de R${:.2f}'.format(salario,aumento))