#Escreva  um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada Km acima do limite.

v = int(input('Digite aqui a velocidade de seu carro: '))
limite = 80
if(v >limite):
    print('Você foi multado por ultrapassar a velocidade!')
    preco = (v-limite) * 7
    print('Você foi multado em R${:.2f}'.format(preco))
else:
    print('Você está na velocidade permitida. Continue assim!')