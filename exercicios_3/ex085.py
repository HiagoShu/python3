# Crie um programa onde um usuário possa digitar 7 valores numéricos e cadastres em uma lista única que mantenha separados os valores pares e ímpares. (Cadastrar os pares no índice 0 e os ímpares no índice 1, por exemplo)

#No final, mostre os valores pares e ímpares em ordem crescente.

numeros =[[],[]]

for n in range(0,7):
    valor = (int(input('Digite um número: ')))
    if valor %2 ==0:
        numeros[0].insert(0,valor)
    else:
        numeros[1].insert(0,valor)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram:  {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')