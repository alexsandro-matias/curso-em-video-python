# interact help
# help()
# help(input)

# outra forma é usando o doc interno ou __doc__
# print(input.__doc__)


# docstring - string de documentação (manual)
# def contador(i, f , p): #parâmetros formais
#     c = i
#     while c <= f:
#         print(f'{c}' , end='..')
#         c+=p
#     print('terminado')

# contador(2,10,2)

# help(contador) -
# Saída - Help on function contador in module __main__:
# ou seja, não tem nenhuma função da função devido a não ser explicitado.
# contador(i, f, p)
# docstring - string de documentação (manual)

# para isso, o texto deve estar entre """ no início da função.

# def contador(i, f , p): #parâmetros formais
#     """
#     Faz uma contagem e mostra na tela
#
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: Sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}' , end='..')
#         c+=p
#     print('terminado')
#
# # Neste momento, se quisermos mostrar ajuda sobre o comando,
# # será exibido a sua respectiva documentação.
#
# help(contador)




# Parâmetros opcionais
# Assinatura anterior da Função.
# def somar(a,b,c):
#     soma = a + b + c
#     print(f'A soma vale {soma}')


# Assinatura posterior da Função.
# def somar(a,b,c =0):
#     soma = a + b + c
#     print(f'A soma vale {soma}')


# somar(3,2,5)

# Mas se quisermos passar menos parâmetros como no exemplo abaixo.
# Teremos um problema.
# somar(8,4)

# Com a nova assinatura da função, quando não for passado o terceiro argumento,
# o valor padrão será o declarado na assinatura da função.
# Da mesma forma que todos os parâmetros fossem opcionais.
# def somar (a = 0 , b = 0 , c = 0):


# outra forma seria nomeiar diretamente na chamada da função:
# somar(2, b = 1, a = 7)


# Escopo de declaração de variáveis
# Local onde uma variável vai existir ou deixar de existir.

# def teste(b):
#     # a = 8
#     # Para forçar que a variável "a" se torne global,
#     # usamos a palavra reservada global
#     global a
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')


# Retorno de valores
# A palavra reservada return
# indica que existe um retorno de algum valor (resultado) de uma função.
# Utilizando a mesma função soma, só que adicionando um retorno:

def somar(a, b, c = 0):
    soma = a + b + c
    return soma

adicao = somar(3, 2, 5)
print(f'A soma vale {adicao}')


# Outra forma seria já colocar o retorno da função diretamente dentro do print()
print(somar(1,2,3))