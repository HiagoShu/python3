# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while True:
    print('''

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa

 ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        multi = valor1 * valor2
        print('O resultado de {} x {} é {}'.format(valor1,valor2,multi))
    elif opcao ==3:
       if valor1 > valor2:
           print('O número {} é maior '.format(valor1))
       else:
           print('O número {} é maior').format(valor2)
