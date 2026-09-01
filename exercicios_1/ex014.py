#Escreva um programa que converta uma temperatura digita em °C e converta para °F.

graus = float(input('Digite aqui a temperatura em °C: '))

fah= (graus *1.8) +32

print('A temperatura em Celsius é {:.1f}°C e em Fahrenheit é {:.1f}°F'.format(graus,fah))