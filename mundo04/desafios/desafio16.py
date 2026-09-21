# Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ao
#  funcionário se apresentar.

class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f'Sou {self.nome} do {self.cargo} do setor {self.setor}'


paula = Funcionario('paula', 'Analista de RH', 'Recursos Humanos')

print(paula)
