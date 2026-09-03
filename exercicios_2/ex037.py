#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
# 2 para octal 
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha a base de conversão:\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n'))

if opcao ==1:
    print('O número {} em BINÁRIO  é {}'.format(num,bin(num)[2:]))
elif opcao ==2:
    print('O número {} em OCTAL é {}'.format(num,oct(num)[2:]))
elif opcao ==3:
    print('O número {} em HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida!')