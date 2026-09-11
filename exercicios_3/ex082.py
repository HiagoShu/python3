# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

# Ao final, mostre o conteúdo dos três listas geradas. 

geral = []
par = []
impar = []

while True:
    n = int(input('Digite um número: '))
    geral.append(n)
    if n %2 == 0:
        par.append(n)
    else:
        impar.append(n)

    opcao = ' '
    while opcao not in 'SsNn':
        opcao=str(input('Você quer continuar? [S/N]').strip().upper()[0])
    if opcao =='N':
        break 

    #Controle de continuação do professor.
        # resp = str(input('Quer continuar? [S/N] '))
        # if resp in 'Nn':
        #       break
#Maneira de preenchimento das listas de par e ímpar do professor
# for i, v in enumerate(num):
#       if v%2 ==0:
#           par.append(v)
#       elif v%2 == 1:
#           impar.append(v)

print('-='*30)
print(f'A lista geral contém os seguintes números: {geral}')
print(f'A lista com os pares é {par}')
print(f'A lista com os ímpares é {impar}')