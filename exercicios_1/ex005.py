#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))
suc = n +1
ant = n -1

print('O seu número é {}, seu antecessor é {} , e seu sucessor é {}'.format(n,ant,suc))

# Alternativa sem as variáveis antecessor e sucessor

#print('O seu número é {}, seu antecessor é {}, e seu sucessor é {}'.format(n,(n-1),(n+1)))