#for oi in range(5):
#    print('Oi mundo.')
#print('FIM')

#for oi in range(1, 6):
#    print('Oi mundo.')
#print('FIM')

# Para contar para trás. Use o -1 no final
#for c in range(6,0, -1):
#    print(c)

# Contando pulando de dois em dois
#for c in range(0,7,2):
#    print(c)
#print('FIM')


#Forma interativa
#n = int(input('Digite um número: '))
#for c in range (0,n+1):
#    print(c)
#print('FIM')

#Forma interativa com passo
#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))

#for c in range(i, f+1, p):
#    print(c)
#print('FIM')

#Somatório com for
s=0
for c in range(0,4):
    n=int(input('Digite um valor: '))
    s += n # O s vai recebendo os valores digitados e somando
print('O somatório de todos os valores foi {}'.format(s))