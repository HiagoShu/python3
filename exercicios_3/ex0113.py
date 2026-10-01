#Reescreva  a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def linha():
    print('-='*30)

def leiaInt(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO! Digite um número real válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n
#Programa principal
linha()
n = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {n2}')