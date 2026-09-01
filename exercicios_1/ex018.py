# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
from math import cos,sin,tan,radians
ang = float(input('Digite o ângulo que você deseja: '))
print('O cosseno desse ângulo é {:.2f}'.format(cos(radians(ang))))
print('O seno desse ângulo é {:.2f}'.format(sin(radians(ang))))
print('A tangente desse ângulo é {:.2f}'.format(tan(radians(ang))))