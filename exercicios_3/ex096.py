#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def linha(txt):
    print(txt)
    print('-='*30)

def área(largura,comprimento):
    area = largura * comprimento 
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


linha('Controle de Terrenos')

largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura,comprimento)