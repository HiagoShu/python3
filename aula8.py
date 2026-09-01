from math import sqrt,ceil
#1º FORMA - Importando tudo
#Se tiver algo a mais na primeira linha, deixe só   import math
#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))


# 2º Forma - Importando apenas uma funcionalidade
# escreva na primeira linha: from math import sqrt,ceil
#E não precisa utilizar a referência math.
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,ceil(raiz)))