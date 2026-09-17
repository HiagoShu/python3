# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Olá,mundo!')
# Saída:  ~~~~~~~~~~~~
#          Olá,Mundo!
#         ~~~~~~~~~~~~

def escreva(txt):
    #Minha forma
    # print('~'*len(txt))
    # print(txt)
    # print('~'*len(txt))

    #Forma do professor
    tam = len(txt) +4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)

escreva('Gustavo Guanabara')
escreva('Papibaquígrafo de um Otorrinolaringologista')
escreva('PT-BR')