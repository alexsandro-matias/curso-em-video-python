# Declaração da classe
class Gafanhoto:
    # DocStrings - para documentação de uma classe.
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    """

    # metodo construtor com parâmetros opcionais
    def __init__(self, nome="", idade=0):
        # atributos de instância.
        self.nome = nome
        self.idade = idade

    # métodos de instância
    def aniversario(self):
        self.idade += 1

    # Dunder Method que será sobrescrito.
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos."

    def __getstate__(self):
        return f"Estado atual do Objeto: nome = {self.nome} e idade = {self.idade}"


g2 = Gafanhoto("Maria", 11)
g2.aniversario()
print(g2.__doc__)  # Dunder Atribute
print(g2)
print(g2.__dict__)
print(g2.__getstate__())
print(g2.__class__)
