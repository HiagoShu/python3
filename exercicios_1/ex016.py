# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127          
# O número 6.127 tem a parte inteira 6. 
#Modo 1
#from math import trunc
#num = float(input('Digite aqui um número real: '))
#print('O número {} tem a parte inteira {}'.format(num,trunc(num)))

# o truncate corta a parte não inteira do número

# Modo 2
num = float(input('Digite aqui um numero real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))