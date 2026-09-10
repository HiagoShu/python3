#LISTAS
#Listas,diferente das tuplas,  podem ser atualizadas 

num = [2,5,9,1]
print(num)
num[0]=1 #Substituindo um item na lista
print(num)
num.append(4)  #Acrescentando um item na lista
print(num)
num.insert(1,8)  #Colocando um 8 na posição(index) 1
print(num)
del num[1] #Deletando um elemento. Nesse caso, o 8
print(num)
num.pop(0)  #Usando num.pop você deleta o último elemento, mas você também pode passar o índice como parâmetro.
print(num)
num.remove(4) #Aqui não estou passando o índice como parâmetro, mas o elemento em si.
print(num)

#Verificando se tal elemento está na lista para apagá-lo
lista1 = ['Pizza','Cachorro-Quente','Asa de Galinha']
if 'Pizza' in lista1:
    lista1.remove('Pizza')
print(lista1)

#Agora, para adicionar
lista2 = ['Macaco','Urubu']
if 'Puma' not in lista2:
    lista2.append('Puma')
print(lista2)

#Também é possível declarar uma lista com a função list
valores = list(range(4,11)) 
print(valores)
#Mostrando cada valor de forma mais bonitinha
for v in valores:
    print(f'{v}...')

#Lista não ordenada e colocada em ordem
valores1=[8,2,5,4,9,3,0]
valores1.sort()  #Colocando em ordem "Crescente"
print(valores1)
valores1.sort(reverse=True) #Revertendo a ordem
print(valores1)

#Vendo o tamanho da lista
print(f'Essa lista tem {len(valores1)} elementos')

#Lendo valores e colocando dentro de listas, e informando sua posição.
#numeros = list()
#for cont in range(0,5):
#    numeros.append(int(input('Digite um valor: ')))

#for c,v in enumerate(numeros):
#    print(f'Na posição {c} encontrei o valor {v} !')
#print('Cheguei ao final da lista')


#Ligação de listas.
#Se eu alterar uma lista que está ligada, a outra também será.
a = [2,3,4,7]
#b=a #Ligação de listas
b = a[:] #Cópia de lista
b[2]=8
print(f'LISTA A: {a}')
print(f'LISTA B: {b}')