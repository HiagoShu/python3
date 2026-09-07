#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c%3 == 0:
       cont += 1
       soma += c
print('A soma de todos os {} ímpares múltiplos de 3 no intervalo de 1 a 500 é {}'.format(cont, soma))
print('FIM')
