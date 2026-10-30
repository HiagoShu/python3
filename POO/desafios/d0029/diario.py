from rich import print

class Diario():
    def __init__(self):
        self.__segredos=[]
        self.__senha =0

    @property
    def escrever(self):
        return self.__segredos 

    @escrever.setter
    def escrever(self,msg):
        self.__segredos.append(msg)
        print("[green]Seu registro no diário foi feito com sucesso![/green]")

    @property
    def ler(self):
        return self.__senha

    @ler.setter 
    def ler(self,senha):
        self.__senha = senha
        if self.__senha == "Deusminhavida":
            for i, registro in enumerate(self.escrever,start=1):
                print(f"Registro do diário [yellow]{i}[/yellow]: [blue]{registro}[/blue]")
        else:
            print("[red]Senha incorreta! Você não pode ler meu diário![/red]")
    