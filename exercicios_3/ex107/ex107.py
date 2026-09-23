#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()

#Faça também um programa que importe esse módulo e use algumas dessas funções

import moeda 

n = float(input('Digite o preço: R$'))

print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n)}')