from abc import ABC,abstractmethod
from rich import print
from rich.panel import Panel
class Funcionário(ABC):
    #Atributos de Classe
    sal_min = 1612
    inss = 7.5

    #Atributos de instância
    def __init__(self,nome=None):
        self.nome = nome 
        self.sal_bruto = 0
        self.salario = 0 

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionário.sal_min

        mensagem = f"O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{base:.1f} salários mínimos.[/]"

        analise =Panel(mensagem,title="Análise de Salário",width=50)
        print(analise)


class FuncionarioHorista(Funcionário):
    def __init__(self,nome,valor_hora = 7.37,qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionário.inss /100)

class FuncionarioMensalista(Funcionário):

    def __init__(self,nome,sal_bruto=Funcionário.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto 

    
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionário.inss /100)
