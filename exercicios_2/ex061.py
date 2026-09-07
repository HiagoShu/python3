# Refaça o DESAFIO 51. lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA ')
print('-='*20)

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro # Mostra/Acumula o termo
cont = 1 #  Conta quantas vezes

while cont <=10:
    print('{} -> '.format(termo),end='')
    termo +=razao # Soma 
    cont +=1
print('Fim')