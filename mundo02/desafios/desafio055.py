# Desafio 55
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

somatorio_peso = 0

peso = float(input('Digite o peso da 1ª pessoa em Kg: '))

maior = peso
menor = peso

for i in range(2, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print("Maior peso digitado: {} Kg.".format(maior))
print("Menor peso digitado: {} Kg.".format(menor))
