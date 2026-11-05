from pessoa import *

def main():
    p = Pessoa("Gustavo",1970)
    p.nascimento = 1943
    print(p.idade)

    a = Aluno('Marcia',2010,'ADM')
    b= Aluno('Pedro',2015,'ENG')
    a.add_curso('MODA')
    print(b.cursos_oficiais)
    print(a.__dict__)


    
if __name__ == "__main__":
    main()