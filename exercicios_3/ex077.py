# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} tem as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou': #A solução para o aceite de palavras com acento é colocar cada letra com as variações.
            print(letra,end=' ')