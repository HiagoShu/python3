# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))

print('-='*20)
for c in range(1, 11):
    print('{} x {} = {}'.format(n,c,n*c))
print('-='*20)
