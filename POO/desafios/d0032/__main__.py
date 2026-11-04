from conta import ContaBancaria

def main():
    cc = ContaBancaria(111,'Josenildo',1000)
    print('Vou tentar Sacar...')
    cc.sacar(500)
    print('Vou tentar alterar o nome...')
    cc.nome = 'Maricota'
    print(cc)
if __name__ == '__main__':
    main()