#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#print(teste)
#galera = list()
#galera.append(teste) #Ocorre uma ligação
#print(galera)
#teste[0] = 'Maria'
#teste [1] = 22
#print(galera) # Galera e Teste foram ambos modificados por causa da ligação
#print(teste)
#galera.append(teste[:]) #Cópia
#print(galera)

#galera =[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
#print(galera)
#print(galera[0]) #Todos os dados de João - índice 0 todo
#print(galera[0] [0]) # índice 0 índice 0 = Nome do João
#print(galera[2][1]) 

#PRINTANDO COM FOR
#for p in galera:
#    print(p) #Acessando os dados completos de todos
#    print(p[0]) #Acessando apenas o nome
#    print(p[1]) #Acessando apenas a idade
#    print(f'{p[0]} tem {p[1]} anos de idade.') #Formatado 


#PEDINDO NOME E IDADE
galera = list() #Estrutura principal
dado = list() #Estrutura auxiliar que vai encaminhar para a principal
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Aqui é uma cópia. Se você ligar e usar o clear(), ambas as listas ficarão vazias.
    dado.clear()
print(galera)

#MOSTRANDO AS PESSOAS COM MAIS DE 21 ANOS
totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')