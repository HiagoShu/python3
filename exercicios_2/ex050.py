# Faça um programa que leia seis números inteiros e mostre a soma apenas dos que forem pares. Se o valor digitado for ímpar, desconsidere-o.
num = 0
soma = 0
for c in range(1,7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares digitados é {}'.format(soma))