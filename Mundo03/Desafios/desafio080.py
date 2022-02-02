# desafio 080
# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela.

# Adicionado no final da lista
# Adicionado na posição {}


numeros = [10, 19, 3, 5, 7, 8, 15, 4, 6]

# numeros = []

novo = numeros[1:-1]

print(novo)


# for i in range(8):

#     temporario = (int(input('Digite outro número: ')))

#     # No primeiro caso, em que a lista está vazia.
#     if len(numeros) == 0:
#         numeros.append(temporario)

#     else:
#         print(numeros)
#         if temporario < min(numeros):
#             numeros.insert(0, temporario)

#         elif temporario > max(numeros):
#             numeros.append(temporario)

#         else:
#             numeros.insert(i-1, temporario)
#     print(numeros)


# print(numeros)
