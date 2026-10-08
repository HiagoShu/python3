# Declaração de Classe
class Gafanhoto:
    #Método construtor
    def __init__(self):
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        print(f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.')


# Declaração de Objetos
g1 = Gafanhoto() #Os parênteses são uma chamada ao método construtor
g1.nome = 'Zé'
g1.idade = 20
g1.aniversario() #Chamada do método aniversario
print(g1.mensagem()) #Chamada do método mensagem