class ContaBancaria:
    """
    Cria uma conta bancária e permite saques e depósitos
    """

    def __init__(self, id, nome, saldo):
        self.id = id
        self.titutar = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titutar} e tem R$ {self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


c1 = ContaBancaria(11, "Sandro", 3000)
print(c1)
c1.sacar(3300)
print(c1)
