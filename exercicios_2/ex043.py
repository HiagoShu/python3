# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18.5: Abaixo do Peso
# - IMC entre 18.5 e 25: Peso Ideal
# - IMC entre 25 e 30: Sobrepeso
# - IMC entre 30 e 40: Obesidade
# - IMC acima de 40: Obesidade Mórbida
peso = int(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está ABAIXO DO PESO.'.format(imc))
elif imc <25:
    print('Seu IMC é {:.1f}. Você está no PESO IDEAL.'.format(imc))
elif imc <30:
    print('Seu IMC é {:.1f}. Você está com SOBREPESO.'.format(imc))
elif imc <40:
    print('Seu IMC é {:.1f}. Você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))