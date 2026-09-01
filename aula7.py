# Operadores aritméticos
# Adição + - Também pode ser usado para concatenar strings
# Subtração -
# Multiplicação * - Também pode ser usado para concaternar strings
# Divisão /
# Potência ** ou pow(número,expoente)
# Divisão inteira //
# Módulo (Resto da divisão) % 
#Raiz quadrada : 81 **(1/2)
# Raiz cúbica : 127 **(1/3)

#Operadores aritméticos só aceitam números ou variáveis que contenham números

#Exemplos

#n= 5+3*2
#n = 3*5+4**2
#n = 3*(5+4)**2
#print(n)

# Concatenando strings com adição e multiplicação
#print('Oi'+'Olá')
#print('=='*5)


#Alinhamentos

#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {}!'.format(nome))
#Espaçamento
#print('Prazer em te conhecer {:20}!'.format(nome)) 

#Alinhamento a direita
#print('Prazer em te conhecer {:>20}!'.format(nome)) 

#Alinhamento a esquerda
#print('{:<20} Prazer em te conhecer !'.format(nome)) 

# OBSERVAÇÃO DO GUANABARA

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 +n2
m = n1 * n2
d =n1 /n2 
di= n1//n2 
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d),end='')
print('  Divisão inteira {} e potência {}'.format(di,e))

#É possível fazer somas sem uma terceira variável
#print('A soma vale {}'.format(n1+n2))

