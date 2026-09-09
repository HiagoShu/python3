#Tuplas podem ser criadas com ou sem parênteses ()
#lanche ='Hambúrguer','Suco','Pizza','Pudim'
#print(lanche)
#print(lanche[1]) #Suco
#print(lanche[-2]) # Pizza
#print(lanche[1:3]) # Suco, Pizza (O último elemento é ignorado)
#print(lanche[2:]) #Pizza até o final, Pudim
#print(lanche[:2]) # Mostra o anterior até o 2, menos ele próprio.
#print(lanche[-3:]) # Vai do suco até o final, acessando de trás para frente.

#Tuplas são imutáveis
#lanche[1] = 'refri' #Dará erro
#print(lanche[1]) 

#Usando for para print de tupla

#for comida in lanche:
#    print(f'Eu vou comer {comida}')

#Acessando o tamanho da tupla 

#print(len(lanche)) # Mostra a quantidade de itens

#Usando for com len

#for cont in range(0,len(lanche)): 
#    print(cont) #Mostra os números dos índices
#    print(lanche[cont]) #Mostra os nomes dos índices

#Outra forma que funciona como a de cima
#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

#Método sorted - Em ordem alfabética
#A ordem não muda, só a apresentação que muda
# Transformando numa lista.

#print(sorted(lanche))

#a = (2,5,4)
#b= (5,8,1,2)
#c = b+a #Ele concatena uma tupla na outra. A ordem tem total influência
#print(c)
#print(len(c))
#Métodos internos da tupla
#print(c.count(5)) #Quantas vezes o número cinco aparece
#print(c.index(2)) #Em qual posição está o número 2? R: 3
#print(c.index(2,4)) #Em qual posição está o número 2 a partir da posição 4?  R: 4

#No python, uma tupla aceita números e strings
pessoa = ('Gustavo',39,'Masculino','99.88')
#É possível apagar uma variável 
# del(pessoa) 
#Logo abaixo daria como 'pessoa' is undefined. É possível apagar apenas a tupla inteira. Não um elemento da tupla.
print(f'Meu nome é {pessoa[0]},tenho {pessoa[1]} anos de idade, sou do sexo {pessoa[2]} e tenho na minha conta R${pessoa[3]}')