from rich import inspect
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.traceback import install
install()

# print("Olá [red]mundo! :earth_americas: ")

caixa = Panel("Esse aqui é um painel de exemplo.", title="Mensagem", style="blue")

print(caixa)

tabela = Table(title="Tabela de Preços", style="purple")
tabela.add_column("Nome", justify="center", style="red")
tabela.add_column("Preço", justify="center", style="blue")
tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")
print(tabela)

inspect(int, all=True)


def divisao(x, y):
    return x / y


print(divisao(3, 0))
