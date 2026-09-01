# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

#d= n *2
#t = n* 3
#rq = n**(1/2)

#print('Seu número é {}, o dobro é {}, o triplo é {}, e a raiz quadrada é {} '.format(n,d,t,rq))

# Alternativa sem variáveis para economia de memória
print('Seu número é {}, o dobro é {}, o triplo é {}, e a raiz quadrada é {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))