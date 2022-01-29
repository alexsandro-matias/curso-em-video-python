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

# print(locadora)
# filme
# star wars       1977        George Lucas (valores)
# titulo          ano         diretor (chaves)

#
# # # Retornando os valores do dicionário, ou seja, o conteúdo das chaves
# print(filme.values())
# #
# # # Retornando as chaves do dicionário:
# print(filme.keys())
# #
# # # Retornando ambos os valores:
# print(filme.items())


# for chave, valor in filme.items():
#     print(f'{chave} - {valor}')

#
# for k,v in enumerate(filme.items()):
#     print(f'O {k} é {v}')


# print(filme['ano'])


# estado1 = {'uf': 'Rio de janeiro' , 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo' , 'sigla': 'SP'}
# brasil = []
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[1])

# No cliclo for é necessária fazer a cópia dos valores, uma vez que:

estado = dict()
brasil = list()

# for c in range(0,2):
#     estado['uf'] = input('Unidade Federativa: ')
#     estado['sigla'] = input('Sigla do estado: ')
#     brasil.append(estado)
#
# print(brasil)

# Unidade Federativa: rio
# Sigla do estado: rj
# Unidade Federativa: sao paulo
# Sigla do estado: sp
# [{'uf': 'sao paulo', 'sigla': 'sp'}, {'uf': 'sao pau


# Para evitar esse "erro",
# existe um método nativo do python para fazer a cópia do dicionário .copy

for c in range(0,2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())

print(brasil)
