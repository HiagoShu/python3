# Declaração de Classe
class Gafanhoto:
    """
    SUMÁRIO
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome,idade)
    """
    #Método construtor
    def __init__(self,nome= 'Vazio',idade=0):
        #Atributos de instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder method 
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"
# Declaração de Objetos
g1 = Gafanhoto('Zé',20) #Os parênteses são uma chamada ao método construtor
print(g1) #Usando o Dunder __str__ para imprimir a mensagem
print(g1.__dict__) #Dunder atributte __dict__ mostra os atributos do objeto
print(g1.__getstate__()) #Usando o Dunder method __getstate__ para imprimir o estado do objeto
print(g1.__class__) #Dunder method __class__ mostra a classe do objeto
# print(g1.__doc__)