# Módulos - Modularização

# Surgiu no início da década de 60 já que os sistema computacionais estavam ficando cada vez maiores.
# Com isso o código se torna mais legível já que a quantidade de linhas por sistema era bem menor.


# # Se tivermos uma função que não é implícita em Python como por exemplo a função de fatorial.
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         fat = 1
#         for i in range(1, n+1):
#             fat *= i
#         return fat
#
# def dobro(n):
#     return n * 2
#
# def triplo(n):
#     return n * 3
#
# # Todas essas funções irão para outro arquivo
# # (módulo) chamado de uteis.py



# numero = int(input('Digite um valor: '))
# f = fatorial(numero)
# print(f'O Fatorial de {numero} é {f}')

# Para realizar a ligação entre uteis.py e este
# módulo é necessária a palavra reservada import

# import uteis
# numero = int(input('Digite um valor: '))
# f = fatorial(numero)
# print(f'O Fatorial de {numero} é {f}')

# Nessa situação de cima ainda não suficiente. Então, precisa-se do [módulo.função]

# import uteis
# numero = int(input('Digite um valor: '))
# f = uteis.fatorial(numero)
# print(f'O Fatorial de {numero} é {f}')


# Para melhorar a legibilidade, um recurso seria a importação explícita das funções de determinado módulo.
# retirando o "." da função.
from uteis import fatorial, dobro
# Sendo o primeiro o nome do módulo e segunda é o nome da função
numero = int(input('Digite um valor: '))
f = fatorial(numero)
print(f'O Fatorial de {numero} é {f}')

# Porém essa forma, não é a recomendada,
# uma vez que se o programa tiver nome de funções iguais em módulos diferentes,
# podem haver conflitos. Assim, a primeira forma é a mais recomendada.

# Vantagens:
# Organização do código
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilização em outros projetos

# Quando a complexidade aumenta e os módulos implementados não resolvem nossas demandas,
#  vem outro conceito de PACOTES o que
# em outras linguagens de programação são chamadas de bibliotecas.
# Esses problemas são causados devido também ao aumento das quantidades de funções dentro dos módulos.
# Resumidamente, pacotes são pastas que contém vários módulos com uma quantidade menor
# de funções separados por assuntos comuns.
# Ex:
# from uteis import datas
# from uteis import cores

# Se cada arquivo .py é considerado um módulo, uma pasta pode ser considerada um pacote.
# Então para criação de um pacote, basta criar um diretório na pasta do projeto.
# Dentro deste diretório deve haver um arquivo chamado __init__.py



# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.



# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.




# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.





# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.



# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
