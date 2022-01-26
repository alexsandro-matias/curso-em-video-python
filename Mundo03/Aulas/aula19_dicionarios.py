# declaração de listas
# dados = list()


# tuplas -> ()
# listas -> []
# dicionários -> {}

#
# dados = dict()
#
# dados = {'nome': 'Pedro', 'idade': 25}
#
# print(dados['nome'])
# print(dados['idade'])
# print(dados)
# dados['sexo'] = 'M'
# del dados['idade']
# print(dados)


filme = {
    'título': 'Star Wars',
    'ano': '1977',
    'diretor': 'George Lucas',

    'título': 'Avengers',
    'ano': '2012',
    'diretor': 'Joss Whedon',

    'título': 'Matrix',
    'ano': '1999',
    'diretor': 'Wachowski',
}


print(filme)

# filme
# star wars       1977        George Lucas (valores)
# titulo          ano         diretor (chaves)


# # Retornando os valores do dicionário, ou seja, o conteúdo das chaves
# print(filme.values())
#
# # Retornando as chaves do dicionário:
# print(filme.keys())
#
# # Retornando ambos os valores:
# print(filme.items())

#
# for chave, valor in filme.items():
#     print(f'{chave} - {valor}')

# print(filme[1])

# locadora = []
#
# locadora.append(filme[0])
# #
# # print(locadora)
#
#
# # for k,v in enumerate(filme.items()):
# #     print(f'O {k} é {v}')
#
#
# for i in filme:
#     print(locadora[1]['ano'])
