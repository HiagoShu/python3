# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.Para salários superiores a R$1250,00 calcule um aumento de 10%.

#Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o valor de seu salário: '))

if salario <= 1250:
    salario = salario *1.15
else:
    salario = salario *1.1
print('Seu salário com reajuste é de R${:.2F}'.format(salario))