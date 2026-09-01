#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# 1 Dólar = 3.27 reais


real = float(input('Diga aqui o seu saldo :R$ '))

dolar = real / 5.16
euro = real / 6.01

print('Você tem R${:.2f}, então pode comprar U${:.2f} e ε${:.2f}'.format(real,dolar,euro))