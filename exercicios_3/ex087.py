# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna. 
# C ) O Maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = scol = 0
#Alimentação da Matriz
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))

print('-='*30)
# Print da Matriz Formatada

for l in range(0,3):
    scol += matriz[l][2]
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 ==0:
            spar += matriz[l][c]
    print()

print(f'A soma dos pares informados é: {spar}')
print(f'A soma dos valores da terceira coluna é de: {scol}')  
print(f' O maior número da segunda linha é: {max(matriz[1])}')