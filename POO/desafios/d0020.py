#Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritas de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.
from rich import print
from rich.panel import Panel 

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome 
        self.nick = nick
        self.favoritos = list() 

    def add_favoritos(self,jogo):
        self.favoritos.append(jogo) 
        self.favoritos.sort()

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        print(Panel(f"{conteudo}",title=self.nick,width=40))

j1 = Gamer("João Silva","Pimpolho123")
j1.add_favoritos("God Of War")
j1.add_favoritos("Animal Kingdom")
j1.add_favoritos("Minecraft")
j1.ficha()

j2 = Gamer("Olívia Souza","peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()