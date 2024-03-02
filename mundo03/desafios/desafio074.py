# desafio 074
# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.
import random

numeros = []

for i in range(6):
    numeros.append(int(random.randint(1, 50)))

numeros = tuple(numeros)

print(numeros)

maior = max(numeros)
menor = min(numeros)

print("O maior valor da tupla: {}".format(maior))
print("O menor valor da tupla: {}".format(menor))
