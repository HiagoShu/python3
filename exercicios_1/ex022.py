# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo (sem contar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite aqui o seu nome: '))
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ',''))))
print('Seu primero nome é {} e ele tem {} letras'.format(nome.split()[0],len(nome.split()[0])))