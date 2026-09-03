# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for pessoa in range(1,6):
    p = float(input('Digite o peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi {:.1f} kg.'.format(maior))
print('O menor peso lido foi {:.1f} kg.'.format(menor))