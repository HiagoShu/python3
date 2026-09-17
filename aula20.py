# def linha():
#     print('-='*30)

# linha()
# print('Hello World!')
# linha()

# def mensagem(msg):
#     print('-='*30)
#     print(msg)
#     print('-='*30)

# mensagem('Sistema de Alunos')


# def soma(n1,n2):
#     print(f'N1 = {n1} e N2 = {n2}')
#     soma = n1+n2 
#     print(f'A soma de {n1} e {n2} é : {soma}')

# soma(4,5)

# soma(8,9)

# soma(n1=2,n2=1)
# soma(n2=3,n1=7)

#EMPACOTANDO PARÂMETROS

# def contador(*num):
# #    print(num) #Ele coloca os valores em tuplas. Então posso fazer o que se faz com tuplas
#     # for valor in num:
#     #     print(f' {valor} ', end='')
#     # print('FIM!')
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')

# contador(2,1,7)
# contador(8,8)
# contador(4,4,7,6,2)

def soma(*valores):
    s=0
    for num in valores:
        s+= num 
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)

#TRABALHANDO COM LISTAS E FUNÇÕES
def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *=2
        pos+=1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)