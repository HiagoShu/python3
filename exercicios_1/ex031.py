#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

dist = int(input('Digite aqui a distância da viagem que você fará: '))

if(dist<=200):
    preco = dist *0.50
    print('O preço da sua viagem será {:.2f}'.format(preco))
else:
    preco = dist *0.45
    print('O preço da sua viagem será {:.2f}'.format(preco))
