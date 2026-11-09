from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,nome):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e emite som.")
class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer QUÁ QUÁ QUÁ")

class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer AU AU AU")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de latir au! au! au!")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} acabou de latir RUF RUF RUF")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer MIAU MIAU MIAU")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} acabou de dizer CÓCÓCÓ")