#TIPOS PRIMITIVOS
#int - inteiro
#Dessa forma, é possível realizar a forma como se fosse um número
# e não uma string.

#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite mais um número: '))
#s = n1+n2
# print('A soma entre',n1,'e',n2, 'vale',s)

#Sintaxe melhor abaixo - mais atual
#print('A soma entre {} e {} vale {}'.format(n1,n2,s))


#float - ponto flutuante
#n = float(input('Digite um valor: '))
#print(n)


# bool - booleano(True,False)
#n= bool(input('Digite um valor: '))
#print(n)
#Se digitar algo, retorna True, se não digitar nada, retorna False


# str - string ,caracteres
#n= str(input('Digite alguma coisa: '))
#print(n)


#O isnumeric - Verifica se é um numeral, independente se é string ou int
#retornando True ou False

#n=input('Digite algo: ')
#print(n.isnumeric())

#isalpha (se é alfabético)
#n= input('Digite algo: ')
#print(n.isalpha())


# isalphanum - Se é número e/ou alfabético
n= input('Digite algo: ')
print(n.isalnum())