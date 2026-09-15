# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final ,tudo isso será guardado em um dicionário, incluindo o total de gols feito durante o campeonato.

jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for g in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {g}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for c,v in jogador.items():
    print(f'O campo {c} tem valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas.')
for p,g in enumerate(partidas):
    print(f' Na partida {p}, fez {g} gols')