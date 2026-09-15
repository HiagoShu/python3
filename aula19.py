#pessoas = {
#    'nome': 'Gustavo',
#    'sexo': 'M',
#    'idade': 22
#}
#print(pessoas)
#print(pessoas['nome']) #Acessando a chave
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #Dentro de um print formatado, usa-se aspas duplas ali na identificação da chave.
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items()) #Uma lista compostas de 3 tuplas.

#Acessando chave, valor e item com FOR
#for key in pessoas.keys():
#    print(key)

#for valor in pessoas.values():
#    print(valor)

#for key,valor in pessoas.items():
#    print(f'{key} = {valor}')

#APAGANDO UM ITEM
#del pessoas['sexo']
#print(pessoas)

#Modificando um item
#pessoas['nome'] = 'Leandro'
#print(pessoas)

#Adicionando um item
#pessoas['peso'] = 98.5
#print(pessoas)


#CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA
#brasil = [] #lista
#estado1 ={'uf':'Rio de Janeiro','sigla':'RJ'} #dicionario
#estado2 ={'uf':'São Paulo','sigla':'SP'}

#brasil.append(estado1)
#brasil.append(estado2)

#print(estado1)
#print(brasil) #Lista com dicionários
#print(brasil[0])
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

#O problema que será aqui apresentado é que, ao dar append, a lista vai receber o último elemento informado pelo input.
#Contudo, se fizer uma cópia, fatiamento, também vai dar ruim, pois é um dicionário.

#COMO FAZER CÓPIA DE UM ELEMENTO SEM FAZER FATIAMENTO?
# Com o método .copy()
estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

# for e in brasil:
#     print(e)

for e in brasil: # Da lista
    # for k,v in e.items(): #Do dicionário
    #     print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')

"""
Oh glória Isso é um COMENTÁRIO
"""