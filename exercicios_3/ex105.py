# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas.
# A maior nota.
# A menor nota. 
# A média da turma.
# A situação(opcional)

#Adicione também as docstrings da função

def linha():
    print('-='*30)

# Minha tentativa - Tryhardei
# def notas(*valor,sit=False):
#     maior = menor = 0
#     soma = media = 0
#     alunos = {}
#     alunos['total']=len(valor) 
#     for cont in range(0,len(valor)):
#         soma += valor[cont]
#         if cont ==1:
#             maior = valor[cont]
#             menor = valor[cont]
#         else:
#             if valor[cont] < menor:
#                 menor = valor[cont]
#             if valor[cont] > maior:
#                 maior = valor[cont] 
#     media = soma / len(valor)

    
#     alunos['Maior'] = maior 
#     alunos['Menor'] = menor
#     alunos['Média'] = media
#     if sit:
#         if media <=8:
#             alunos['Situação'] = 'Boa'
#         if media <=7:
#             alunos['Situação'] = 'Razoável'
#         if media <=5:
#             alunos['Situação'] = 'Ruim'
#     return alunos.items()


#Método do professor
def notas(*n,sit = False):
    """_summary_
    -> Função para a informação de notas
     :param *n: Informe quantas notas quiser.
     :param sit: valor opcional, indicando se deve ou não adicionar a situação.
     :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >=7:
            r['situação'] = 'BOA'
        elif r['média'] >=5:
             r['situação'] = 'RAZOÁVEL'
        else: 
            r['situação'] = 'RUIM'
    return r

linha()
resp = notas(5.5,2.5,1.5,sit=True)
print(resp)
help(notas)