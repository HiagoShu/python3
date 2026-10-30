# Implemente um termostato orientado a objetos.
#Temperatúra mínima: 16 graus, máxima: 30.
# Inicia em 24 graus.
#Incrementa de 0.5 



class Termostato():
    def __init__(self):
        self.__temperatura =24

    @property
    def temperatura(self): #getter
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor): #setter
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor}{chr(176)}C é inválida!")
        if valor < 16:
            self.__temperatura =16
        elif valor >30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"