from lib.interface import cabeçalho
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #write text
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()

def cadastrar(arq, nomePessoa='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #append text
    except:
        print('Houve um ERRO ao cadastrar a pessoa!')
    else:
        a.write(f'{nomePessoa};{idade}\n')
        print(f'Novo registro de {nomePessoa} adicionado.')
    finally:
        a.close()