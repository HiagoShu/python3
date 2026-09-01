#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 =float(input('Digite aqui sua nota 1: '))
n2 = float(input('Digite aqui sua nota 2: '))

media = (n1+n2) /2

print('Sua nota 1 é {:.1f} , sua nota 2 é {:.1f} , e sua média ficou {:.1f} .'.format(n1,n2,media))