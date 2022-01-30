# desafio 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.
# [Caso haja mais de uma posição do menor ou maior, mostre todas.]

# numeros = []
# for i in range(5):
#     numeros.append(int(input(('Digite um número:'))))

# pré-determinada lista apenas para testes.
numeros = [7, 1, 1, 8, 4, 10, 4, 7, 10, 6]

maior = max(numeros)
menor = min(numeros)

posicao_maior = numeros.index(maior)
posicao_menor = numeros.index(menor)

print("Lista: {}".format(numeros))
print("Maior: {} e está na posição {}".format(maior, posicao_maior))
print("Menor: {} e está na posição {}".format(menor, posicao_menor))


# # pré-determinada lista apenas para testes.
# numeros = [7, 1, 1, 8, 4, 10, 4, 7, 10, 6]
# maior = max(numeros)
# menor = min(numeros)
