#Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
#Crie também um método que permita ao funcionário se apresentar.

class Funcionario:
    def __init__(self,nome,setor,cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo 

    def apresentar(self):
        return f"Olá. Meu nome é {self.nome}, trabalho no setor de {self.setor} e ocupo o cargo de {self.cargo}."


funcionario1 = Funcionario("João","Financeiro","Analista")

print(funcionario1.apresentar())