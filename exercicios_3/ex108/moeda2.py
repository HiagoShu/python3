def aumentar(num=0,taxa=0):
    res = num + (num * taxa/100)
    return res 

def diminuir(num = 0,taxa=0 ):
    res = num - (num * taxa/100)
    return res
def metade(num=0):
    return num /2

def dobro(num=0):
    return num *2

def moeda(num=0,moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')