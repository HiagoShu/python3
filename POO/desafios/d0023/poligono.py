from abc import ABC,abstractmethod
class Poligono(ABC):
    def __init__(self,lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass 

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono): 
    def __init__(self,comprimento_lado=1):
        super().__init__(4)
        self.tam_lados = comprimento_lado

    def perimetro(self):
        return  self.tam_lados *4

    def area(self):
        return self.tam_lados * self.tam_lados 

class Circulo(Poligono):
    def __init__(self,raio):
        super().__init__(0)
        self.raio = raio 

    def perimetro(self):
        return 2* 3.14 * self.raio  

    def area(self):
        return 3.14 * (self.raio **2)