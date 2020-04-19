# desafio 075
# deselvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9;
# b) Em que posição foi digitado o primeiro valor 3;
# c) Quais foram os números pares.

# Para testes
numeros = [10, 9 , 3 , 2]
pares = []

# numeros = []
# for i in range(4):
#     numeros.append(int(input('Digite um valor: ')))

for i in numeros:
    ocorrencia_9 = numeros.count(9)
    posicao_3 = numeros.index(3)

    if i % 2 == 0:
        pares.append(i)

print("Lista: {}".format(numeros))
print("Quantas vezes apareceu o valor 9: {}".format(ocorrencia_9))
print("Em que posição foi digitado o primeiro valor 3: {}".format(posicao_3))
print("Quais foram os números pares: {}".format(pares))