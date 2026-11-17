from abc import ABC,abstractmethod

class Arquivo(ABC):
    def __init__(self,nome:str,extensao:str,tamanho:int=0):
        self.nome = nome 
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = extensao

    @property 
    def extensao(self):
        return self._extensao

    @property 
    def nome_completo(self):
        return f"{self.nome}.{self.extensao} ({self.tamanho/1000000}MB)"

    @extensao.setter
    def extensao(self,extensao:str):
        formatos = ['pdf','doc','docx']
        ext = extensao.lower().strip()
        if ext in formatos:
            self._extensao = ext 
        else:
            raise AttributeError("O Arquivo está em um formato não suportado")


    @abstractmethod
    def abrir(self):
        pass

class DOC(Arquivo):

    def __init__(self,nome:str, tam:int):
        super().__init__(nome,'docx',tam)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word") 

class PDF(Arquivo):

    def __init__(self,nome:str,tam:int):
        super().__init__(nome,'pdf',tam)   

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader") 


def abrir_arquivo(arquivo):
    arquivo.abrir()