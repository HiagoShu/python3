from pessoa import Pessoa
class Aluno(Pessoa): #subclasses da classe pessoa
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade) #chama o construtor da classe pai 
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} acabou de fazer matrícula!")