# desafio 080
# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort())
# No final, mostre a lista ordenada na tela.

# Adicionado no final da lista
# Adicionado na posição {}


numeros = []

for i in range(5):
    temporario = (int(input('Digite um número:')))
    menor = temporario

    if temporario <= menor(numeros):
        numeros.insert(i, temporario)
    print('Número {} adicionado na posição {}'.format(numeros[i], i))


print((numeros))