from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self,dist):
        self.distancia = dist 

    @abstractmethod
    def calcular_frete():
        pass

class Moto(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.frete =0.50 

    def calcular_frete(self):
        return self.frete * self.distancia


class Caminhao(Transporte):
    def __init__(self,dist):
        super().__init__(dist)
        self.frete = 1.20

    def calcular_frete(self):
        #Maneira sem a tabela
        # if self.distancia <50:
        #     print(f"Não é possível realizar viagens de Caminhão com menos de 50km!")
        #     return None
        # else:
        #     return self.frete *self.distancia
        if self.distancia <50:
            return "Distância mínima de 50Km"
        return self.frete *self.distancia
        



class Drone(Transporte):
   def __init__(self,dist):
       super().__init__(dist)
       self.frete = 9.50

   def calcular_frete(self):
       #Maneira sem a tabela
        # if self.distancia >10:
        #     print("Não é possível realizar entregas de drone acima de 10km!")
        #     return None
        # else:
        #     return self.frete * self.distancia
        if self.distancia >10:
            return "Raio máximo de 10Km"
        return self.frete *self.distancia