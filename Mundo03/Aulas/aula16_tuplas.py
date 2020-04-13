# Variáveis Compostas
# Tuplas, Listas e Dicionários
# () - Tuplas - Apartir do Python 3.5 o uso dos () é facultativo.
# [] - Listas
# {} - Dicionários

# Strings são variáveis compostas

lanche = ('Hamburguer', 'suco' , 'pizza' , 'pudim')
# Da mesma forma, o fateamento pode ser aplicado nas tuplas.
# print(lanche[0])
# print(lanche[1:])
# print(lanche[-1])
# print(lanche[-2])
# print(lanche[:2])
# print(len(lanche))
# As estruturas de repetição aplicadas às tuplas:
# for comida in lanche:
#     print(comida)
# É criada uma variável chamada comida

# Outra forma:
# for contador in range (0,len(lanche)):
#     print(f'Eu vou comer {lanche[contador]} na posição {contador}')

# As tuplas são imutáveis. Não é possível trocar esses elementos.
# lanche[1] = 'refrigerante'
# print(lanche[1])
#    lanche[1] = 'refrigerante'
# TypeError: 'tuple' object does not support item assignment

# Para verificar a posição da interação
# for posicao, comida in enumerate(lanche):
#     print(f"{comida} na posição {posicao}")

# Para ordenar a tupla, usamos o método sorted()
# print(sorted(lanche))
# print(lanche)
# Saída:
# ['Hamburguer', 'pizza', 'pudim', 'suco']
# ('Hamburguer', 'suco', 'pizza', 'pudim')
# Como a tupla é imutável, apenas ela é exibida de forma ordenada.
# Para isso, é necessário converter para listas para ser feita essa ordenação.

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
# Concatenação de tuplas, o que não representa a mesma coisa em ordem diferente.
# c = b + a
# print(c)
# Da mesma forma que Strings, podemos utilizar alguns métodos semelhantes:
# Contando quantas ocorrências do número 5
# print(c.count(5))

# Em que a primeira posição que encontra-se determinado elemento:
# print(c.index(8))

# Caso, seja feita essa medição apartir de
# de determinada posição (deslocamento):
# print(c.index(8, 1))
# primeiro parâmetro - elemento | segundo - apartir de qual posição

# Diferentemente de outras linguagens de programação,
# nas tuplas podem ser colocadas vários tipos de dados:
pessoa = ('João' , 39 , 'Masculino' , 83,55)

# Para apagar da memória determinada tupla,
# usamos o método del
# del(pessoa)
# print(pessoa)

# desafio 072
# Crie um programa que tenha uma
# tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# e mostrá-lo por extenso. [Sem usar IF's]

# desafio 073
# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# Na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.

# desafio 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

# desafio 075
# deselvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9;
# b) Em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares.

# desafio 076
# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência
#
# No final, mostre uma listagem de preços organizando os dados em forma tabular.
#
# listagem = ('Pão',1, 'Leite', 3.50, 'Frango', 10.90).
#
#
# desafio 077
# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

