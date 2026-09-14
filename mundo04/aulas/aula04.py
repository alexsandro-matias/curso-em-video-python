# Declaração da classe
class Gafanhoto:
    # metodo construtor com parâmetros opcionais
    def __init__(self, nome="", idade=0):
        # atributos de instância.
        self.nome = nome
        self.idade = idade

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos."


# Declaração do objeto
g1 = Gafanhoto("Mauro", 4)
print(g1.mensagem())


g2 = Gafanhoto("Maria", 11)
g2.aniversario()
print(g2.mensagem())
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())
