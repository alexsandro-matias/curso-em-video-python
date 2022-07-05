dados = list()
dados.append("Pedro")
dados.append(25)

dados.append("Maria")
dados.append(19)

dados.append("João")
dados.append(32)

pessoas = list()

# jogando uma cópia de uma estrutura dentro de dados
# pessoas.append(dados[:])
# print(pessoas)

pessoas = [["pedro", 19], ["maria", 20], ["joão", 30]]
# print(pessoas)

# Neste caso, ocorre uma lista dentro de outra lista.

# acessando um elemento da lista:
print(pessoas[1])
# ['maria', 20]

# acessando um item da lista interna
print(pessoas[0][0])
print(pessoas[0][1])
# pedro
# 19

# A mesma tipo de saída acontece quando não há o fateamento dos itens da lista.
# teste = []
# teste.append('gustavo')
# teste.append(40)
#
# # outra lista que irá receber os valores da primeira lista
# galera = []
# galera.append(teste)
#
# # Neste ponto tudo normal, porém se fizer a alteração
#
# teste[0] = 'Joao'
# teste[1] = '20'
#
# galera.append(teste)
# print(galera)
# [['Joao', '20'], ['Joao', '20']]
# Esta saída ocorre devido à ligação entre as estruturas de dados.
# Então é necessário fazer o fateamento da estrutura como nas listas simples
# Para fazer esse fateamento por meio de uma cópia:

teste = []
teste.append('gustavo')
teste.append(40)

galera = []
galera.append(teste[:])  # Neste ponto

teste[0] = 'Joao'
teste[1] = '20'

galera.append(teste[:])  # E Neste ponto
print(galera)
