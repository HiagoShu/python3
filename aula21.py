# Função com docstrings
def contador(i,f,p):
    """_summary_
        -> Faz uma contagem e mostra na tela.
        :Parâmetro i: início da contagem.
        :Parâmetro f: fim da contagem.
        :Parâmetro p: passo da contagem
        :return: sem retorno
    """
    c = i 
    while c <=f:
        print(f'{c}',end=' ... ')
        c+=p 
    print('FIM!')

#contador(0,100,10)


# Ajuda interativa
#help(contador)

# Parâmetros opcionais

def somar(a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale: {s}')

#somar(3,2,5) # Funciona
#somar(8,4) #Se não fosse o conceito de parâmetros opcionais, daria erro
# somar(3)
# somar()
# somar(b=4,c=3)

# Escopo de variáveis

def teste():
    x =8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
# Programa principal
n =2  # Escopo global, alcança a todo o programa
# print(f'No programa principal, n vale {n}')
# teste()
#print(f'No programa principal, x vale {x}') Dá erro pois o x é de escopo local da função teste

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

# n1 = 2 
# print(f'N1 fora vale {n1}')
# funcao()



# Como modificar a variável global
def teste1(b):
    global a #Modificação no A global, sem criação de variável local
    a = 8
    b+=4
    c =2 
    print(f'A dentro vale {a}')
    print(f'B dentro vale  {b}')
    print(f'C dentro vale {c}')

# a = 5
# teste1(a)
# print(f'A fora vale {a}')

#RETORNAR VALORES
def somar1(a=0,b=0,c=0):
    s = a+b+c 
    return s 

# resp = somar1(3,2,5)
# print(somar(3,2,5))

# r1 = somar1(3,2,5)
# r2 = somar1(1,7)
# r3 = somar1(4)
# print(f'Meus cálculos deram {r1},{r2},{r3}')


def fatorial (n =1):
    f = 1 
    for c in range(n, 0, -1):
        f *= c 
    return f 

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


# f1 = fatorial(5)
# f2  = fatorial(4)
# f3 = fatorial()

# print(f'Os resultados são {f1},{f2},{f3}')

def par(n=0):
    if n %2 ==0:
        return True
    else:
        return False 

# num = int(input('Digite um número: '))
# if par(num):
#     print('É par!')
# else:
#     print('Não é par!')