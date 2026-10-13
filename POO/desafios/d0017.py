# Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.
from rich import print 
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco 

    def etiqueta(self):
        return Panel(f"{self.nome} ---------------------------- Preço: R$ {self.preco:.2f}",title = "Produto:",width=35,)


produto1 = Produto("Notebook", 2500.00)
produto2 = Produto("Smartphone", 1500.00)

print(produto1.etiqueta())
print(produto2.etiqueta())