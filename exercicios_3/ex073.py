#Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem da colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

tupla = ('Flamengo','Palmeiras','Atlético-PR','Fluminense','Bahia','Cruzeiro','Coritiba','Atlético-MG','Bragantino','São Paulo','EC Vitória','Corinthians','Santos','Botafogo','Grêmio','Mirassol','Vasco de Gama','Internacional','Remo','Chapecoense')

print(f'Os Cinco primeiros colocados são: {tupla[:5]}')
print('-='*20)
print(f'Os Quatro últimos colocados são: {tupla[-4:]}')
print('-='*20)
print(f'Em ordem alfabética: {sorted(tupla)}')
print('-='*20)
print(f'A posição da chapecoense  é : {tupla.index("Chapecoense")+1}ª')