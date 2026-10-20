class ContaBancaria:
    """
    SUMMARY
    Cria uma conta bancária e permite fazer saques e depósitos

    Obj = ContaBancaria(id, nome, __saldo=0)
    """

    def __init__(self,id,nome, __saldo=0):
        self.id =id # público (+)
        self._titular = nome #protegido (#)
        self.__saldo = __saldo  # privado (-)
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}')

    def __str__(self):
        # return f'A conta {self.id} de {self.titular} tem R${self.__saldo:,.2f} de saldo'
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self,valor):
        valor = abs(valor) #impede que seja depositado valor negativo
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self,valor):
        valor = abs(valor) #impede que seja sacado valores negativos
        if valor > self.__saldo:
            print(f'Saque de R${valor:,.2f} negado na conta {self.id}. Saldo insuficiente.')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
