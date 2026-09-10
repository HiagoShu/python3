# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela = ('Salsinha',3.55,'Manjericão',2.95,'Cominho',2.89,'Alecrim',7,'Alho',8.5)
#Meu método
#print('=-'*20)
#print('TABELA DE PREÇOS')
#print('=-'*20)
#print(f'''
#{tabela[0]} ............ R${tabela[1]}
#{tabela[2]} ............ R${tabela[3]}
#{tabela[4]} ............ R${tabela[5]}
#''')
#print('=-'*20)

#Método do Professor
print('-'*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(tabela)):
    if pos %2 == 0:
        print(f'{tabela[pos]:.<30}',end='') 
    else:
        print(f'R${tabela[pos]:>7.2f}')
print('-'*40)

#O método do professor tá mais bem feitinho kkkkkk