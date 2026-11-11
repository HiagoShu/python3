from classes import *

def main():
    # f = Gerente('Pedro',8000) 
    # try:
    #     f.salario = 2000
    # except Exception as e:
    #     print(f"ERRO! : {e}")
    # print(f)
    funcionarios = [
        Dev("Pedro",18000),
        Designer('José',25000),
        Gerente('Mariana',45000)
    ]

    for f in funcionarios:
        print(f)

if __name__ == "__main__":
    main()