# Declaração da classe
class Gafanhoto:
    # metodo construtor
    def __init__(self):
        # atributos de instância.
        self.nome = ''
        self.idade = 0

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos."


# Declaração do objeto
g1 = Gafanhoto()
g1.nome = 'teste'
g1.idade = 20
print(g1.mensagem())
