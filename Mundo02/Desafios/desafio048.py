# Desafio 48 -
# Faça um programa que calcule a soma entre
# os números ímpares que são múltiplos de 3
# e que se encontram no intervalor de 1 até 50

for numero in range(1,50):
    if (numero % 2 != 0) and (numero % 3 == 0):
        print(numero, end=" ")