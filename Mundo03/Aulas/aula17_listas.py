# Diferentemente das tuplas, as listas podem ser alteradas mutáveis
# Declaração de uma lista:
# valores = []
# ou
# valores = list().

lanches = ['Hamburguer', 'suco' , 'pizza' , 'picolé']

# def impressao():
#     print(lanches)
#
def impressao():
    print(valores)


#  Em relação a inserção de dados se deve através de métodos
# Append().
# lanches.append('biscoito')
# impressao()

# Para inserção de dados na lista com o ciclo for.
# for contador in range(0,5):
#     valores.append(int(input('Digite mais valores: ')))
#
# impressao()

# Para inserção em determinada posição, usamos o insert()
# lanches.insert(0,'cachorro quente')
# impressao()

# Para deleção:
# del lanches[3]

# Para eliminação do último elemento, método pop
# lanches.pop(3)
# impressao()

# para deleção da primeira ocorrência um termo específico:
valores = [8,2,5,4,9,3,0]
# valores.insert(2,2)
# impressao()
# valores.remove(2)
# impressao()

# Caso o item a ser apagado não existir na lista, será lançada uma exceção.
# 'Hamburguer', 'suco', 'pizza', 'picolé', 'biscoito']
#     lanches.remove('pizza')
# ['cachorro quente', 'Hambuuguer', 'suco', 'pizza', 'picolé', 'biscoito']
# ValueError: list.remove(x): x not in list
# ['cachorro quente', 'Hambuuguer', 'suco', 'biscoito']



# Para apagar somente itens que existam, verificamos se há ou não o elemento:
#
# if 'pizza' in lanches:
#     lanches.remove('pizza')
#     print('O elemento apagado com sucesso.')
# else:
#     print('Elemento não existe na lista.')


# Criando listas usando o range:
# valores = list(range(4,11))
# impressao()

# # Para ordenação dos valores, usa-se o método sort
# valores = [8,2,5,4,9,3,0]
# valores.sort()
# impressao()
#
# # Para ordenação inversa, passamos parâmetros para esse método:
# valores.sort(reverse=True)
# impressao()
#
# # Para a quantidade de termos:
# len(valores)

# Para exibição dos valores:
# for v in valores:
#     print(v)
# ou:
# for c, v in enumerate(valores):
#     print('Na posição {} é o valor {}'.format(c,v))

# Ligação entre listas: os valores da "a" neste caso fica com uma ligação com a lista "b"
# a = valores
# b = valores
# print(a)
# print(b)
# b[2] = 8
# print(a)
# print(b)

# Para uma cópia, pode ser feita através do fateamento.
# b = a[:]
# b[2] = 8
# print(a)
# print(b)









