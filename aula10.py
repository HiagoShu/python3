#nome = str(input('Qual é seu nome? '))

#condição simples
#if nome == 'Gustavo':
#    print('Que nome legal!')
##condição composta
#else:
#    print('Seu nome é tão normal...')
#print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) /2
print('A sua média foi {:.1f}'.format(m))
if m <7:
    print('Reprovado(a)')
else:
    print('Aprovado(a)')