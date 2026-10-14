#Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa. Considere que cada pessoa consome 400g de carne e o preço do kg da carne é R$ 82,40.
from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self,titulo, num_pessoas):
        self.titulo = titulo
        self.num_pessoas = num_pessoas
        self.consumo_por_pessoa = 0.4 #em kg
        self.preco_kg_carne = 82.40 #em reais

    def calcular_quantidade_carne(self):
        return self.num_pessoas * self.consumo_por_pessoa

    def calcular_custo_total(self):
        quantidade_carne = self.calcular_quantidade_carne()
        return quantidade_carne * self.preco_kg_carne

    def calcular_preco_por_pessoa(self):
        custo_total = self.calcular_custo_total()
        return custo_total / self.num_pessoas 

    def analisar(self):
        quantidade_carne = self.calcular_quantidade_carne()
        custo_total = self.calcular_custo_total()
        custo_pessoa = self.calcular_preco_por_pessoa()
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.num_pessoas} convidados. [/] \n"

        conteudo +=f"Cada participante comerá {self.consumo_por_pessoa}Kg e cada Kg custa R${self.preco_kg_carne:.2f}\n"

        conteudo += f"Recomendo [blue]comprar {quantidade_carne}Kg[/] de carne.\n"

        conteudo +=f"O custo total será de [green]R${custo_total:.2f}[/]\n"

        conteudo += f"Cada pessoa pagará [yellow]R${custo_pessoa}[/] para participar"

        # return Panel(f"Analisando [green] Churras dos Amigos[/] com [blue]{self.num_pessoas} convidados. [/] \nCada participante comerá {self.consumo_por_pessoa}Kg e cada Kg custa R${self.preco_kg_carne:.2f}\nRecomendo [blue]comprar {quantidade_carne}Kg[/] de carne.\nO custo total será de [green]R${custo_total:.2f}[/]\nCada pessoa pagará [yellow]R${custo_pessoa}[/] para participar",title="Churras dos Amigos",width=70)

        return Panel(f"{conteudo}",title=self.titulo,width=70)


c1 = Churrasco("Churras dos Amigos",15)
print(c1.analisar())