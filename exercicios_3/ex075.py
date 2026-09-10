# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3. 
# C) Quais foram os números pares.
tupla=()
for num in range(0,4):
    valor = int(input('Digite um valor: '))
    tupla += (valor,) #Transforma o valor em tupla.

print(f' Os valores que você digitou foram: {tupla}',end='')
print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')
#Tratamento para quando há e não há o valor 3
if 3 in tupla:
    print(f' O valor 3 apareceu na  {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado.')

print('Os números pares digitados foram: ',end=' ')

for numero in tupla:
    if numero %2 ==0:
        print(numero,end=' ')