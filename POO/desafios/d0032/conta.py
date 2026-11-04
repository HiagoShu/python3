from hashlib import sha256
class ContaBancaria:
    """
    SUMMARY
    Cria uma conta bancária e permite fazer saques e depósitos

    Obj = ContaBancaria(id, nome, __saldo=0)
    """

    def __init__(self,id:int,nome:str=None, __saldo:float=0,chave:str= None):
        self._id =id 
        self._titular = nome 
        self.__saldo = __saldo  
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f'Conta {self._id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}')


    def pede_senha(self) ->str:
        from pwinput import pwinput
        while True:
            senha = pwinput('Digite a senha da conta: ')
            if len(senha) >=6:
                break
        return senha

    def validar_senha(self,chave) -> bool:
        usuario  = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self,valor):
        valor = abs(valor) #impede que seja depositado valor negativo
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')

    def sacar(self,valor:float,chave:str = None):
        valor = abs(valor) #impede que seja sacado valores negativos
        if chave is None:
            chave = self.pede_senha()
        
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque de R${valor:,.2f} negado na conta {self._id}. Saldo insuficiente.')
            else:
                self.__saldo -= valor
                print(f'Saque de R${valor:,.2f} autorizado na conta {self._id}')
        else:
            print(f"Senha não confere. Saque de R${valor:,.2f} negado na conta {self._id}.")
    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self,novonome:str=None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >=5:
                self._titular = novonome

        else:
            print("Senha não confere. Nome não alterado.")