#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

m = int(input('Digite aqui um valor em metro: '))

cm = m *100
mm = m*1000

print('O valor em metro é {} metros, o valor em centímetro é {} , o valor em milímetro é {}'.format(m,cm,mm))