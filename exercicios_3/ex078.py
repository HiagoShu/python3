#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros=list()
for cont in range(0,5):
    numeros.append(int(input('Digite um valor: ')))

print(f'Você digitou os valores: {numeros}')

maior = max(numeros)
menor = min(numeros)

pos_maior = list()
pos_menor = list()
for c,v in enumerate(numeros):
    if v == maior:
        pos_maior.append(c)
    elif v == menor:
        pos_menor.append(c)

print(f'O maior valor digitado foi {maior} nas posições {pos_maior}')
print(f'O menor valor digitado foi {menor} nas posições {pos_menor}')

print('Cheguei ao fim da lista.')