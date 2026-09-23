def aumentar(num=0,taxa=0,format=False):
    res = num + (num * taxa/100)
    return res if format is False else moeda(res)

def diminuir(num = 0,taxa=0,format=False):
    res = num - (num * taxa/100)
    return res if format is False else moeda(res)


def metade(num=0,format=False):
    res = num /2
    return res if format is False else moeda(res)

def dobro(num=0,format=False):
    res = num *2
    return res if format is False else moeda(res)

def moeda(num=0,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')

def resumo(num,aum,red):
    print('-='*30)
    print('RESUMO DO VALOR'.center(30))
    print('-='*30)

    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço:  \t{moeda(dobro(num))}')
    print(f'Metade do preço: \t{moeda(metade(num))}')
    print(f'20% de aumento:  \t{moeda(aumentar(num,aum))}')
    print(f'12% de redução:  \t{moeda(diminuir(num,red))}')
    print('-='*30)