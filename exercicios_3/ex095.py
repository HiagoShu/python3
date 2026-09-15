# Aprimore o desafio 93, para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for g in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {g+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]')).upper()[0]
        if opcao in 'SN':
            break 
        print('ERRO! Responda apenas S ou N')
    if opcao =='N':
        break



#RESULTADOS

#Cabeçalhos
print('-='*30)
print('Cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*40)


for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)


#Dados individuais
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca ==999:
        break 
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i,g in enumerate(time[busca] ['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-'*40)
print('<< VOLTE SEMPRE >>')