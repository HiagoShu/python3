from rich import print

#Meu jeito
# class Diario():
#     def __init__(self):
#         self.__segredos=[]
#         self.__senha =0

#     @property
#     def escrever(self):
#         return self.__segredos 

#     @escrever.setter
#     def escrever(self,msg):
#         self.__segredos.append(msg)
#         print("[green]Seu registro no diário foi feito com sucesso![/green]")

#     @property
#     def ler(self):
#         return self.__senha

#     @ler.setter 
#     def ler(self,senha):
#         self.__senha = senha
#         if self.__senha == "Deusminhavida":
#             for i, registro in enumerate(self.escrever,start=1):
#                 print(f"Registro do diário [yellow]{i}[/yellow]: [blue]{registro}[/blue]")
#         else:
#             print("[red]Senha incorreta! Você não pode ler meu diário![/red]")
    

#Forma do professor
class Diario:
    def __init__(self,senhamestra= 'Senha'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self,msg):
        if isinstance(msg,str) and len(msg) > 0:
            self.__segredos.append(msg.strip()) 

    def ler(self,senha=None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")
        else:
            print(f"[green]Diário LIBERADO![/]")
            for segredo in self.__segredos:
                print(f" - {segredo}")

    @property 
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha!")