# Desafio 017
# Faça um programa que leia o comprimento do cateto oposto
# e de um cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
from math import hypot
catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(catetoAdjacente , catetoOposto)
print('O valor da hipotenusa vale: {:.2f}'.format(hipotenusa))


