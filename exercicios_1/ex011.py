#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura =float(input('Digite aqui a altura da sua parede em metros: '))
largura = float(input('Digite aqui a largura da sua parede em metros: '))

area = altura * largura 

tinta = area / 2

print('A área da parede é de {}m² e será necessário {} litros de tinta'.format(area,tinta))