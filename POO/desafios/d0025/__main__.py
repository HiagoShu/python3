from transportes import Moto, Caminhao, Drone
from rich import print
from rich.table import Table
from rich.console import Console 

#MANEIRA SEM A TABELA
# def main():
#     dist = 10

#     entrega = Drone(dist)
#     frete = entrega.calcular_frete()
#     if frete is not None:
#         print(f"Frete de {type(entrega).__name__} em {dist}Km = R${frete:,.2f}")
#     else:
#         print("Cálculo de frete cancelado devido ás restrições de distância")



#COM A TABELA
def main():
    dist = 100
    transportes = [
        Moto(dist),
        Caminhao(dist),
        Drone(dist)
    ]

    #Criação do objeto Console e da Tabela
    console = Console()
    tabela = Table()

    #Adição das colunas conforme o exemplo
    tabela.add_column("Distancia") 
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    #Adicionando as linhas dinamicamente
    for item in transportes:
        resultado = item.calcular_frete()

        #Se o resultado for numérico, formata como moeda
        if isinstance(resultado,(int,float)):
            valor_frete = f"R${resultado:,.2f}"
        else:
            valor_frete = str(resultado)

        tabela.add_row(
            f"{item.distancia}Km",
            type(item).__name__,
            valor_frete
        )

    #Exibe a tabela formatada no terminal
    console.print(tabela)


if __name__ == "__main__":
    main()