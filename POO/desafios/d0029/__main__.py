#minha forma
# from diario import Diario 

# def main():
#     d = Diario()
#     d.escrever="Oi, meu nome é Hiago"
#     d.escrever="Eu amo Jesus"
#     d.ler('Senha')

# if __name__ == "__main__":
#     main()


#Forma do professor
from diario import Diario 
from rich import print

def main():
    d = Diario()
    d.escrever("Oi, meu nome é Hiago")
    d.escrever("Eu amo Jesus")
    try:
        d.ler('Senha')
    except Exception as e:
        print(f"[red] ERRO: {e}[/]")

if __name__ == "__main__":
    main()