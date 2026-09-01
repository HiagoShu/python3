
# Estrutura condicional aninhada
nome = str(input('Qual é o seu nome? '))
if nome =='Gustavo':
    print('Que nome bonito!')
elif nome == 'Heisenberg':
    print('You are goddamn right')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else: 
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))